#!/usr/bin/env python3
"""
GFRP Smart Search - Category-aware keyword search for ASCE/SEI 74-23

Maps user keywords to relevant chapters and searches efficiently.

Usage:
    python3 smart_search.py "lateral-torsional buckling"
    python3 smart_search.py "연결부 설계"
    python3 smart_search.py "environmental factors" --verbose
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Get the skill directory (parent of scripts/)
SKILL_DIR = Path(__file__).parent.parent
DATA_DIR = SKILL_DIR / "data" / "specification"

# Keyword to chapter mapping
KEYWORD_MAP = {
    # General and Design Requirements
    "scope": [1],
    "materials": [1],
    "load": [1, 2],
    "load combination": [1, 2],
    "lrfd": [1, 2],
    "resistance factor": [2],
    "phi": [2],
    "φ": [2],
    "time effect": [2],
    "lambda": [2],
    "λ": [2],
    "duration": [2],
    "creep": [2],
    "environmental": [2],
    "moisture": [2],
    "temperature": [2],
    "chemical": [2],
    "C_M": [2],
    "C_T": [2],
    "C_CH": [2],
    "deflection": [2],
    "drift": [2],
    "serviceability": [2],
    "fatigue": [2],

    # Tension Members (Chapter 3)
    "tension": [3],
    "tensile": [3],
    "net section": [3, 8],
    "gross section": [3],
    "pin connected": [3],
    "threaded rod": [3],

    # Compression Members (Chapter 4)
    "compression": [4, 6],
    "column": [4],
    "buckling": [4, 5],
    "flexural buckling": [4],
    "local buckling": [4, 5],
    "local flange buckling": [4, 5],
    "local web buckling": [4, 5],
    "torsional buckling": [4],
    "flexural-torsional": [4],
    "effective length": [4],
    "KL": [4],
    "slenderness": [4],

    # Flexural Members and Shear (Chapter 5)
    "beam": [5, 6],
    "flexure": [5, 6],
    "bending": [5, 6],
    "moment": [5, 6],
    "lateral-torsional": [5],
    "LTB": [5],
    "shear": [5, 7],
    "web": [5],
    "shear buckling": [5],
    "web buckling": [5],
    "stiffener": [5],
    "concentrated load": [5],
    "web crippling": [5],

    # Combined Forces (Chapter 6)
    "beam-column": [6],
    "combined": [6],
    "interaction": [6],
    "torsion": [6],
    "axial and flexure": [6],

    # Plates (Chapter 7)
    "plate": [7],
    "in-plane": [7],
    "open-hole": [7],
    "pull-through": [7, 8],
    "two-way": [7],

    # Connections (Chapter 8)
    "connection": [8],
    "bolt": [8],
    "bolted": [8],
    "bearing": [8],
    "net tension": [8],
    "shear-out": [8],
    "block shear": [8],
    "pin bearing": [8],
    "multi-row": [8],
    "geometry": [8],
    "edge distance": [8],
    "end distance": [8],

    # Seismic (Chapter 9)
    "seismic": [9],
    "earthquake": [9],
    "braced frame": [9],
    "cooling tower": [9],
    "R factor": [9],

    # Korean keywords
    "인장": [3],
    "압축": [4],
    "기둥": [4],
    "좌굴": [4, 5],
    "보": [5],
    "휨": [5],
    "전단": [5],
    "연결부": [8],
    "볼트": [8],
    "지압": [8],
    "내진": [9],
}

# File mapping
FILE_MAP = {
    1: "ASCE_SEI_74-23_part1_pages1-25.md",
    2: "ASCE_SEI_74-23_part1_pages1-25.md",  # Ch 2 spans part1 and part2
    3: "ASCE_SEI_74-23_part2_pages26-50.md",
    4: "ASCE_SEI_74-23_part2_pages26-50.md",
    5: "ASCE_SEI_74-23_part2_pages26-50.md",  # Ch 5 spans part2 and part3
    6: "ASCE_SEI_74-23_part3_pages51-75.md",
    7: "ASCE_SEI_74-23_part3_pages51-75.md",
    8: "ASCE_SEI_74-23_part4_pages76-100.md",  # Ch 8 spans part4 and part5
    9: "ASCE_SEI_74-23_part5_pages101-125.md",
}


def find_chapters(keyword: str) -> List[int]:
    """Find relevant chapters based on keyword."""
    keyword_lower = keyword.lower()
    chapters = set()

    for key, chaps in KEYWORD_MAP.items():
        if key in keyword_lower:
            chapters.update(chaps)

    # If no match, search all chapters
    if not chapters:
        chapters = set(range(1, 10))

    return sorted(list(chapters))


def search_in_file(filepath: Path, keyword: str, context_lines: int = 2) -> List[Dict]:
    """Search for keyword in file with context."""
    results = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)

        for i, line in enumerate(lines):
            if keyword_pattern.search(line):
                # Get context
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                context = lines[start:end]

                results.append({
                    'line_num': i + 1,
                    'line': line.strip(),
                    'context': ''.join(context),
                    'file': filepath.name
                })

    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)

    return results


def smart_search(keyword: str, verbose: bool = False) -> List[Dict]:
    """Perform smart search based on keyword mapping."""
    # Find relevant chapters
    chapters = find_chapters(keyword)

    if verbose:
        print(f"Keyword: '{keyword}'")
        print(f"Searching in chapters: {chapters}")
        print()

    # Get unique files to search
    files_to_search = set()
    for chapter in chapters:
        if chapter in FILE_MAP:
            files_to_search.add(FILE_MAP[chapter])

    # Search in relevant files
    all_results = []
    for filename in sorted(files_to_search):
        filepath = DATA_DIR / filename
        if filepath.exists():
            results = search_in_file(filepath, keyword)
            all_results.extend(results)

    return all_results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    keyword = sys.argv[1]
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    results = smart_search(keyword, verbose=verbose)

    if not results:
        print(f"No results found for '{keyword}'")
        print("\nTry broader keywords or check spelling.")
        return

    print(f"Found {len(results)} results for '{keyword}':\n")
    print("=" * 80)

    for i, result in enumerate(results[:20], 1):  # Limit to first 20 results
        print(f"\n[{i}] {result['file']} - Line {result['line_num']}")
        print("-" * 80)
        print(result['context'])
        print("-" * 80)

    if len(results) > 20:
        print(f"\n... and {len(results) - 20} more results (showing first 20)")

    print("\n" + "=" * 80)
    print(f"Total: {len(results)} matches")


if __name__ == "__main__":
    main()
