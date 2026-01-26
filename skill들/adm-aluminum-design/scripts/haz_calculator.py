#!/usr/bin/env python3
"""
ADM 2020 HAZ (Heat-Affected Zone) Calculator

Calculate the strength reduction and capacity impact of welding on aluminum members.
Compares unwelded vs welded capacity for different member types.

Usage:
    python3 haz_calculator.py --alloy "6061-T6" --member-type tension --area 5.0
    python3 haz_calculator.py --alloy "6061-T6" --member-type column --area 8.0 --slenderness 40
    python3 haz_calculator.py --alloy "6061-T6" --member-type beam --section-modulus 15.0
"""

import argparse
import sys
from typing import Dict, Tuple

# Import alloy database from alloy_lookup
try:
    from alloy_lookup import ALLOY_DATABASE
except ImportError:
    # Minimal database if import fails
    ALLOY_DATABASE = {
        '6061-T6': {
            'unwelded': {'Fty': 35.0, 'Ftu': 38.0, 'Fcy': 35.0, 'Fsu': 24.0},
            'welded': {'Fty': 19.0, 'Ftu': 24.0, 'Fcy': 19.0, 'Fsu': 15.0},
            'buckling': {
                'unwelded': {'Bc': 30000, 'Dc': 200, 'Cc': 65},
                'welded': {'Bc': 16000, 'Dc': 110, 'Cc': 54}
            }
        },
    }

# Safety factors (ASD per ADM 2020)
OMEGA_T = 1.95  # Tension
OMEGA_C = 1.95  # Compression
OMEGA_B = 1.65  # Bending

class HAZCalculator:
    def __init__(self, alloy: str):
        """Initialize calculator with alloy properties."""
        alloy_upper = alloy.upper()
        if alloy_upper not in ALLOY_DATABASE:
            raise ValueError(f"Alloy {alloy} not found in database")

        self.alloy = alloy_upper
        self.data = ALLOY_DATABASE[alloy_upper]

    def calculate_tension(self, area: float) -> Dict:
        """
        Calculate tension member capacity (unwelded vs welded).

        Args:
            area: Gross cross-sectional area (in²)

        Returns:
            Dictionary with unwelded and welded capacities
        """
        # Unwelded
        Fty_u = self.data['unwelded']['Fty']
        Pn_u = Fty_u * area
        Pa_u = Pn_u / OMEGA_T

        # Welded (HAZ)
        Fty_w = self.data['welded']['Fty']
        Pn_w = Fty_w * area
        Pa_w = Pn_w / OMEGA_T

        # Reduction
        reduction = ((Pa_u - Pa_w) / Pa_u * 100) if Pa_u != 0 else 0

        return {
            'member_type': 'Tension',
            'unwelded': {
                'Fty': Fty_u,
                'Pn': Pn_u,
                'Pa': Pa_u,
            },
            'welded': {
                'Fty': Fty_w,
                'Pn': Pn_w,
                'Pa': Pa_w,
            },
            'reduction_percent': reduction,
        }

    def calculate_compression(self, area: float, slenderness: float) -> Dict:
        """
        Calculate column capacity (unwelded vs welded).

        Args:
            area: Gross cross-sectional area (in²)
            slenderness: Slenderness ratio (kL/r)

        Returns:
            Dictionary with unwelded and welded capacities
        """
        # Unwelded
        Fcy_u = self.data['unwelded']['Fcy']
        Bc_u = self.data['buckling']['unwelded']['Bc']
        Dc_u = self.data['buckling']['unwelded']['Dc']
        Cc_u = self.data['buckling']['unwelded']['Cc']

        if slenderness < Cc_u:
            # Inelastic buckling
            Fc_u = Fcy_u - Dc_u * (slenderness ** 2) / 1e6
            buckling_type_u = 'Inelastic'
        else:
            # Elastic buckling
            Fc_u = Bc_u / (slenderness ** 2)
            buckling_type_u = 'Elastic'

        Pn_u = Fc_u * area
        Pa_u = Pn_u / OMEGA_C

        # Welded (HAZ)
        Fcy_w = self.data['welded']['Fcy']
        Bc_w = self.data['buckling']['welded']['Bc']
        Dc_w = self.data['buckling']['welded']['Dc']
        Cc_w = self.data['buckling']['welded']['Cc']

        if slenderness < Cc_w:
            # Inelastic buckling
            Fc_w = Fcy_w - Dc_w * (slenderness ** 2) / 1e6
            buckling_type_w = 'Inelastic'
        else:
            # Elastic buckling
            Fc_w = Bc_w / (slenderness ** 2)
            buckling_type_w = 'Elastic'

        Pn_w = Fc_w * area
        Pa_w = Pn_w / OMEGA_C

        # Reduction
        reduction = ((Pa_u - Pa_w) / Pa_u * 100) if Pa_u != 0 else 0

        return {
            'member_type': 'Compression (Column)',
            'slenderness': slenderness,
            'unwelded': {
                'Fcy': Fcy_u,
                'Fc': Fc_u,
                'Cc': Cc_u,
                'buckling_type': buckling_type_u,
                'Pn': Pn_u,
                'Pa': Pa_u,
            },
            'welded': {
                'Fcy': Fcy_w,
                'Fc': Fc_w,
                'Cc': Cc_w,
                'buckling_type': buckling_type_w,
                'Pn': Pn_w,
                'Pa': Pa_w,
            },
            'reduction_percent': reduction,
        }

    def calculate_flexure(self, section_modulus: float) -> Dict:
        """
        Calculate beam flexural capacity (unwelded vs welded).

        Args:
            section_modulus: Elastic section modulus (in³)

        Returns:
            Dictionary with unwelded and welded capacities
        """
        # Unwelded
        Fty_u = self.data['unwelded']['Fty']
        Mn_u = Fty_u * section_modulus
        Ma_u = Mn_u / OMEGA_B

        # Welded (HAZ)
        Fty_w = self.data['welded']['Fty']
        Mn_w = Fty_w * section_modulus
        Ma_w = Mn_w / OMEGA_B

        # Reduction
        reduction = ((Ma_u - Ma_w) / Ma_u * 100) if Ma_u != 0 else 0

        return {
            'member_type': 'Flexure (Beam)',
            'unwelded': {
                'Fty': Fty_u,
                'Mn': Mn_u,
                'Ma': Ma_u,
            },
            'welded': {
                'Fty': Fty_w,
                'Mn': Mn_w,
                'Ma': Ma_w,
            },
            'reduction_percent': reduction,
        }

