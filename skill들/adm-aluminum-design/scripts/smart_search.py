#!/usr/bin/env python3
"""
ADM 2020 Smart Search Tool

Intelligent search across ADM specification, commentary, design guides, and examples.
Supports category-based queries with relevance ranking.

Usage:
    python3 smart_search.py "tension member" --category specification
    python3 smart_search.py "HAZ" --welded-only
    python3 smart_search.py "buckling constants" --alloy "6061-T6"
"""

import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
import sys

# Category mappings for intelligent search
CATEGORY_KEYWORDS = {
    'tension': ['tension', 'tensile', 'axial tension', 'yield', 'Fty', 'Ftu', 'Chapter D'],
    'compression': ['compression', 'column', 'buckling', 'slenderness', 'Fc', 'Fcy', 'Chapter E', 'kL/r'],
    'flexure': ['flexure', 'bending', 'beam', 'moment', 'lateral-torsional', 'LTB', 'Mn', 'Chapter F'],
    'shear': ['shear', 'web', 'shear stress', 'Fsu', 'Chapter G'],
    'connection': ['connection', 'weld', 'bolt', 'rivet', 'joint', 'Chapter J'],
    'haz': ['HAZ', 'heat-affected', 'welded', 'weld', 'strength reduction'],
    'alloy': ['alloy', 'temper', '6061', '6063', '5052', '5083', 'material'],
    'buckling': ['buckling', 'Bc', 'Dc', 'Cc', 'local buckling', 'B.4.1', 'B.4.2'],
    'serviceability': ['deflection', 'serviceability', 'vibration', 'Chapter L'],
    'fabrication': ['fabrication', 'erection', 'tolerances', 'Chapter M'],
}

CHAPTER_FILES = {
    'A': 'specification/Chapter_A_General_Provisions.md',
    'B': 'specification/Chapter_B_Design_Requirements.md',
    'C': 'specification/Chapter_C_Design_for_Stability.md',
    'D': 'specification/Chapter_D_Design_for_Tension.md',
    'E': 'specification/Chapter_E_Design_for_Compression.md',
    'F': 'specification/Chapter_F_Design_for_Flexure.md',
    'G': 'specification/Chapter_G_Design_for_Shear.md',
    'H': 'specification/Chapter_H_Combined_Forces_Torsion.md',
    'J': 'specification/Chapter_J_Connections.md',
    'L': 'specification/Chapter_L_Serviceability.md',
    'M': 'specification/Chapter_M_Fabrication_Erection.md',
    'N': 'specification/Chapter_N_Quality_Control.md',
}

