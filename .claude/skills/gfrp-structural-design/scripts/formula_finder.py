#!/usr/bin/env python3
"""
GFRP Formula Finder - Extract formulas from ASCE/SEI 74-23 with context

Finds mathematical formulas and equations with surrounding context.

Usage:
    python3 formula_finder.py "M_n"
    python3 formula_finder.py "F_cre" --chapter 4
    python3 formula_finder.py "λ" --context 5
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict

# Get the skill directory
SKILL_DIR = Path(__file__).parent.parent
DATA_DIR = SKILL_DIR / "data" / "specification"

# Common formula patterns
FORMULA_PATTERNS = [
    r'\$\$.*?\$\$',  # Display math: $$...$$
    r'\$[^$]+\$',    # Inline math: $...$
    r'[A-Z][a-z]*_[a-z]+\s*=',  # Variable assignment: F_L =
    r'\b[A-Z]_[a-z]+\s*=',  # Short variable: M_n =
    r'φ\s*=',  # Phi =
    r'λ\s*=',  # Lambda =
    r'Equation\s+\(\d+-\d+\)',  # Equation reference
]


def extract_formulas(filepath: Path, pattern: str = None, context_lines: int = 3) -> List[Dict]:
    """Extract formulas from file with context."""
    results = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            is_formula = False

            # Check if line contains formula
            if pattern:
                # User-specified pattern
                if re.search(re.escape(pattern), line, re.IGNORECASE):
                    is_formula = True
            else:
                # Check against common patterns
                for formula_pattern in FORMULA_PATTERNS:
                    if re.search(formula_pattern, line):
                        is_formula = True
                        break

            if is_formula:
                # Get context
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                context = lines[start:end]

                # Look for equation number
                eq_num = None
                for ctx_line in context:
                    eq_match = re.search(r'Equation\s+\((\d+-\d+)\)', ctx_line)
                    if eq_match:
                        eq_num = eq_match.group(1)
                        break

                results.append({
                    'line_num': i + 1,
                    'line': line.strip(),
                    'context': ''.join(context),
                    'file': filepath.name,
                    'equation_num': eq_num
                })

    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)

    return results


def find_formulas_in_chapter(chapter: int, pattern: str = None, context_lines: int = 3) -> List[Dict]:
    """Find formulas in specific chapter."""
    # Map chapter to file
    file_map = {
        1: ["ASCE_SEI_74-23_part1_pages1-25.md"],
        2: ["ASCE_SEI_74-23_part1_pages1-25.md", "ASCE_SEI_74-23_part2_pages26-50.md"],
        3: ["ASCE_SEI_74-23_part2_pages26-50.md"],
        4: ["ASCE_SEI_74-23_part2_pages26-50.md"],
        5: ["ASCE_SEI_74-23_part2_pages26-50.md", "ASCE_SEI_74-23_part3_pages51-75.md"],
        6: ["ASCE_SEI_74-23_part3_pages51-75.md"],
        7: ["ASCE_SEI_74-23_part3_pages51-75.md", "ASCE_SEI_74-23_part4_pages76-100.md"],
        8: ["ASCE_SEI_74-23_part4_pages76-100.md", "ASCE_SEI_74-23_part5_pages101-125.md"],
        9: ["ASCE_SEI_74-23_part5_pages101-125.md"],
    }

    files = file_map.get(chapter, [])
    all_results = []

    for filename in files:
        filepath = DATA_DIR / filename
        if filepath.exists():
            results = extract_formulas(filepath, pattern, context_lines)
            all_results.extend(results)

    return all_results


def find_all_formulas(pattern: str = None, context_lines: int = 3) -> List[Dict]:
    """Find formulas in all files."""
    all_results = []

    for filepath in sorted(DATA_DIR.glob("*.md")):
        results = extract_formulas(filepath, pattern, context_lines)
        all_results.extend(results)

    return all_results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    pattern = sys.argv[1]

    # Parse options
    chapter = None
    context_lines = 3

    for i, arg in enumerate(sys.argv[2:], 2):
        if arg in ["--chapter", "-c"] and i + 1 < len(sys.argv):
            chapter = int(sys.argv[i + 1])
        elif arg in ["--context", "-x"] and i + 1 < len(sys.argv):
            context_lines = int(sys.argv[i + 1])

    # Search
    if chapter:
        print(f"Searching for '{pattern}' in Chapter {chapter}...")
        results = find_formulas_in_chapter(chapter, pattern, context_lines)
    else:
        print(f"Searching for '{pattern}' in all chapters...")
        results = find_all_formulas(pattern, context_lines)

    if not results:
        print(f"\nNo formulas found matching '{pattern}'")
        print("\nTry:")
        print("  - Different variable name (e.g., M_n, P_n, F_L)")
        print("  - Greek letters (φ, λ)")
        print("  - Broader search without pattern")
        return

    print(f"\nFound {len(results)} formulas matching '{pattern}':\n")
    print("=" * 80)

    for i, result in enumerate(results[:15], 1):  # Limit to 15 results
        print(f"\n[{i}] {result['file']} - Line {result['line_num']}", end='')
        if result['equation_num']:
            print(f" - Equation ({result['equation_num']})")
        else:
            print()
        print("-" * 80)
        print(result['context'])
        print("-" * 80)

    if len(results) > 15:
        print(f"\n... and {len(results) - 15} more results (showing first 15)")

    print("\n" + "=" * 80)
    print(f"Total: {len(results)} matches")

    # Show equation numbers if found
    eq_nums = [r['equation_num'] for r in results if r['equation_num']]
    if eq_nums:
        print(f"\nEquation numbers found: {', '.join(sorted(set(eq_nums)))}")


if __name__ == "__main__":
    main()