def print_results(results: Dict):
    """Print HAZ calculation results."""
    print(f"\n{'='*80}")
    print(f"HAZ Impact Analysis: {results['member_type']}")
    print(f"{'='*80}\n")

    if 'slenderness' in results:
        print(f"Slenderness Ratio (kL/r): {results['slenderness']:.1f}")
        print()

    # Unwelded
    print(f"{'UNWELDED (Base Metal Properties)':<40}")
    print(f"{'-'*80}")
    u = results['unwelded']

    if 'Fc' in u:
        # Column
        print(f"  Fcy = {u['Fcy']:.1f} ksi")
        print(f"  Cc  = {u['Cc']:.0f}")
        print(f"  Buckling Type: {u['buckling_type']}")
        print(f"  Fc  = {u['Fc']:.2f} ksi")
        print(f"  Pn  = {u['Pn']:.2f} kips")
        print(f"  Pa  = {u['Pa']:.2f} kips (ASD, Ω = {OMEGA_C})")
    elif 'Mn' in u:
        # Beam
        print(f"  Fty = {u['Fty']:.1f} ksi")
        print(f"  Mn  = {u['Mn']:.2f} kip-in")
        print(f"  Ma  = {u['Ma']:.2f} kip-in (ASD, Ω = {OMEGA_B})")
    else:
        # Tension
        print(f"  Fty = {u['Fty']:.1f} ksi")
        print(f"  Pn  = {u['Pn']:.2f} kips")
        print(f"  Pa  = {u['Pa']:.2f} kips (ASD, Ω = {OMEGA_T})")

    print()

    # Welded (HAZ)
    print(f"{'WELDED (HAZ Properties)':<40}")
    print(f"{'-'*80}")
    w = results['welded']

    if 'Fc' in w:
        # Column
        print(f"  Fcy(HAZ) = {w['Fcy']:.1f} ksi")
        print(f"  Cc(HAZ)  = {w['Cc']:.0f}")
        print(f"  Buckling Type: {w['buckling_type']}")
        print(f"  Fc(HAZ)  = {w['Fc']:.2f} ksi")
        print(f"  Pn(HAZ)  = {w['Pn']:.2f} kips")
        print(f"  Pa(HAZ)  = {w['Pa']:.2f} kips (ASD, Ω = {OMEGA_C})")
    elif 'Mn' in w:
        # Beam
        print(f"  Fty(HAZ) = {w['Fty']:.1f} ksi")
        print(f"  Mn(HAZ)  = {w['Mn']:.2f} kip-in")
        print(f"  Ma(HAZ)  = {w['Ma']:.2f} kip-in (ASD, Ω = {OMEGA_B})")
    else:
        # Tension
        print(f"  Fty(HAZ) = {w['Fty']:.1f} ksi")
        print(f"  Pn(HAZ)  = {w['Pn']:.2f} kips")
        print(f"  Pa(HAZ)  = {w['Pa']:.2f} kips (ASD, Ω = {OMEGA_T})")

    print()

    # Summary
    print(f"{'='*80}")
    print(f"{'CAPACITY REDUCTION DUE TO HAZ:':<50} {results['reduction_percent']:.1f}%")
    print(f"{'='*80}\n")

    # Recommendations
    print("Recommendations:")
    if results['reduction_percent'] > 40:
        print("  ⚠️  SIGNIFICANT HAZ EFFECT (>40% capacity loss)")
        print("  → Consider using 5xxx series alloy (minimal HAZ)")
        print("  → Or use bolted connections instead of welding")
    elif results['reduction_percent'] > 30:
        print("  ⚠️  Moderate HAZ effect (30-40% capacity loss)")
        print("  → Design with HAZ properties (as calculated above)")
        print("  → Verify welding quality and HAZ extent")
    else:
        print("  ✓  Acceptable HAZ effect (<30%)")
        print("  → Design with HAZ properties")

    print()

