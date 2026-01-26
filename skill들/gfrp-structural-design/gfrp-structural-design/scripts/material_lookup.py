#!/usr/bin/env python3
"""
GFRP Material Properties Lookup

Quick reference for typical GFRP material properties.

Usage:
    python3 material_lookup.py --property E_L
    python3 material_lookup.py --all
    python3 material_lookup.py --compare
"""

import sys
from typing import Dict

# Typical GFRP material properties (from material-properties-guide.md)
PROPERTIES = {
    'E_L': {
        'name': 'Longitudinal Elastic Modulus',
        'typical_range': '2,000 - 4,000 ksi (14 - 28 GPa)',
        'typical_value': '2,500 ksi (17 GPa)',
        'units': 'ksi (MPa)',
        'notes': 'Parallel to fibers, ~20% of steel',
        'test_standard': 'ASTM D3039',
    },
    'E_T': {
        'name': 'Transverse Elastic Modulus',
        'typical_range': '800 - 1,500 ksi (5.5 - 10 GPa)',
        'typical_value': '1,000 ksi (7 GPa)',
        'units': 'ksi (MPa)',
        'notes': 'Perpendicular to fibers, ~40% of E_L',
        'test_standard': 'ASTM D3039',
    },
    'G_LT': {
        'name': 'In-Plane Shear Modulus',
        'typical_range': '300 - 600 ksi (2 - 4 GPa)',
        'typical_value': '400 ksi (2.8 GPa)',
        'units': 'ksi (MPa)',
        'notes': '~15% of E_L',
        'test_standard': 'ASTM D5379',
    },
    'nu_LT': {
        'name': "Poisson's Ratio",
        'typical_range': '0.25 - 0.35',
        'typical_value': '0.30',
        'units': 'dimensionless',
        'notes': 'Use 0.3 if not tested',
        'test_standard': 'ASTM D3039',
    },
    'F_Lt': {
        'name': 'Longitudinal Tensile Strength',
        'typical_range': '30 - 50 ksi (210 - 345 MPa)',
        'typical_value': '35 ksi (240 MPa)',
        'units': 'ksi (MPa)',
        'notes': 'Characteristic value, fiber-dominated',
        'test_standard': 'ASTM D3039, D6121',
    },
    'F_Tt': {
        'name': 'Transverse Tensile Strength',
        'typical_range': '5 - 10 ksi (35 - 70 MPa)',
        'typical_value': '7 ksi (48 MPa)',
        'units': 'ksi (MPa)',
        'notes': 'Much lower than F_Lt (5:1 to 8:1 ratio)',
        'test_standard': 'ASTM D3039, D6121',
    },
    'F_Lc': {
        'name': 'Longitudinal Compressive Strength',
        'typical_range': '20 - 40 ksi (140 - 275 MPa)',
        'typical_value': '25 ksi (170 MPa)',
        'units': 'ksi (MPa)',
        'notes': '60-80% of F_Lt',
        'test_standard': 'ASTM D3410 or D695, D6121',
    },
    'F_Tc': {
        'name': 'Transverse Compressive Strength',
        'typical_range': '10 - 20 ksi (70 - 140 MPa)',
        'typical_value': '15 ksi (100 MPa)',
        'units': 'ksi (MPa)',
        'notes': 'Often higher than F_Tt',
        'test_standard': 'ASTM D3410 or D695, D6121',
    },
    'F_LTs': {
        'name': 'In-Plane Shear Strength',
        'typical_range': '4 - 10 ksi (28 - 70 MPa)',
        'typical_value': '6 ksi (40 MPa)',
        'units': 'ksi (MPa)',
        'notes': 'Relatively low compared to metals',
        'test_standard': 'ASTM D5379, D6121',
    },
    'T_g': {
        'name': 'Glass Transition Temperature',
        'typical_range': '180 - 250°F (80 - 120°C)',
        'typical_value': '200°F (93°C)',
        'units': '°F (°C)',
        'notes': 'Critical threshold, service temp < T_g - 20°F',
        'test_standard': 'ASTM E1640',
    },
    'density': {
        'name': 'Density',
        'typical_range': '0.060 - 0.070 lb/in³',
        'typical_value': '0.065 lb/in³',
        'units': 'lb/in³ (g/cm³)',
        'notes': '~1/4 of steel density',
        'test_standard': 'ASTM D792',
    },
    'CTE': {
        'name': 'Coefficient of Thermal Expansion',
        'typical_range': '12 - 14 × 10⁻⁶ /°F',
        'typical_value': '13 × 10⁻⁶ /°F',
        'units': '10⁻⁶ /°F',
        'notes': '~2× steel, similar to aluminum',
        'test_standard': 'ASTM E831',
    },
}


