#!/usr/bin/env python3
"""
ASCE 7-22 Load Combination Generator

Generates applicable load combinations per Chapter 2.

Usage:
    python3 load_combinator.py --design LRFD --loads D,L,W
    python3 load_combinator.py --design ASD --loads D,L,S,E --seismic
    python3 load_combinator.py --list
"""

import argparse
import sys
from typing import List, Set

# LRFD (Strength Design) Load Combinations per Section 2.3
LRFD_BASIC = [
    ("1.4D", "2.3-1", "Dead load only"),
    ("1.2D + 1.6L + 0.5(Lr or S or R)", "2.3-2", "Dead + Live + Secondary"),
    ("1.2D + 1.6(Lr or S or R) + (L or 0.5W)", "2.3-3", "Dead + Roof/Snow/Rain + Secondary"),
    ("1.2D + 1.0W + L + 0.5(Lr or S or R)", "2.3-4", "Dead + Wind + Secondary"),
    ("1.2D + 1.0E + L + 0.2S", "2.3-5", "Dead + Seismic + Secondary"),
    ("0.9D + 1.0W + 1.6H", "2.3-6", "Dead (reduced) + Wind + Lateral Earth"),
    ("0.9D + 1.0E + 1.6H", "2.3-7", "Dead (reduced) + Seismic + Lateral Earth"),
]

LRFD_SEISMIC_ENHANCED = [
    ("1.2D + Eh + Ev + L + 0.2S", "2.3-12", "Dead + Seismic (detailed) + Secondary"),
    ("(0.9 - 0.2SDS)D + ρQE + 1.6H", "2.3-13", "Dead (reduced by seismic) + Redundancy + Lateral Earth"),
]

LRFD_FLOOD = [
    ("1.2D + 1.0W + 2.0Fa + L + 0.5(Lr or S or R)", "2.3-7", "Flood: V Zone or Coastal A Zone"),
    ("1.2D + 1.0W + 1.0Fa + L + 0.5(Lr or S or R)", "2.3-8", "Flood: Noncoastal A Zone"),
    ("0.9D - 1.0W + 1.0Fa", "2.3-9", "Flood: Uplift/buoyancy"),
]

LRFD_ICE = [
    ("1.2D + 1.0Wi + L + 0.5(Lr or S or R)", "2.3-10", "Ice: Wind-on-ice"),
    ("0.9D - 1.0Wi + 1.6H", "2.3-11", "Ice: Wind-on-ice (reduced dead)"),
]

# ASD (Allowable Stress Design) Load Combinations per Section 2.4
ASD_BASIC = [
    ("D", "2.4-1", "Dead load only"),
    ("D + L", "2.4-2", "Dead + Live"),
    ("D + (Lr or S or R)", "2.4-3", "Dead + Roof/Snow/Rain"),
    ("D + 0.75L + 0.75(Lr or S or R)", "2.4-4", "Dead + 0.75(Live + Secondary)"),
    ("D + (0.6W or 0.7E)", "2.4-5", "Dead + Wind or Seismic (reduced)"),
    ("D + 0.75L + 0.75(0.6W) + 0.75(Lr or S or R)", "2.4-6", "Dead + 0.75(Live + Wind + Secondary)"),
    ("D + 0.75L + 0.75(0.7E) + 0.75S", "2.4-7", "Dead + 0.75(Live + Seismic + Snow)"),
    ("0.6D + 0.6W + H", "2.4-8", "Dead (reduced) + Wind + Lateral Earth"),
    ("0.6D + 0.7E + H", "2.4-9", "Dead (reduced) + Seismic + Lateral Earth"),
]