def main():
    parser = argparse.ArgumentParser(
        description='ADM 2020 HAZ (Heat-Affected Zone) Calculator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Tension member:
    python3 haz_calculator.py --alloy "6061-T6" --member-type tension --area 5.0

  Column (short):
    python3 haz_calculator.py --alloy "6061-T6" --member-type column --area 8.0 --slenderness 40

  Column (long):
    python3 haz_calculator.py --alloy "6061-T6" --member-type column --area 8.0 --slenderness 80

  Beam:
    python3 haz_calculator.py --alloy "6061-T6" --member-type beam --section-modulus 15.0

  Compare with 5083 (non-heat-treatable):
    python3 haz_calculator.py --alloy "5083-H112" --member-type column --area 8.0 --slenderness 40
        """
    )

    parser.add_argument('--alloy', required=True, help='Alloy designation (e.g., "6061-T6")')
    parser.add_argument('--member-type', required=True, choices=['tension', 'column', 'beam'],
                        help='Member type')
    parser.add_argument('--area', type=float, help='Cross-sectional area (in²) - for tension/column')
    parser.add_argument('--slenderness', type=float, help='Slenderness ratio (kL/r) - for column')
    parser.add_argument('--section-modulus', type=float, help='Elastic section modulus (in³) - for beam')

    args = parser.parse_args()

    try:
        calc = HAZCalculator(args.alloy)

        if args.member_type == 'tension':
            if not args.area:
                print("Error: --area required for tension member", file=sys.stderr)
                sys.exit(1)
            results = calc.calculate_tension(args.area)

        elif args.member_type == 'column':
            if not args.area or not args.slenderness:
                print("Error: --area and --slenderness required for column", file=sys.stderr)
                sys.exit(1)
            results = calc.calculate_compression(args.area, args.slenderness)

        elif args.member_type == 'beam':
            if not args.section_modulus:
                print("Error: --section-modulus required for beam", file=sys.stderr)
                sys.exit(1)
            results = calc.calculate_flexure(args.section_modulus)

        print_results(results)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("\nAvailable alloys: 6061-T6, 6061-T4, 6063-T6, 6063-T5, 5052-H32, 5083-H112")
        sys.exit(1)

if __name__ == '__main__':
    main()
