#!/usr/bin/env python3
"""
GFRP Environmental Adjustment Calculator

Calculate adjusted material properties based on environmental factors.

Usage:
    python3 environmental_adjustment.py --F_ref 35 --C_M 0.85 --C_T 0.90 --C_CH 1.00
    python3 environmental_adjustment.py --preset wet-hot
    python3 environmental_adjustment.py --interactive
"""

import sys
from typing import Dict, Tuple


# Preset environmental conditions
PRESETS = {
    'dry-normal': {
        'C_M': 1.00,
        'C_T': 1.00,
        'C_CH': 1.00,
        'description': 'Dry, room temperature, no chemicals',
    },
    'wet-normal': {
        'C_M': 0.85,
        'C_T': 1.00,
        'C_CH': 1.00,
        'description': 'Wet service, room temperature',
    },
    'wet-hot': {
        'C_M': 0.80,
        'C_T': 0.85,
        'C_CH': 1.00,
        'description': 'Wet service, 140°F sustained',
    },
    'immersed-hot': {
        'C_M': 0.75,
        'C_T': 0.80,
        'C_CH': 1.00,
        'description': 'Continuous immersion, 160°F sustained',
    },
    'wet-hot-acid': {
        'C_M': 0.80,
        'C_T': 0.85,
        'C_CH': 0.90,
        'description': 'Wet service, 140°F, mild acid exposure',
    },
    'severe': {
        'C_M': 0.70,
        'C_T': 0.75,
        'C_CH': 0.80,
        'description': 'Immersed, 180°F, moderate acid',
    },
}


def calculate_adjustment(F_ref: float, C_M: float = 1.0, C_T: float = 1.0,
                        C_CH: float = 1.0, C_CA: float = 1.0, C_LS: float = 1.0) -> Tuple[float, float]:
    """
    Calculate adjusted strength.

    Returns: (adjusted_strength, reduction_percentage)
    """
    F_adj = F_ref * C_M * C_T * C_CH * C_CA * C_LS
    reduction = (1 - F_adj / F_ref) * 100

    return F_adj, reduction


def print_adjustment_result(F_ref: float, factors: Dict, F_adj: float, reduction: float):
    """Print formatted adjustment results."""
    print("\n" + "=" * 80)
    print("GFRP Environmental Adjustment Calculation")
    print("=" * 80)
    print(f"\nReference Strength:        F_ref = {F_ref:.1f} ksi")
    print("\nEnvironmental Factors:")
    print(f"  Moisture factor (C_M):      {factors.get('C_M', 1.0):.2f}")
    print(f"  Temperature factor (C_T):   {factors.get('C_T', 1.0):.2f}")
    print(f"  Chemical factor (C_CH):     {factors.get('C_CH', 1.0):.2f}")
    print(f"  Composite action (C_CA):    {factors.get('C_CA', 1.0):.2f}")
    print(f"  Load sharing (C_LS):        {factors.get('C_LS', 1.0):.2f}")

    combined_factor = (factors.get('C_M', 1.0) * factors.get('C_T', 1.0) *
                       factors.get('C_CH', 1.0) * factors.get('C_CA', 1.0) *
                       factors.get('C_LS', 1.0))

    print(f"\nCombined Factor:           {combined_factor:.3f}")
    print("\nFormula:")
    print("  F_adjusted = F_ref × C_M × C_T × C_CH × C_CA × C_LS")
    print(f"  F_adjusted = {F_ref:.1f} × {factors.get('C_M', 1.0):.2f} × {factors.get('C_T', 1.0):.2f} × {factors.get('C_CH', 1.0):.2f} × {factors.get('C_CA', 1.0):.2f} × {factors.get('C_LS', 1.0):.2f}")

    print(f"\n{'▶ Adjusted Strength:':<30} F_adj = {F_adj:.1f} ksi")
    print(f"{'▶ Reduction from Reference:':<30} {reduction:.1f}%")

    print("\n" + "=" * 80)

    # Warnings
    if reduction > 40:
        print("⚠ WARNING: Severe reduction (>40%)! Consider:")
        print("  - Increasing section size")
        print("  - Changing resin system (vinyl ester or epoxy)")
        print("  - Providing environmental protection")
        print("  - Conducting project-specific testing")
    elif reduction > 25:
        print("⚠ CAUTION: Significant reduction (>25%). Verify:")
        print("  - Environmental factors are appropriate")
        print("  - T_service < T_g - 20°F")
        print("  - Chemical compatibility with resin")

    print("=" * 80 + "\n")


