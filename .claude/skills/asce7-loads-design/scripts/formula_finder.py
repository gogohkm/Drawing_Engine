#!/usr/bin/env python3
"""
ASCE 7-22 Formula Finder

Extracts formulas and equations from ASCE 7 chapters with context.

Usage:
    python3 formula_finder.py "V =" Chapter_12_Seismic_Design_Requirements_Building.md
    python3 formula_finder.py "qz" Chapter_26_Wind_Loads_General_Requirements.md
    python3 formula_finder.py --all Chapter_02_Combinations_of_Loads.md
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Formula:
    """Formula with context"""
    equation: str
    equation_number: str
    line_number: int
    context_before: List[str]
    context_after: List[str]
    variables: List[str]

def extract_formulas(filepath: Path, pattern: str = None, context_lines: int = 3) -> List[Formula]:
    """Extract formulas from markdown file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    formulas = []

    # Pattern for equation numbers like (2.3-1), (12.8-1), etc.
    eq_num_pattern = r'\((\d+(?:\.\d+)?-\d+[a-z]?)\)'

    # Pattern for LaTeX math
    latex_pattern = r'\$[^$]+\$'

    # Pattern for common formula structures
    formula_patterns = [
        r'[A-Z][a-z]?\s*=\s*',  # V =, F =, etc.
        r'\$[A-Z_][^$]*=',      # $V = ...$
        r'^\d+[a-z]?\.\s+[A-Z]',  # 1a. D
    ]

    for i, line in enumerate(lines):
        # Check if line contains pattern (if specified)
        if pattern and pattern.lower() not in line.lower():
            continue

        # Check if line contains formula indicators
        is_formula = False

        # Check for equation numbers
        if re.search(eq_num_pattern, line):
            is_formula = True

        # Check for LaTeX math
        if re.search(latex_pattern, line):
            is_formula = True

        # Check for formula patterns
        for fp in formula_patterns:
            if re.search(fp, line):
                is_formula = True
                break

        if not is_formula:
            continue

        # Extract equation number
        eq_num_match = re.search(eq_num_pattern, line)
        eq_num = eq_num_match.group(1) if eq_num_match else ""

        # Extract equation text
        equation_text = line.strip()

        # Extract context
        context_before = []
        for j in range(max(0, i - context_lines), i):
            if lines[j].strip():
                context_before.append(lines[j].strip())

        context_after = []
        for j in range(i + 1, min(len(lines), i + 1 + context_lines)):
            if lines[j].strip():
                context_after.append(lines[j].strip())

        # Extract variables (capital letters or Greek symbols)
        variables = re.findall(r'\$([A-Z][a-z]?(?:_[a-z0-9]+)?)\$', line)

        formulas.append(Formula(
            equation=equation_text,
            equation_number=eq_num,
            line_number=i + 1,
            context_before=context_before,
            context_after=context_after,
            variables=list(set(variables))
        ))

    return formulas

def main():
    parser = argparse.ArgumentParser(description='Find formulas in ASCE 7 chapters')
    parser.add_argument('pattern', nargs='?', help='Pattern to search for (e.g., "V =", "qz")')
    parser.add_argument('file', help='Chapter file to search')
    parser.add_argument('--all', action='store_true', help='Show all formulas')
    parser.add_argument('--context', type=int, default=3, help='Context lines (default: 3)')

    args = parser.parse_args()

    # Resolve file path
    if not Path(args.file).exists():
        # Try in data directory
        data_dir = Path(__file__).parent.parent / 'data'
        filepath = data_dir / args.file
        if not filepath.exists():
            print(f"Error: File not found: {args.file}")
            return 1
    else:
        filepath = Path(args.file)

    # Extract formulas
    pattern = None if args.all else args.pattern
    formulas = extract_formulas(filepath, pattern, args.context)

    if not formulas:
        print(f"No formulas found matching: '{pattern if pattern else 'all'}'")
        return 1

    print(f"\n{'='*80}")
    print(f"Formulas in: {filepath.name}")
    if pattern:
        print(f"Matching: '{pattern}'")
    print(f"{'='*80}\n")

    for i, formula in enumerate(formulas, 1):
        print(f"{'─'*80}")
        print(f"Formula {i}:")
        if formula.equation_number:
            print(f"Equation Number: {formula.equation_number}")
        print(f"Line: {formula.line_number}")
        print()

        # Context before
        if formula.context_before:
            print("Context:")
            for line in formula.context_before[-2:]:
                print(f"  {line}")
            print()

        # Equation
        print(f"Equation:")
        print(f"  {formula.equation}")
        print()

        # Variables
        if formula.variables:
            print(f"Variables: {', '.join(formula.variables)}")
            print()

        # Context after
        if formula.context_after:
            print("Where:")
            for line in formula.context_after[:2]:
                print(f"  {line}")
            print()

    print(f"{'─'*80}")
    print(f"\nTotal formulas found: {len(formulas)}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