class ADMSearcher:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.results = []

    def search(self, query: str, category: str = None, welded_only: bool = False,
               alloy: str = None, max_results: int = 20) -> List[Dict]:
        """
        Search ADM documents with intelligent filtering.

        Args:
            query: Search query string
            category: Category filter (specification, commentary, examples, etc.)
            welded_only: Only show results related to welded members
            alloy: Filter by specific alloy (e.g., "6061-T6")
            max_results: Maximum number of results to return
        """
        self.results = []

        # Determine search directories
        search_dirs = self._get_search_dirs(category)

        # Perform search
        for search_dir in search_dirs:
            if not search_dir.exists():
                continue

            for md_file in search_dir.rglob('*.md'):
                self._search_file(md_file, query, welded_only, alloy)

        # Rank and sort results
        self._rank_results(query)

        return self.results[:max_results]

    def _get_search_dirs(self, category: str) -> List[Path]:
        """Determine which directories to search based on category."""
        if category == 'specification':
            return [self.data_dir / 'specification']
        elif category == 'commentary':
            return [self.data_dir / 'commentary']
        elif category == 'examples':
            return [self.data_dir / 'examples']
        elif category == 'design-guide':
            return [self.data_dir / 'design-guide']
        elif category == 'material':
            return [self.data_dir / 'reference-data']
        else:
            # Search all
            return [
                self.data_dir / 'specification',
                self.data_dir / 'commentary',
                self.data_dir / 'examples',
                self.data_dir / 'design-guide',
                self.data_dir / 'reference-data',
                self.data_dir.parent  # Include Symbols.md
            ]

    def _search_file(self, file_path: Path, query: str, welded_only: bool, alloy: str):
        """Search within a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Apply filters
            if welded_only and 'weld' not in content.lower() and 'HAZ' not in content:
                return

            if alloy and alloy not in content:
                return

            # Find matches
            pattern = re.compile(re.escape(query), re.IGNORECASE)
            matches = list(pattern.finditer(content))

            if not matches:
                # Try partial word matching
                words = query.lower().split()
                if all(word in content.lower() for word in words):
                    matches = [None]  # Placeholder for partial match

            if matches:
                # Extract context
                for match in matches[:5]:  # Limit to 5 matches per file
                    if match:
                        context = self._extract_context(content, match.start(), match.end())
                        line_num = content[:match.start()].count('\n') + 1
                    else:
                        # Partial match - find first occurrence of first word
                        first_word = query.lower().split()[0]
                        idx = content.lower().find(first_word)
                        context = self._extract_context(content, idx, idx + len(first_word))
                        line_num = content[:idx].count('\n') + 1 if idx >= 0 else 1

                    self.results.append({
                        'file': file_path.relative_to(self.data_dir.parent),
                        'line': line_num,
                        'context': context,
                        'relevance': 0  # Will be calculated later
                    })

        except Exception as e:
            print(f"Error searching {file_path}: {e}", file=sys.stderr)

    def _extract_context(self, content: str, start: int, end: int, context_lines: int = 3) -> str:
        """Extract context around match."""
        lines = content.split('\n')
        match_line = content[:start].count('\n')

        start_line = max(0, match_line - context_lines)
        end_line = min(len(lines), match_line + context_lines + 1)

        context_lines_list = lines[start_line:end_line]

        # Truncate long lines
        truncated = []
        for i, line in enumerate(context_lines_list):
            if len(line) > 150:
                line = line[:147] + '...'
            truncated.append(line)

        return '\n'.join(truncated)

    def _rank_results(self, query: str):
        """Rank results by relevance."""
        query_lower = query.lower()

        for result in self.results:
            score = 0
            context_lower = result['context'].lower()
            file_str = str(result['file']).lower()

            # Exact phrase match
            if query_lower in context_lower:
                score += 10

            # Word matches
            words = query_lower.split()
            for word in words:
                if word in context_lower:
                    score += 2

            # File priority
            if 'specification' in file_str:
                score += 5
            elif 'examples' in file_str:
                score += 4
            elif 'commentary' in file_str:
                score += 3

            # HAZ priority
            if 'haz' in query_lower and 'haz' in context_lower:
                score += 8

            # Formula indicators
            if any(pattern in context_lower for pattern in ['=', 'equation', 'formula']):
                score += 3

            result['relevance'] = score

        # Sort by relevance
        self.results.sort(key=lambda x: x['relevance'], reverse=True)

def print_results(results: List[Dict], verbose: bool = False):
    """Print search results in a readable format."""
    if not results:
        print("No results found.")
        return

    print(f"\n{'='*80}")
    print(f"Found {len(results)} results:")
    print(f"{'='*80}\n")

    for i, result in enumerate(results, 1):
        print(f"{i}. {result['file']}:{result['line']}")
        print(f"   Relevance: {result['relevance']}")
        if verbose:
            print(f"\n{result['context']}\n")
        print()

def main():
    parser = argparse.ArgumentParser(
        description='Smart search tool for ADM 2020 documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Search for tension members:
    python3 smart_search.py "tension member" --category specification

  Search for HAZ-related content:
    python3 smart_search.py "HAZ" --welded-only

  Search for alloy-specific information:
    python3 smart_search.py "buckling constants" --alloy "6061-T6"

  Search examples:
    python3 smart_search.py "welded column" --category examples
        """
    )

    parser.add_argument('query', help='Search query')
    parser.add_argument('--category', choices=['specification', 'commentary', 'examples', 'design-guide', 'material', 'all'],
                        default='all', help='Category to search')
    parser.add_argument('--welded-only', action='store_true', help='Only show welded/HAZ results')
    parser.add_argument('--alloy', help='Filter by alloy (e.g., "6061-T6")')
    parser.add_argument('--max-results', type=int, default=20, help='Maximum results to show')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show context for each result')

    args = parser.parse_args()

    # Find data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / 'data'

    if not data_dir.exists():
        print(f"Error: Data directory not found at {data_dir}", file=sys.stderr)
        sys.exit(1)

    # Perform search
    searcher = ADMSearcher(data_dir)
    results = searcher.search(
        args.query,
        category=args.category if args.category != 'all' else None,
        welded_only=args.welded_only,
        alloy=args.alloy,
        max_results=args.max_results
    )

    # Print results
    print_results(results, verbose=args.verbose)

    # Summary
    if results:
        print(f"{'='*80}")
        print(f"Top files: {', '.join(set(str(r['file']) for r in results[:5]))}")
        print(f"{'='*80}")

if __name__ == '__main__':
    main()
