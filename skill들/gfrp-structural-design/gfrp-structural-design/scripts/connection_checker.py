#!/usr/bin/env python3
"""
GFRP Connection Design Checker - Multi-Mode Failure Analysis

Checks bolted connection capacity for all ASCE/SEI 74-23 Chapter 8 failure modes.

Usage:
    python3 connection_checker.py --P 10 --d 0.75 --t 0.5 --w 3 --e 2 --s 3
    python3 connection_checker.py --interactive
    python3 connection_checker.py --preset single-bolt --P 15
"""

import sys
import math
from typing import Dict, Tuple, List


# Preset connection geometries (typical configurations)
PRESETS = {
    'single-bolt': {
        'description': 'Single bolt connection (minimum geometry)',
        'd': 0.75,      # 3/4" bolt diameter (in)
        't': 0.5,       # 1/2" plate thickness (in)
        'w': 3.0,       # 3" width (4d minimum)
        'e': 2.25,      # 2.25" end distance (3d minimum)
        's': None,      # N/A for single bolt
        'n_rows': 1,
    },
    'double-shear': {
        'description': 'Double shear connection (2 bolts in line)',
        'd': 0.75,
        't': 0.5,
        'w': 3.0,
        'e': 2.25,
        's': 3.0,       # 3" spacing (4d typical)
        'n_rows': 2,
    },
    'multi-row': {
        'description': 'Multi-row connection (3 bolts)',
        'd': 0.875,     # 7/8" bolt
        't': 0.625,     # 5/8" plate
        'w': 4.0,
        'e': 3.0,
        's': 3.5,
        'n_rows': 3,
    },
}


# Typical GFRP material properties (conservative values)
DEFAULT_PROPERTIES = {
    'F_Lt': 35.0,       # Longitudinal tensile strength (ksi)
    'F_Tt': 7.0,        # Transverse tensile strength (ksi)
    'F_brg': 15.0,      # Bearing strength (ksi)
    'F_LTs': 6.0,       # In-plane shear strength (ksi)
    'E_L': 2500.0,      # Longitudinal modulus (ksi)
    'nu_LT': 0.30,      # Poisson's ratio
}


# Resistance factors (ASCE/SEI 74-23 Section 8.2)
RESISTANCE_FACTORS = {
    'bearing': 0.65,            # φ for bearing (Eq. 8.2-1)
    'net_tension': 0.50,        # φ for net tension (Eq. 8.2-2)
    'shear_out': 0.50,          # φ for shear-out (Eq. 8.2-3)
    'block_shear': 0.50,        # φ for block shear (Eq. 8.2-4)
    'pull_through': 0.65,       # φ for pull-through (Eq. 8.2-5)
    'bolt_shear': 0.75,         # φ for bolt shear (AISC)
}


def check_bearing(P: float, d: float, t: float, F_brg: float, phi: float = 0.65) -> Tuple[float, float, str]:
    """
    Check bearing capacity (ASCE/SEI 74-23 Eq. 8.2-1).

    P_n = C_bearing × d × t × F_brg
    where C_bearing = 2.0 for e/d ≥ 3

    Returns: (capacity, utilization, status)
    """
    C_bearing = 2.0  # Conservative (assumes e/d ≥ 3)
    P_n = C_bearing * d * t * F_brg
    phi_P_n = phi * P_n

    utilization = P / phi_P_n if phi_P_n > 0 else float('inf')
    status = 'OK' if utilization <= 1.0 else 'NG'

    return phi_P_n, utilization, status


def check_net_tension(P: float, d: float, t: float, w: float, F_Lt: float,
                     phi: float = 0.50) -> Tuple[float, float, str]:
    """
    Check net tension capacity (ASCE/SEI 74-23 Eq. 8.2-2).

    P_n = A_net × F_Lt
    A_net = (w - d_hole) × t
    d_hole = d + 1/8" (standard hole)

    Returns: (capacity, utilization, status)
    """
    d_hole = d + 0.125  # Standard hole size
    A_net = (w - d_hole) * t
    P_n = A_net * F_Lt
    phi_P_n = phi * P_n

    utilization = P / phi_P_n if phi_P_n > 0 else float('inf')
    status = 'OK' if utilization <= 1.0 else 'NG'

    return phi_P_n, utilization, status


def check_shear_out(P: float, d: float, t: float, e: float, F_LTs: float,
                   phi: float = 0.50) -> Tuple[float, float, str]:
    """
    Check shear-out capacity (ASCE/SEI 74-23 Eq. 8.2-3).

    P_n = 2 × e × t × F_LTs
    (two shear planes at end distance)

    Returns: (capacity, utilization, status)
    """
    P_n = 2.0 * e * t * F_LTs
    phi_P_n = phi * P_n

    utilization = P / phi_P_n if phi_P_n > 0 else float('inf')
    status = 'OK' if utilization <= 1.0 else 'NG'

    return phi_P_n, utilization, status


