import math

def calculate_h_beam_capacity():
    # 1. Section Dimensions (H588x300x12x20)
    d = 588  # mm
    bf = 300 # mm
    tw = 12  # mm
    tf = 20  # mm
    L_total = 20000 # mm
    Lb = 12000 # mm (distance between top lug points, assuming unbraced)
    
    # Material Properties (SS275)
    Fy = 275 # MPa (N/mm^2)
    E = 200000 # MPa
    G = 77200 # MPa
    
    # 2. Section Properties calculation
    # Area
    Af = bf * tf
    Aw = (d - 2*tf) * tw
    Ag = 2*Af + Aw
    
    # Moment of Inertia (x-axis)
    Ix = (bf * d**3 / 12) - ((bf - tw) * (d - 2*tf)**3 / 12)
    Sx = Ix / (d/2)
    
    # Plastic Section Modulus (x-axis)
    # Zx = sum of (Area_i * y_i)
    # Flanges: 2 * (bf * tf) * (d/2 - tf/2)
    # Web: 2 * (tw * (d/2 - tf)**2 / 2)
    Zx = 2 * (bf * tf * (d - tf)/2) + (tw * (d - 2*tf)**2 / 4)
    
    # Radius of gyration (y-axis)
    Iy = (2 * tf * bf**3 / 12) + ((d - 2*tf) * tw**3 / 12)
    ry = math.sqrt(Iy / Ag)
    
    # Torsional constant (approximate for I-shape)
    # J = sum(b * t^3 / 3)
    J = (2 * bf * tf**3 + (d - 2*tf) * tw**3) / 3
    
    # Warping constant (Cw)
    ho = d - tf # distance between flange centroids
    Cw = Iy * ho**2 / 4
    
    # rts (Sect F2.2)
    rts = math.sqrt(math.sqrt(Iy * Cw) / Sx) # simplified approx
    
    # 3. AISC Chapter B: Slenderness Check (Table B4.1b)
    # Flange slenderness
    lambda_f = bf / (2 * tf)
    lambda_pf = 0.38 * math.sqrt(E / Fy)
    lambda_rf = 1.0 * math.sqrt(E / Fy)
    
    # Web slenderness
    h = d - 2*tf # clear distance between flanges
    lambda_w = h / tw
    lambda_pw = 3.76 * math.sqrt(E / Fy)
    lambda_rw = 5.70 * math.sqrt(E / Fy)
    
    is_compact_flange = lambda_f <= lambda_pf
    is_compact_web = lambda_w <= lambda_pw
    
    print(f"--- Section Properties ---")
    print(f"Ix: {Ix:,.0f} mm^4")
    print(f"Sx: {Sx:,.0f} mm^3")
    print(f"Zx: {Zx:,.0f} mm^3")
    print(f"Iy: {Iy:,.0f} mm^4")
    print(f"ry: {ry:,.2f} mm")
    print(f"J: {J:,.0f} mm^4")
    print(f"Cw: {Cw:,.0e} mm^6")
    print(f"\n--- Slenderness Check ---")
    print(f"Flange: lambda={lambda_f:.2f}, pf={lambda_pf:.2f} -> {'Compact' if is_compact_flange else 'Non-compact'}")
    print(f"Web: lambda={lambda_w:.2f}, pw={lambda_pw:.2f} -> {'Compact' if is_compact_web else 'Non-compact'}")
    
    # 4. AISC Chapter F: Flexural Strength (Mn)
    # Limit State: Yielding (Plastic Moment)
    Mp = Fy * Zx
    
    # Limit State: Lateral-Torsional Buckling (LTB)
    # Lp (F2-5)
    Lp = 1.76 * ry * math.sqrt(E / Fy)
    
    # Lr (F2-6)
    # c = 1 for doubly symmetric I-shape
    c = 1.0
    term1 = (J * c) / (Sx * ho)
    term2 = 6.76 * (0.7 * Fy / E)**2
    Lr = 1.95 * rts * (E / (0.7 * Fy)) * math.sqrt(term1 + math.sqrt(term1**2 + term2))
    
    Cb = 1.0 # Conservative
    
    if Lb <= Lp:
        Mn_ltb = Mp
        limit_state = "Yielding"
    elif Lb <= Lr:
        Mn_ltb = Cb * (Mp - (Mp - 0.7 * Fy * Sx) * (Lb - Lp) / (Lr - Lp))
        Mn_ltb = min(Mn_ltb, Mp)
        limit_state = "Inelastic LTB"
    else:
        Fcr = (Cb * math.pi**2 * E / (Lb / rts)**2) * math.sqrt(1 + 0.078 * (J * c / (Sx * ho)) * (Lb / rts)**2)
        Mn_ltb = Fcr * Sx
        Mn_ltb = min(Mn_ltb, Mp)
        limit_state = "Elastic LTB"
        
    Mn = Mn_ltb # Since it's compact or non-compact, yielding/LTB controls.
    
    # 5. AISC Chapter G: Shear Strength (Vn)
    # Vn = 0.6 * Fy * Aw * Cv1
    Aw_shear = d * tw
    Cv1 = 1.0 # Typical for d/tw <= 2.24*sqrt(E/Fy)
    if lambda_w <= 2.24 * math.sqrt(E / Fy):
        Cv1 = 1.0
    Vn = 0.6 * Fy * Aw_shear * Cv1
    
    print(f"\n--- AISC Strength (LRFD) ---")
    phi_b = 0.9
    phi_v = 1.0 # For Cv1 = 1.0
    
    Available_Mn = phi_b * Mn / 1e6 # kNm
    Available_Vn = phi_v * Vn / 1000 # kN
    
    print(f"Limit State: {limit_state}")
    print(f"Nominal Mn: {Mn / 1e6:,.2f} kNm")
    print(f"Available Mn (phi=0.9): {Available_Mn:,.2f} kNm")
    print(f"Available Vn (phi=1.0): {Available_Vn:,.2f} kN")
    
    # 6. Load Capacity Approximation
    # Max Moment for simply supported beam with Span L and load P at center: M = P*L/4
    # P_allowed = 4 * Mn / L
    # Here, L_total = 20m. Assuming lifting lug points are supports?
    # Actually, lifting lugs are at 4m - 12m - 4m.
    # If lifting from top 2 points (12m apart), and hanging load from 4 bottom points:
    # Max moment will happen at the center of the 12m span.
    # P_total_allowed = 8 * Available_Mn / (12) # very simplified
    
    print(f"\n--- Load Capacity (Theoretical) ---")
    print(f"Estimated Max Total Load based on Flexure (12m span): {8 * Available_Mn / 12:,.2f} kN")
    print(f"Estimated Max Total Load (Metric Tons): {8 * Available_Mn / 12 / 9.81:,.2f} Tons")

calculate_h_beam_capacity()
