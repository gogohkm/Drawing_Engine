#!/usr/bin/env python3
"""
ADM 2020 Alloy Property Lookup Tool

Quick lookup of aluminum alloy properties including unwelded, welded (HAZ),
and buckling constants.

Usage:
    python3 alloy_lookup.py "6061-T6"
    python3 alloy_lookup.py "6061-T6" --welded
    python3 alloy_lookup.py "6061-T6" --buckling
    python3 alloy_lookup.py --list-alloys
"""

import argparse
import sys
from typing import Dict, Optional

# Material properties database (from ADM 2020 Part IV)
# Format: alloy: {unwelded: {...}, welded: {...}, buckling: {...}}

ALLOY_DATABASE = {
    '6061-T6': {
        'description': 'Most common structural aluminum alloy',
        'product_forms': 'Extrusions, plate, sheet',
        'unwelded': {
            'Fty': 35.0,  # ksi
            'Ftu': 38.0,  # ksi
            'Fcy': 35.0,  # ksi
            'Fsu': 24.0,  # ksi
            'E': 10100,   # ksi
        },
        'welded': {
            'Fty': 19.0,  # ksi (46% reduction)
            'Ftu': 24.0,  # ksi (37% reduction)
            'Fcy': 19.0,  # ksi
            'Fsu': 15.0,  # ksi
            'E': 10100,   # ksi (unchanged)
        },
        'buckling': {
            'unwelded': {
                'Bc': 30000,  # ksi
                'Dc': 200,
                'Cc': 65,
            },
            'welded': {
                'Bc': 16000,  # ksi (reduced)
                'Dc': 110,
                'Cc': 54,
            }
        },
        'temperature_limit': {
            'sustained': 200,  # °F for T6 temper
            'short_term': 250,
        },
        'notes': [
            'Most common choice for structural design',
            'Significant HAZ effect (46% yield strength loss)',
            'Temperature > 200°F causes strength degradation',
        ]
    },

    '6061-T4': {
        'description': 'Solution heat treated, naturally aged (formable)',
        'product_forms': 'Extrusions, plate, sheet',
        'unwelded': {
            'Fty': 16.0,
            'Ftu': 26.0,
            'Fcy': 16.0,
            'Fsu': 16.0,
            'E': 10100,
        },
        'welded': {
            'Fty': 16.0,  # Minimal HAZ effect (already soft)
            'Ftu': 26.0,
            'Fcy': 16.0,
            'Fsu': 16.0,
            'E': 10100,
        },
        'buckling': {
            'unwelded': {
                'Bc': 14000,
                'Dc': 90,
                'Cc': 50,
            },
            'welded': {
                'Bc': 14000,  # Minimal change
                'Dc': 90,
                'Cc': 50,
            }
        },
        'temperature_limit': {
            'sustained': 200,
            'short_term': 250,
        },
        'notes': [
            'Lower strength but good formability',
            'Minimal HAZ effect (already in soft condition)',
        ]
    },

    '6063-T6': {
        'description': 'Architectural extrusions',
        'product_forms': 'Extrusions (complex shapes)',
        'unwelded': {
            'Fty': 25.0,
            'Ftu': 30.0,
            'Fcy': 25.0,
            'Fsu': 19.0,
            'E': 10100,
        },
        'welded': {
            'Fty': 14.0,  # 44% reduction
            'Ftu': 20.0,  # 33% reduction
            'Fcy': 14.0,
            'Fsu': 13.0,
            'E': 10100,
        },
        'buckling': {
            'unwelded': {
                'Bc': 22000,
                'Dc': 140,
                'Cc': 59,
            },
            'welded': {
                'Bc': 12000,
                'Dc': 80,
                'Cc': 52,
            }
        },
        'temperature_limit': {
            'sustained': 200,
            'short_term': 250,
        },
        'notes': [
            'Common for architectural applications',
            'Lower strength than 6061-T6',
            'Excellent extrudability',
        ]
    },

    '6063-T5': {
        'description': 'Architectural extrusions (lower strength)',
        'product_forms': 'Extrusions',
        'unwelded': {
            'Fty': 16.0,
            'Ftu': 22.0,
            'Fcy': 16.0,
            'Fsu': 14.0,
            'E': 10100,
        },
        'welded': {
            'Fty': 9.0,   # 44% reduction
            'Ftu': 14.0,  # 36% reduction
            'Fcy': 9.0,
            'Fsu': 9.0,
            'E': 10100,
        },
        'buckling': {
            'unwelded': {
                'Bc': 14000,
                'Dc': 80,
                'Cc': 53,
            },
            'welded': {
                'Bc': 7500,
                'Dc': 45,
                'Cc': 47,
            }
        },
        'temperature_limit': {
            'sustained': 200,
            'short_term': 250,
        },
        'notes': [
            'Lower strength architectural alloy',
            'Good for light-duty applications',
        ]
    },

    '5052-H32': {
        'description': 'Marine, non-heat-treatable',
        'product_forms': 'Sheet, plate',
        'unwelded': {
            'Fty': 23.0,
            'Ftu': 31.0,
            'Fcy': 23.0,
            'Fsu': 20.0,
            'E': 10200,
        },
        'welded': {
            'Fty': 23.0,  # Minimal HAZ effect!
            'Ftu': 31.0,
            'Fcy': 23.0,
            'Fsu': 20.0,
            'E': 10200,
        },
        'buckling': {
            'unwelded': {
                'Bc': 20000,
                'Dc': 130,
                'Cc': 57,
            },
            'welded': {
                'Bc': 20000,  # No change (non-heat-treatable)
                'Dc': 130,
                'Cc': 57,
            }
        },
        'temperature_limit': {
            'sustained': 200,
            'short_term': 300,
        },
        'notes': [
            'Non-heat-treatable (strain-hardened)',
            'Minimal HAZ effect - excellent for welding!',
            'Good corrosion resistance',
        ]
    },

    '5083-H112': {
        'description': 'Marine, high strength, non-heat-treatable',
        'product_forms': 'Plate, extrusions',
        'unwelded': {
            'Fty': 35.0,
            'Ftu': 44.0,
            'Fcy': 35.0,
            'Fsu': 27.0,
            'E': 10400,
        },
        'welded': {
            'Fty': 35.0,  # Minimal HAZ effect!
            'Ftu': 44.0,
            'Fcy': 35.0,
            'Fsu': 27.0,
            'E': 10400,
        },
        'buckling': {
            'unwelded': {
                'Bc': 30000,
                'Dc': 200,
                'Cc': 65,
            },
            'welded': {
                'Bc': 30000,  # No change!
                'Dc': 200,
                'Cc': 65,
            }
        },
        'temperature_limit': {
            'sustained': 200,
            'short_term': 300,
        },
        'notes': [
            'Highest strength of 5xxx series',
            'Minimal HAZ effect - BEST for welded structures!',
            'Same strength as 6061-T6 but no HAZ penalty',
            'Excellent corrosion resistance',
        ]
    },
}