def check_block_shear(P: float, d: float, t: float, e: float, s: float,
                     n_rows: int, F_Lt: float, F_LTs: float,
                     phi: float = 0.50) -> Tuple[float, float, str]:
    """
    Check block shear capacity (ASCE/SEI 74-23 Eq. 8.2-4).

    P_n = A_nv × F_LTs + A_nt × F_Lt
    A_nv = net shear area
    A_nt = net tension area

    Returns: (capacity, utilization, status)
    """
    if n_rows < 2 or s is None:
        # Block shear not applicable for single bolt
        return float('inf'), 0.0, 'N/A'

    d_hole = d + 0.125

    # Shear area (two vertical planes)
    L_v = e + (n_rows - 1) * s  # Total shear length
    A_nv = 2.0 * (L_v - (n_rows - 0.5) * d_hole) * t

    # Tension area (one horizontal plane)
    # Simplified - assumes bolt spacing >> hole diameter
    A_nt = s * t

    P_n = A_nv * F_LTs + A_nt * F_Lt
    phi_P_n = phi * P_n

    utilization = P / phi_P_n if phi_P_n > 0 else float('inf')
    status = 'OK' if utilization <= 1.0 else 'NG'

    return phi_P_n, utilization, status


def check_pull_through(P: float, d: float, t: float, F_brg: float,
                       phi: float = 0.65) -> Tuple[float, float, str]:
    """
    Check pull-through capacity (ASCE/SEI 74-23 Eq. 8.2-5).

    P_n = C_pt × t² × F_brg
    C_pt depends on washer size (use 4.0 for standard washers)

    Returns: (capacity, utilization, status)
    """
    C_pt = 4.0  # Conservative (standard washer)
    P_n = C_pt * (t ** 2) * F_brg
    phi_P_n = phi * P_n

    utilization = P / phi_P_n if phi_P_n > 0 else float('inf')
    status = 'OK' if utilization <= 1.0 else 'NG'

    return phi_P_n, utilization, status


def check_bolt_shear(P: float, d: float, F_u_bolt: float = 120.0,
                    phi: float = 0.75) -> Tuple[float, float, str]:
    """
    Check bolt shear capacity (AISC steel bolt).

    P_n = 0.48 × A_bolt × F_u
    (assumes single shear, A325/A490 bolts)

    Returns: (capacity, utilization, status)
    """
    A_bolt = math.pi * (d ** 2) / 4.0
    P_n = 0.48 * A_bolt * F_u_bolt
    phi_P_n = phi * P_n

    utilization = P / phi_P_n if phi_P_n > 0 else float('inf')
    status = 'OK' if utilization <= 1.0 else 'NG'

    return phi_P_n, utilization, status


def check_geometry(d: float, e: float, w: float, s: float = None) -> List[str]:
    """
    Check geometric requirements (ASCE/SEI 74-23 Section 8.3).

    Minimum requirements:
    - e ≥ 3d (end distance)
    - w ≥ 4d (width)
    - s ≥ 4d (spacing, if applicable)

    Returns: list of warnings
    """
    warnings = []

    if e < 3.0 * d:
        warnings.append(f"⚠ End distance e={e:.2f}\" < 3d={3*d:.2f}\" (minimum required)")

    if w < 4.0 * d:
        warnings.append(f"⚠ Width w={w:.2f}\" < 4d={4*d:.2f}\" (minimum required)")

    if s is not None and s < 4.0 * d:
        warnings.append(f"⚠ Spacing s={s:.2f}\" < 4d={4*d:.2f}\" (recommended minimum)")

    return warnings


