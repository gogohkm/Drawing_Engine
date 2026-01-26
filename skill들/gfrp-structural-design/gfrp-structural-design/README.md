# GFRP Structural Design Skill

Claude Code skill for GFRP (Glass Fiber Reinforced Polymer) structural design based on ASCE/SEI 74-23.

## Overview

This skill provides comprehensive support for pultruded GFRP structural member design, including:
- ASCE/SEI 74-23 specification search and navigation
- Material property lookup and environmental adjustments
- Time effect factor calculations
- Connection design verification
- Formula extraction and cross-referencing

## Structure

```
gfrp-structural-design/
├── SKILL.md                    # Main skill definition
├── README.md                   # This file
├── data/specification/         # ASCE/SEI 74-23 documents (5 files, 433KB)
├── references/                 # Quick reference guides (8 files)
│   ├── symbols.md              # 150+ variable definitions
│   ├── glossary.md             # 50+ technical terms
│   ├── material-properties-guide.md
│   ├── environmental-factors.md
│   ├── resistance-factors.md
│   ├── time-effect-factors.md
│   ├── chapter-structure.md
│   └── abbreviations.md
└── scripts/                    # Python automation tools (5 scripts)
    ├── smart_search.py         # Category-aware keyword search
    ├── formula_finder.py       # Formula extraction with context
    ├── material_lookup.py      # Property lookup and comparison
    ├── environmental_adjustment.py  # Environmental factor calculator
    └── connection_checker.py   # Multi-mode connection design

```

## Quick Start

### Using the Skill in Claude Code

The skill activates with keywords like:
- "GFRP design", "FRP structural", "pultruded GFRP"
- "lateral-torsional buckling", "connection design"
- "environmental factors", "time effect factor"
- Korean: "GFRP 설계", "섬유강화폴리머", "연결부 설계"

### Using Python Scripts

**Material Property Lookup:**
```bash
cd scripts/
python3 material_lookup.py --all              # All properties summary
python3 material_lookup.py E_L                # Specific property
python3 material_lookup.py --compare          # GFRP vs Steel comparison
```

**Environmental Adjustment:**
```bash
python3 environmental_adjustment.py --preset wet-hot --F_ref 35
python3 environmental_adjustment.py --interactive
python3 environmental_adjustment.py --F_ref 35 --C_M 0.85 --C_T 0.90
```

**Connection Design Check:**
```bash
python3 connection_checker.py --preset single-bolt --P 10
python3 connection_checker.py --interactive
python3 connection_checker.py --P 10 --d 0.75 --t 0.5 --w 3 --e 2 --s 3
```

**Smart Search:**
```bash
python3 smart_search.py "lateral-torsional buckling"
python3 smart_search.py "연결부 설계" --verbose
```

**Formula Finder:**
```bash
python3 formula_finder.py "M_n"
python3 formula_finder.py "λ" --chapter 2
python3 formula_finder.py "F_cre" --context 5
```

## Key GFRP Design Concepts

### 1. Orthotropic Behavior
- E_L (longitudinal) ≠ E_T (transverse)
- Typical ratio: E_L/E_T ≈ 2.5:1
- Fiber direction matters significantly

### 2. Time Effect Factor (λ)
- Accounts for creep rupture under sustained load
- Range: 0.60 (permanent) to 1.00 (10-minute duration)
- Applied to strength calculations: F_adj = λ × F_ref

### 3. Environmental Factors
- C_M (moisture): 0.70-1.00
- C_T (temperature): 0.75-1.00
- C_CH (chemical): 0.60-1.00
- Combined: F_adj = F_ref × C_M × C_T × C_CH

### 4. Resistance Factors (φ)
- Lower than steel due to variability
- Tension: φ = 0.85
- Compression: φ = 0.70-0.80
- Connection (net tension): φ = 0.50 (critical!)

### 5. Connection Design
- Must check 6+ failure modes:
  1. Bearing
  2. Net tension
  3. Shear-out
  4. Block shear
  5. Pull-through
  6. Bolt shear
- Controlling mode determines capacity

## Material Testing Requirements

All design values must come from manufacturer testing per:
- **ASTM D6121**: Statistical basis (75% confidence, 20% exclusion)
- **ASTM D7290**: Minimum test program requirements
- **ASTM D3039**: Tension testing
- **ASTM D3410**: Compression testing
- **ASTM D5379**: Shear testing

**Do NOT use handbook values for final design!**

## ASCE/SEI 74-23 Chapter Guide

| Chapter | Topic | Key Sections |
|---------|-------|--------------|
| 1 | General Provisions | Scope, Materials, Definitions |
| 2 | Design Requirements | LRFD, λ, φ, Environmental |
| 3 | Tension Members | Gross/Net Section, Threaded Rods |
| 4 | Compression Members | Flexural/Local/Torsional Buckling |
| 5 | Flexural Members | LTB, Shear, Web Buckling |
| 6 | Combined Forces | Beam-Columns, Interaction |
| 7 | Plates | In-plane Loading, Open-hole |
| 8 | Connections | Bolted Connections (6 modes) |
| 9 | Seismic | Braced Frames, R-factors |

## Typical GFRP Properties (Preliminary Design Only)

| Property | Typical Value | Units |
|----------|---------------|-------|
| E_L | 2,500 | ksi |
| E_T | 1,000 | ksi |
| F_Lt | 35 | ksi |
| F_Lc | 25 | ksi |
| F_LTs | 6 | ksi |
| T_g | 200 | °F |
| Density | 0.065 | lb/in³ |

## Common Workflows

### 1. Tension Member Design
```
1. Calculate required area: A_req = P_u / (φ × λ × F_Lt × C_M × C_T × C_CH)
2. Check net section at holes
3. Verify connection (6 modes)
4. Check serviceability (deflection)
```

### 2. Compression Member Design
```
1. Determine effective length (K × L)
2. Check flexural buckling (λ_c)
3. Check local buckling (λ_local)
4. Check torsional buckling (if applicable)
5. Apply φ = 0.70-0.80 depending on mode
```

### 3. Beam Design
```
1. Check flexural strength (local buckling vs LTB)
2. Check shear strength (web buckling)
3. Check concentrated loads (web crippling)
4. Verify deflection (L/180 to L/240 typical)
```

### 4. Connection Design
```
1. Run all 6 failure mode checks
2. Identify controlling mode (minimum capacity)
3. Verify geometry requirements (3d, 4d minimums)
4. Check for combined loading if applicable
```

## Important Notes

- **Brittle Material**: No yielding before failure (no ductility)
- **Temperature Limit**: T_service < T_g - 20°F (critical!)
- **Statistical Basis**: All properties are characteristic values
- **Testing Required**: Manufacturer data per ASTM D6121 mandatory
- **Lower φ Factors**: Especially for connections (φ = 0.50 for net tension)
- **Time Matters**: Permanent loads see 40% strength reduction (λ = 0.60)
- **Environment Matters**: Combined reductions can exceed 50%

## Support

For questions or issues:
1. Check SKILL.md for detailed workflows
2. Review reference guides in `references/`
3. Consult ASCE/SEI 74-23 specification files in `data/specification/`
4. Use Python scripts for quick calculations

---

**Standard:** ASCE/SEI 74-23 (Pultruded GFRP Structures)  
**Created:** 2025-11  
**Language Support:** English / Korean (한국어)