def interactive_mode():
    """Interactive calculator mode."""
    print("\n" + "=" * 80)
    print("GFRP Environmental Adjustment - Interactive Mode")
    print("=" * 80 + "\n")

    # Get reference strength
    while True:
        try:
            F_ref = float(input("Enter reference strength F_ref (ksi): "))
            if F_ref > 0:
                break
            print("Strength must be positive!")
        except ValueError:
            print("Please enter a number.")

    print("\nEnvironmental Conditions:")
    print("-" * 80)

    # Moisture
    print("\nMoisture Exposure:")
    print("  1. Dry (indoor, climate-controlled)      C_M = 1.00")
    print("  2. Humid (high humidity, unconditioned)  C_M = 0.85-0.90")
    print("  3. Wet (frequent water contact)          C_M = 0.75-0.85")
    print("  4. Immersed (continuous submersion)      C_M = 0.70-0.80")

    while True:
        choice = input("Select (1-4) or enter custom C_M: ")
        if choice == '1':
            C_M = 1.00
            break
        elif choice == '2':
            C_M = 0.87
            break
        elif choice == '3':
            C_M = 0.80
            break
        elif choice == '4':
            C_M = 0.75
            break
        else:
            try:
                C_M = float(choice)
                if 0.5 <= C_M <= 1.0:
                    break
                print("C_M should be between 0.5 and 1.0")
            except ValueError:
                print("Invalid input")

    # Temperature
    print("\nTemperature Exposure:")
    print("  1. < 100°F (normal)                     C_T = 1.00")
    print("  2. 100-120°F (mild elevation)           C_T = 0.95")
    print("  3. 120-150°F (moderate elevation)       C_T = 0.85-0.95")
    print("  4. 150-180°F (high, near T_g)           C_T = 0.75-0.85")

    while True:
        choice = input("Select (1-4) or enter custom C_T: ")
        if choice == '1':
            C_T = 1.00
            break
        elif choice == '2':
            C_T = 0.95
            break
        elif choice == '3':
            C_T = 0.90
            break
        elif choice == '4':
            C_T = 0.80
            break
        else:
            try:
                C_T = float(choice)
                if 0.5 <= C_T <= 1.0:
                    break
                print("C_T should be between 0.5 and 1.0")
            except ValueError:
                print("Invalid input")

    # Chemical
    print("\nChemical Exposure:")
    print("  1. None (air, water only)               C_CH = 1.00")
    print("  2. Mild (weak acids/alkalis)            C_CH = 0.90-0.95")
    print("  3. Moderate (pH 3-4 or 10-12)           C_CH = 0.80-0.90")
    print("  4. Severe (strong acids/alkalis)        C_CH = 0.60-0.80")

    while True:
        choice = input("Select (1-4) or enter custom C_CH: ")
        if choice == '1':
            C_CH = 1.00
            break
        elif choice == '2':
            C_CH = 0.92
            break
        elif choice == '3':
            C_CH = 0.85
            break
        elif choice == '4':
            C_CH = 0.70
            break
        else:
            try:
                C_CH = float(choice)
                if 0.5 <= C_CH <= 1.0:
                    break
                print("C_CH should be between 0.5 and 1.0")
            except ValueError:
                print("Invalid input")

    # Calculate
    factors = {'C_M': C_M, 'C_T': C_T, 'C_CH': C_CH, 'C_CA': 1.0, 'C_LS': 1.0}
    F_adj, reduction = calculate_adjustment(F_ref, C_M, C_T, C_CH)

    print_adjustment_result(F_ref, factors, F_adj, reduction)


def preset_mode(preset_name: str, F_ref: float = 35.0):
    """Use preset environmental condition."""
    if preset_name not in PRESETS:
        print(f"Preset '{preset_name}' not found.")
        print("\nAvailable presets:")
        for name, data in PRESETS.items():
            print(f"  {name:<20} - {data['description']}")
        sys.exit(1)

    preset = PRESETS[preset_name]
    factors = {
        'C_M': preset['C_M'],
        'C_T': preset['C_T'],
        'C_CH': preset['C_CH'],
        'C_CA': 1.0,
        'C_LS': 1.0,
    }

    F_adj, reduction = calculate_adjustment(F_ref, **factors)

    print(f"\nUsing preset: {preset_name}")
    print(f"Description: {preset['description']}\n")

    print_adjustment_result(F_ref, factors, F_adj, reduction)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nAvailable presets:")
        for name, data in PRESETS.items():
            print(f"  {name:<20} - {data['description']}")
        sys.exit(1)

    if sys.argv[1] == "--interactive" or sys.argv[1] == "-i":
        interactive_mode()
        return

    if sys.argv[1] == "--preset":
        if len(sys.argv) < 3:
            print("Usage: --preset <preset_name> [--F_ref <value>]")
            sys.exit(1)

        preset_name = sys.argv[2]
        F_ref = 35.0  # Default

        for i, arg in enumerate(sys.argv[3:], 3):
            if arg == "--F_ref" and i + 1 < len(sys.argv):
                F_ref = float(sys.argv[i + 1])

        preset_mode(preset_name, F_ref)
        return

    # Parse command line arguments
    F_ref = None
    C_M = 1.0
    C_T = 1.0
    C_CH = 1.0
    C_CA = 1.0
    C_LS = 1.0

    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--F_ref" and i + 1 < len(sys.argv):
            F_ref = float(sys.argv[i + 1])
        elif arg == "--C_M" and i + 1 < len(sys.argv):
            C_M = float(sys.argv[i + 1])
        elif arg == "--C_T" and i + 1 < len(sys.argv):
            C_T = float(sys.argv[i + 1])
        elif arg == "--C_CH" and i + 1 < len(sys.argv):
            C_CH = float(sys.argv[i + 1])
        elif arg == "--C_CA" and i + 1 < len(sys.argv):
            C_CA = float(sys.argv[i + 1])
        elif arg == "--C_LS" and i + 1 < len(sys.argv):
            C_LS = float(sys.argv[i + 1])

    if F_ref is None:
        print("Error: --F_ref is required")
        print(__doc__)
        sys.exit(1)

    factors = {'C_M': C_M, 'C_T': C_T, 'C_CH': C_CH, 'C_CA': C_CA, 'C_LS': C_LS}
    F_adj, reduction = calculate_adjustment(F_ref, C_M, C_T, C_CH, C_CA, C_LS)

    print_adjustment_result(F_ref, factors, F_adj, reduction)


if __name__ == "__main__":
    main()