def print_results(P: float, geometry: Dict, properties: Dict, results: Dict):
    """Print formatted connection check results."""
    print("\n" + "=" * 80)
    print("GFRP Bolted Connection Design Check - ASCE/SEI 74-23 Chapter 8")
    print("=" * 80)

    print(f"\nApplied Load:          P = {P:.2f} kips")

    print("\nConnection Geometry:")
    print(f"  Bolt diameter:       d = {geometry['d']:.3f} in")
    print(f"  Plate thickness:     t = {geometry['t']:.3f} in")
    print(f"  Width:               w = {geometry['w']:.3f} in")
    print(f"  End distance:        e = {geometry['e']:.3f} in")
    if geometry['s'] is not None:
        print(f"  Bolt spacing:        s = {geometry['s']:.3f} in")
        print(f"  Number of rows:      n = {geometry['n_rows']}")

    print("\nMaterial Properties:")
    print(f"  F_Lt (tensile):      {properties['F_Lt']:.1f} ksi")
    print(f"  F_brg (bearing):     {properties['F_brg']:.1f} ksi")
    print(f"  F_LTs (shear):       {properties['F_LTs']:.1f} ksi")

    # Check geometry
    warnings = check_geometry(geometry['d'], geometry['e'], geometry['w'], geometry['s'])
    if warnings:
        print("\nGeometry Warnings:")
        for warning in warnings:
            print(f"  {warning}")

    print("\n" + "-" * 80)
    print(f"{'Failure Mode':<25} {'φP_n (kips)':<15} {'P/φP_n':<12} {'Status':<10} φ")
    print("-" * 80)

    for mode, data in results.items():
        if data['status'] != 'N/A':
            print(f"{mode:<25} {data['capacity']:>10.2f}     {data['utilization']:>8.3f}    "
                  f"{data['status']:<10} {data['phi']:.2f}")
        else:
            print(f"{mode:<25} {'N/A':>10}     {'---':>8}    {data['status']:<10} ---")

    print("-" * 80)

    # Find controlling mode
    valid_modes = {k: v for k, v in results.items() if v['status'] != 'N/A'}
    if valid_modes:
        controlling = min(valid_modes.items(), key=lambda x: x[1]['capacity'])
        print(f"\n▶ Controlling Mode:    {controlling[0]}")
        print(f"▶ Design Capacity:     φP_n = {controlling[1]['capacity']:.2f} kips")
        print(f"▶ Max Utilization:     {controlling[1]['utilization']:.3f}")

        if controlling[1]['status'] == 'OK':
            print(f"▶ Overall Status:      ✓ PASS (P ≤ φP_n)")
        else:
            print(f"▶ Overall Status:      ✗ FAIL (P > φP_n)")
            print(f"\n  Recommendation: Increase geometry, use larger bolt, or reduce load")

    print("\n" + "=" * 80)
    print("Notes:")
    print("  • All calculations per ASCE/SEI 74-23 Chapter 8")
    print("  • Resistance factors (φ) from Section 8.2")
    print("  • Use manufacturer-tested F_brg values when available")
    print("  • Check additional modes for specific configurations")
    print("=" * 80 + "\n")


def interactive_mode():
    """Interactive connection checker."""
    print("\n" + "=" * 80)
    print("GFRP Connection Checker - Interactive Mode")
    print("=" * 80 + "\n")

    # Get applied load
    while True:
        try:
            P = float(input("Enter applied load P (kips): "))
            if P > 0:
                break
            print("Load must be positive!")
        except ValueError:
            print("Please enter a number.")

    # Get geometry
    print("\nConnection Geometry:")
    while True:
        try:
            d = float(input("  Bolt diameter d (in): "))
            if d > 0:
                break
            print("  Diameter must be positive!")
        except ValueError:
            print("  Please enter a number.")

    while True:
        try:
            t = float(input("  Plate thickness t (in): "))
            if t > 0:
                break
            print("  Thickness must be positive!")
        except ValueError:
            print("  Please enter a number.")

    while True:
        try:
            w = float(input("  Width w (in): "))
            if w > 0:
                break
            print("  Width must be positive!")
        except ValueError:
            print("  Please enter a number.")

    while True:
        try:
            e = float(input("  End distance e (in): "))
            if e > 0:
                break
            print("  End distance must be positive!")
        except ValueError:
            print("  Please enter a number.")

    # Optional spacing for multi-bolt
    s_input = input("  Bolt spacing s (in, Enter to skip): ")
    s = float(s_input) if s_input.strip() else None

    n_rows = 1
    if s is not None:
        while True:
            try:
                n_rows = int(input("  Number of bolt rows: "))
                if n_rows >= 2:
                    break
                print("  Must be ≥ 2 for multi-row!")
            except ValueError:
                print("  Please enter an integer.")

    # Get material properties (use defaults or custom)
    use_default = input("\nUse default GFRP properties? (Y/n): ").strip().lower() != 'n'

    if use_default:
        properties = DEFAULT_PROPERTIES.copy()
    else:
        properties = {}
        properties['F_Lt'] = float(input("  F_Lt (tensile strength, ksi): "))
        properties['F_brg'] = float(input("  F_brg (bearing strength, ksi): "))
        properties['F_LTs'] = float(input("  F_LTs (shear strength, ksi): "))

    # Run checks
    geometry = {'d': d, 't': t, 'w': w, 'e': e, 's': s, 'n_rows': n_rows}
    results = run_all_checks(P, geometry, properties)

    print_results(P, geometry, properties, results)