def filter_combinations(combinations: List[tuple], loads: Set[str], seismic: bool = False,
                       flood: bool = False, ice: bool = False) -> List[tuple]:
    """Filter combinations based on applicable loads"""
    filtered = []

    for combo, eq_num, desc in combinations:
        # Check if combination uses only specified loads
        combo_loads = set()

        if 'D' in combo:
            combo_loads.add('D')
        if 'L' in combo:
            combo_loads.add('L')
        if 'Lr' in combo or 'S' in combo or 'R' in combo:
            combo_loads.add('Lr/S/R')
        if 'W' in combo and 'Wi' not in combo:
            combo_loads.add('W')
        if 'E' in combo or 'Eh' in combo:
            combo_loads.add('E')
        if 'H' in combo:
            combo_loads.add('H')
        if 'Fa' in combo:
            combo_loads.add('Fa')
        if 'Wi' in combo:
            combo_loads.add('Wi')

        # Check if loads are applicable
        is_applicable = True

        # Must have Dead load
        if 'D' not in loads:
            continue

        # Check each load in combination
        for load in combo_loads:
            if load == 'D':
                continue
            elif load == 'Lr/S/R':
                if not any(l in loads for l in ['Lr', 'S', 'R']):
                    is_applicable = False
            elif load == 'E' and not seismic:
                is_applicable = False
            elif load == 'Fa' and not flood:
                is_applicable = False
            elif load == 'Wi' and not ice:
                is_applicable = False
            elif load not in loads:
                is_applicable = False

        if is_applicable:
            filtered.append((combo, eq_num, desc))

    return filtered

def main():
    parser = argparse.ArgumentParser(description='Generate ASCE 7-22 load combinations')
    parser.add_argument('--design', choices=['LRFD', 'ASD'], default='LRFD',
                       help='Design method (default: LRFD)')
    parser.add_argument('--loads', type=str, required=True,
                       help='Comma-separated loads (e.g., D,L,W,S)')
    parser.add_argument('--seismic', action='store_true',
                       help='Include seismic load combinations')
    parser.add_argument('--flood', action='store_true',
                       help='Include flood load combinations')
    parser.add_argument('--ice', action='store_true',
                       help='Include ice load combinations')
    parser.add_argument('--list', action='store_true',
                       help='List available loads')

    args = parser.parse_args()

    if args.list:
        print("\nAvailable Load Types:")
        print("  D   = Dead load")
        print("  L   = Live load")
        print("  Lr  = Roof live load")
        print("  S   = Snow load")
        print("  R   = Rain load")
        print("  W   = Wind load")
        print("  E   = Seismic load")
        print("  H   = Lateral earth pressure")
        print("  Fa  = Flood load")
        print("  Wi  = Wind-on-ice load")
        print("\nDesign Methods:")
        print("  LRFD = Load and Resistance Factor Design (Strength Design)")
        print("  ASD  = Allowable Stress Design")
        return 0

    # Parse loads
    loads = set(load.strip().upper() for load in args.loads.split(','))

    # Validate loads
    valid_loads = {'D', 'L', 'Lr', 'S', 'R', 'W', 'E', 'H', 'Fa', 'Wi'}
    invalid = loads - valid_loads
    if invalid:
        print(f"Error: Invalid loads: {', '.join(invalid)}")
        print("Use --list to see available loads")
        return 1

    # Dead load is required
    if 'D' not in loads:
        print("Error: Dead load (D) is required")
        return 1

    # Generate combinations
    print(f"\n{'='*80}")
    print(f"ASCE 7-22 Load Combinations - {args.design}")
    print(f"Loads: {', '.join(sorted(loads))}")
    if args.seismic:
        print("Including: Seismic combinations")
    if args.flood:
        print("Including: Flood combinations")
    if args.ice:
        print("Including: Ice combinations")
    print(f"{'='*80}\n")

    # Get applicable combinations
    if args.design == 'LRFD':
        combinations = filter_combinations(LRFD_BASIC, loads, args.seismic, args.flood, args.ice)

        if args.seismic and 'E' in loads:
            combinations.extend(filter_combinations(LRFD_SEISMIC_ENHANCED, loads, True, False, False))

        if args.flood and 'Fa' in loads:
            combinations.extend(filter_combinations(LRFD_FLOOD, loads, False, True, False))

        if args.ice and 'Wi' in loads:
            combinations.extend(filter_combinations(LRFD_ICE, loads, False, False, True))
    else:  # ASD
        combinations = filter_combinations(ASD_BASIC, loads, args.seismic, args.flood, args.ice)

    if not combinations:
        print("No applicable load combinations for specified loads.")
        return 1

    # Display combinations
    for i, (combo, eq_num, desc) in enumerate(combinations, 1):
        print(f"{i}. {combo}")
        print(f"   Eq. {eq_num}: {desc}")
        print()

    print(f"{'─'*80}")
    print(f"Total combinations: {len(combinations)}")
    print(f"\nReference: ASCE 7-22 Chapter 2")

    return 0

if __name__ == '__main__':
    sys.exit(main())