def print_property(prop_name: str):
    """Print detailed information for a property."""
    if prop_name not in PROPERTIES:
        print(f"Property '{prop_name}' not found.")
        print(f"Available properties: {', '.join(PROPERTIES.keys())}")
        return

    prop = PROPERTIES[prop_name]
    print(f"\n{'=' * 80}")
    print(f"Property: {prop_name}")
    print(f"{'=' * 80}")
    print(f"Name:          {prop['name']}")
    print(f"Typical Range: {prop['typical_range']}")
    print(f"Typical Value: {prop['typical_value']} (for preliminary design)")
    print(f"Units:         {prop['units']}")
    print(f"Notes:         {prop['notes']}")
    print(f"Test Standard: {prop['test_standard']}")
    print(f"{'=' * 80}\n")


def print_all_properties():
    """Print summary of all properties."""
    print(f"\n{'=' * 100}")
    print("GFRP Material Properties - Typical Values Summary")
    print(f"{'=' * 100}\n")

    print(f"{'Property':<10} {'Name':<40} {'Typical Value':<30}")
    print("-" * 100)

    for prop_name, prop in PROPERTIES.items():
        print(f"{prop_name:<10} {prop['name']:<40} {prop['typical_value']:<30}")

    print(f"\n{'=' * 100}")
    print("WARNING: These are TYPICAL values for preliminary design only.")
    print("Final design MUST use manufacturer test data per ASTM D6121.")
    print("Characteristic values determined with 75% confidence, 20% exclusion.")
    print(f"{'=' * 100}\n")


def print_comparison():
    """Print comparison table with steel."""
    print(f"\n{'=' * 100}")
    print("GFRP vs Steel Material Property Comparison")
    print(f"{'=' * 100}\n")

    comparisons = [
        ("E (Modulus)", "2,500 ksi", "29,000 ksi", "1:12", "Deflection controls GFRP"),
        ("F_t (Tensile)", "35 ksi", "36-50 ksi", "Similar", "Good strength"),
        ("Density", "0.065 lb/in³", "0.284 lb/in³", "1:4.4", "Much lighter"),
        ("Strength/Weight", "538 ksi/(lb/in³)", "127-176 ksi/(lb/in³)", "3-4:1", "Excellent ratio"),
        ("Ductility", "None (brittle)", "High (ductile)", "-", "No yielding warning"),
        ("Directional", "Orthotropic (E_L≠E_T)", "Isotropic", "-", "L vs T different"),
        ("Time-dependent", "Yes (λ=0.60-1.00)", "No", "-", "Creep rupture"),
        ("Environmental", "Sensitive (C_M,C_T,C_CH)", "Minimal", "-", "Degradation"),
        ("T limit", "~200°F (T_g)", "~1000°F", "-", "Temperature limited"),
        ("CTE", "13×10⁻⁶/°F", "6.5×10⁻⁶/°F", "2:1", "Higher expansion"),
    ]

    print(f"{'Property':<20} {'GFRP':<25} {'Steel':<25} {'Ratio':<10} {'Notes'}")
    print("-" * 100)

    for prop, gfrp, steel, ratio, notes in comparisons:
        print(f"{prop:<20} {gfrp:<25} {steel:<25} {ratio:<10} {notes}")

    print(f"\n{'=' * 100}")
    print("Key Takeaways:")
    print("  • GFRP is much lighter but more flexible (E is 1/12 of steel)")
    print("  • GFRP is brittle (no yielding) vs steel ductile")
    print("  • GFRP is orthotropic (direction matters) vs steel isotropic")
    print("  • GFRP has time and environmental effects (λ, C_M, C_T, C_CH factors)")
    print(f"{'=' * 100}\n")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nAvailable properties:")
        for prop in PROPERTIES.keys():
            print(f"  - {prop}")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "--all":
        print_all_properties()
    elif arg == "--compare":
        print_comparison()
    elif arg.startswith("--property="):
        prop_name = arg.split("=")[1]
        print_property(prop_name)
    elif arg == "--property" and len(sys.argv) > 2:
        prop_name = sys.argv[2]
        print_property(prop_name)
    else:
        # Assume it's a property name
        print_property(arg)


if __name__ == "__main__":
    main()