def lookup_alloy(alloy: str, welded: bool = False, buckling: bool = False) -> Optional[Dict]:
    """
    Look up alloy properties.

    Args:
        alloy: Alloy designation (e.g., "6061-T6")
        welded: Return welded (HAZ) properties
        buckling: Return buckling constants

    Returns:
        Dictionary with alloy properties or None if not found
    """
    alloy_upper = alloy.upper()

    if alloy_upper not in ALLOY_DATABASE:
        return None

    data = ALLOY_DATABASE[alloy_upper]

    if buckling:
        return {
            'alloy': alloy_upper,
            'description': data['description'],
            'buckling': data['buckling']['welded' if welded else 'unwelded'],
            'condition': 'welded' if welded else 'unwelded',
        }
    else:
        return {
            'alloy': alloy_upper,
            'description': data['description'],
            'product_forms': data['product_forms'],
            'properties': data['welded' if welded else 'unwelded'],
            'temperature_limit': data['temperature_limit'],
            'condition': 'welded' if welded else 'unwelded',
            'notes': data['notes'],
        }

def print_properties(data: Dict):
    """Print alloy properties in readable format."""
    print(f"\n{'='*70}")
    print(f"Alloy: {data['alloy']} ({'Welded (HAZ)' if data['condition'] == 'welded' else 'Unwelded'})")
    print(f"{'='*70}")
    print(f"Description: {data['description']}")

    if 'buckling' in data:
        # Buckling constants
        print(f"\nBuckling Constants:")
        print(f"  Bc = {data['buckling']['Bc']:,} ksi")
        print(f"  Dc = {data['buckling']['Dc']}")
        print(f"  Cc = {data['buckling']['Cc']}")
    else:
        # Mechanical properties
        print(f"Product Forms: {data['product_forms']}")
        print(f"\nMechanical Properties:")
        props = data['properties']
        print(f"  Fty (Tensile Yield)      = {props['Fty']:.1f} ksi")
        print(f"  Ftu (Tensile Ultimate)   = {props['Ftu']:.1f} ksi")
        print(f"  Fcy (Compressive Yield)  = {props['Fcy']:.1f} ksi")
        print(f"  Fsu (Shear Ultimate)     = {props['Fsu']:.1f} ksi")
        print(f"  E   (Modulus)            = {props['E']:,} ksi")

        print(f"\nTemperature Limits:")
        print(f"  Sustained: {data['temperature_limit']['sustained']}°F")
        print(f"  Short-term: {data['temperature_limit']['short_term']}°F")

        print(f"\nNotes:")
        for note in data['notes']:
            print(f"  - {note}")

    print(f"{'='*70}\n")