def run_all_checks(P: float, geometry: Dict, properties: Dict) -> Dict:
    """Run all connection checks and return results."""
    results = {}

    # 1. Bearing
    cap, util, status = check_bearing(P, geometry['d'], geometry['t'],
                                      properties['F_brg'])
    results['Bearing'] = {
        'capacity': cap, 'utilization': util, 'status': status,
        'phi': RESISTANCE_FACTORS['bearing']
    }

    # 2. Net tension
    cap, util, status = check_net_tension(P, geometry['d'], geometry['t'],
                                         geometry['w'], properties['F_Lt'])
    results['Net Tension'] = {
        'capacity': cap, 'utilization': util, 'status': status,
        'phi': RESISTANCE_FACTORS['net_tension']
    }

    # 3. Shear-out
    cap, util, status = check_shear_out(P, geometry['d'], geometry['t'],
                                       geometry['e'], properties['F_LTs'])
    results['Shear-out'] = {
        'capacity': cap, 'utilization': util, 'status': status,
        'phi': RESISTANCE_FACTORS['shear_out']
    }

    # 4. Block shear (multi-bolt only)
    cap, util, status = check_block_shear(P, geometry['d'], geometry['t'],
                                         geometry['e'], geometry['s'],
                                         geometry['n_rows'], properties['F_Lt'],
                                         properties['F_LTs'])
    results['Block Shear'] = {
        'capacity': cap, 'utilization': util, 'status': status,
        'phi': RESISTANCE_FACTORS['block_shear']
    }

    # 5. Pull-through
    cap, util, status = check_pull_through(P, geometry['d'], geometry['t'],
                                          properties['F_brg'])
    results['Pull-through'] = {
        'capacity': cap, 'utilization': util, 'status': status,
        'phi': RESISTANCE_FACTORS['pull_through']
    }

    # 6. Bolt shear (steel bolt)
    cap, util, status = check_bolt_shear(P, geometry['d'])
    results['Bolt Shear'] = {
        'capacity': cap, 'utilization': util, 'status': status,
        'phi': RESISTANCE_FACTORS['bolt_shear']
    }

    return results


def preset_mode(preset_name: str, P: float):
    """Use preset connection configuration."""
    if preset_name not in PRESETS:
        print(f"Preset '{preset_name}' not found.")
        print("\nAvailable presets:")
        for name, data in PRESETS.items():
            print(f"  {name:<20} - {data['description']}")
        sys.exit(1)

    preset = PRESETS[preset_name]
    geometry = {
        'd': preset['d'],
        't': preset['t'],
        'w': preset['w'],
        'e': preset['e'],
        's': preset['s'],
        'n_rows': preset['n_rows'],
    }

    properties = DEFAULT_PROPERTIES.copy()

    print(f"\nUsing preset: {preset_name}")
    print(f"Description: {preset['description']}\n")

    results = run_all_checks(P, geometry, properties)
    print_results(P, geometry, properties, results)


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
            print("Usage: --preset <preset_name> --P <load>")
            sys.exit(1)

        preset_name = sys.argv[2]
        P = None

        for i, arg in enumerate(sys.argv[3:], 3):
            if arg == "--P" and i + 1 < len(sys.argv):
                P = float(sys.argv[i + 1])

        if P is None:
            print("Error: --P is required with --preset")
            sys.exit(1)

        preset_mode(preset_name, P)
        return

    # Parse command line arguments
    P = None
    d = None
    t = None
    w = None
    e = None
    s = None
    n_rows = 1

    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--P" and i + 1 < len(sys.argv):
            P = float(sys.argv[i + 1])
        elif arg == "--d" and i + 1 < len(sys.argv):
            d = float(sys.argv[i + 1])
        elif arg == "--t" and i + 1 < len(sys.argv):
            t = float(sys.argv[i + 1])
        elif arg == "--w" and i + 1 < len(sys.argv):
            w = float(sys.argv[i + 1])
        elif arg == "--e" and i + 1 < len(sys.argv):
            e = float(sys.argv[i + 1])
        elif arg == "--s" and i + 1 < len(sys.argv):
            s = float(sys.argv[i + 1])
        elif arg == "--n" and i + 1 < len(sys.argv):
            n_rows = int(sys.argv[i + 1])

    if None in [P, d, t, w, e]:
        print("Error: Required parameters missing")
        print("Required: --P --d --t --w --e")
        print("Optional: --s --n")
        print(__doc__)
        sys.exit(1)

    geometry = {'d': d, 't': t, 'w': w, 'e': e, 's': s, 'n_rows': n_rows}
    properties = DEFAULT_PROPERTIES.copy()

    results = run_all_checks(P, geometry, properties)
    print_results(P, geometry, properties, results)


if __name__ == "__main__":
    main()