def compare_welded_unwelded(alloy: str):
    """Compare welded vs unwelded properties."""
    unwelded = lookup_alloy(alloy, welded=False)
    welded = lookup_alloy(alloy, welded=True)

    if not unwelded or not welded:
        print(f"Error: Alloy {alloy} not found in database", file=sys.stderr)
        return

    print(f"\n{'='*70}")
    print(f"Alloy: {alloy.upper()} - HAZ Strength Reduction Comparison")
    print(f"{'='*70}")

    props_u = unwelded['properties']
    props_w = welded['properties']

    print(f"\n{'Property':<20} {'Unwelded':>12} {'Welded (HAZ)':>12} {'Reduction':>12}")
    print(f"{'-'*70}")

    for prop in ['Fty', 'Ftu', 'Fcy', 'Fsu']:
        u_val = props_u[prop]
        w_val = props_w[prop]
        reduction = ((u_val - w_val) / u_val * 100) if u_val != 0 else 0
        print(f"{prop:<20} {u_val:>10.1f} ksi {w_val:>10.1f} ksi {reduction:>10.1f}%")

    # Buckling constants comparison
    buck_u = ALLOY_DATABASE[alloy.upper()]['buckling']['unwelded']
    buck_w = ALLOY_DATABASE[alloy.upper()]['buckling']['welded']

    print(f"\n{'Buckling Constant':<20} {'Unwelded':>12} {'Welded':>12} {'Reduction':>12}")
    print(f"{'-'*70}")

    for const in ['Bc', 'Dc', 'Cc']:
        u_val = buck_u[const]
        w_val = buck_w[const]
        reduction = ((u_val - w_val) / u_val * 100) if u_val != 0 else 0
        print(f"{const:<20} {u_val:>12} {w_val:>12} {reduction:>10.1f}%")

    print(f"\n{'='*70}\n")

def list_alloys():
    """List all available alloys."""
    print(f"\n{'='*70}")
    print(f"Available Alloys in Database:")
    print(f"{'='*70}\n")

    for alloy, data in sorted(ALLOY_DATABASE.items()):
        print(f"{alloy:<15} - {data['description']}")

    print(f"\n{'='*70}\n")

def main():
    parser = argparse.ArgumentParser(
        description='ADM 2020 Alloy Property Lookup Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Look up unwelded properties:
    python3 alloy_lookup.py "6061-T6"

  Look up welded (HAZ) properties:
    python3 alloy_lookup.py "6061-T6" --welded

  Look up buckling constants:
    python3 alloy_lookup.py "6061-T6" --buckling

  Compare welded vs unwelded:
    python3 alloy_lookup.py "6061-T6" --compare

  List all available alloys:
    python3 alloy_lookup.py --list-alloys
        """
    )

    parser.add_argument('alloy', nargs='?', help='Alloy designation (e.g., "6061-T6")')
    parser.add_argument('--welded', action='store_true', help='Show welded (HAZ) properties')
    parser.add_argument('--buckling', action='store_true', help='Show buckling constants')
    parser.add_argument('--compare', action='store_true', help='Compare welded vs unwelded')
    parser.add_argument('--list-alloys', action='store_true', help='List all available alloys')

    args = parser.parse_args()

    if args.list_alloys:
        list_alloys()
        return

    if not args.alloy:
        parser.print_help()
        sys.exit(1)

    if args.compare:
        compare_welded_unwelded(args.alloy)
    else:
        data = lookup_alloy(args.alloy, welded=args.welded, buckling=args.buckling)
        if data:
            print_properties(data)
        else:
            print(f"Error: Alloy '{args.alloy}' not found in database", file=sys.stderr)
            print("\nAvailable alloys:")
            for alloy in sorted(ALLOY_DATABASE.keys()):
                print(f"  - {alloy}")
            sys.exit(1)

if __name__ == '__main__':
    main()
