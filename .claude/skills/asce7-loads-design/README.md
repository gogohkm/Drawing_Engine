# ASCE 7-22 Loads and Design Skill

**Version:** 1.0
**Last Updated:** 2025-11-14
**Standard:** ASCE 7-22 (2022 Edition)

## Overview

This skill provides comprehensive access to ASCE 7-22, the authoritative US standard for determining structural loads on buildings and other structures.

**What this skill covers:**
- Load combinations (LRFD and ASD)
- Wind loads and wind design
- Seismic loads and seismic design criteria
- Snow loads, rain loads, ice loads
- Flood and tsunami loads
- Risk categories and building classification

**What this skill does NOT cover:**
- Member design (use AISC 360 for steel, ACI 318 for concrete)
- Connection design
- Material properties

## Quick Start

### For Claude Code Users

This skill automatically activates when you ask about:
- "ASCE 7 load combinations"
- "Wind load calculation"
- "Seismic base shear"
- "Snow load on roof"
- "LRFD vs ASD"

### Available Chapters

**Complete ASCE 7-22 Coverage - 30 Chapters:**

**General & Basic Loads (Ch 1-5):**
- Chapter 1: General (31 KB)
- Chapter 2: Combinations of Loads (16 KB)
- Chapter 3: Dead Loads, Soil Loads, Hydrostatic Pressure (8 KB)
- Chapter 4: Live Loads (26 KB)
- Chapter 5: Flood Loads (10 KB)

**Environmental Loads (Ch 6-10):**
- Chapter 6: Tsunami Loads and Effects (98 KB)
- Chapter 7: Snow Loads (24 KB)
- Chapter 10: Ice Loads - Atmospheric Icing (12 KB)

**Seismic Design (Ch 11-23):**
- Chapter 11: Seismic Design Criteria (64 KB)
- Chapter 12: Seismic Design Requirements - Buildings (177 KB)
- Chapter 13: Seismic Requirements - Nonstructural (84 KB)
- Chapter 14: Material-Specific Seismic Design (11 KB)
- Chapter 15: Seismic Requirements - Nonbuilding (43 KB)
- Chapter 16: Nonlinear Response History Analysis (23 KB)
- Chapter 17: Seismically Isolated Structures (64 KB)
- Chapter 18: Structures with Damping Systems (81 KB)
- Chapter 19: Soil-Structure Interaction (19 KB)
- Chapter 20: Site Classification Procedure (7 KB)
- Chapter 21: Site-Specific Ground Motion (3 KB)
- Chapter 22: Seismic Ground Motion Maps (32 KB)
- Chapter 23: Seismic Design Reference Documents (18 KB)

**Wind & Tornado (Ch 26-32):**
- Chapter 26: Wind Loads - General Requirements (58 KB)
- Chapter 27: Wind MWFRS - Directional (37 KB)
- Chapter 28: Wind MWFRS - Envelope (18 KB)
- Chapter 29: Wind - Building Appurtenances (55 KB)
- Chapter 30: Wind - Components and Cladding (114 KB)
- Chapter 31: Wind Tunnel Procedure (18 KB)
- Chapter 32: Tornado Loads (81 KB)

**Reserved:**
- Chapter 24-25: Reserved for Future Provisions

**Note:** Chapters 8 (Rain Loads) and 9 (Reserved) not available due to source limitations

## Automation Scripts

### 1. Smart Search
Find relevant chapters based on keywords:
```bash
python3 scripts/smart_search.py "seismic design category"
```

### 2. Formula Finder
Extract formulas with context:
```bash
python3 scripts/formula_finder.py "V =" data/Chapter_12_Seismic_Design_Requirements_Building.md
```

### 3. Load Combinator
Generate applicable load combinations:
```bash
python3 scripts/load_combinator.py --design LRFD --loads D,L,W,S
```

## Directory Structure

```
asce7-loads-design/
├── SKILL.md              # Main skill definition
├── README.md             # This file
├── PROJECT_SUMMARY.md    # Project overview and summary
├── data/                 # Complete chapter files (30 chapters)
│   ├── Chapter_01_General.md
│   ├── Chapter_02_Combinations_of_Loads.md
│   ├── Chapter_03_Dead_Loads_Soil_Loads_Hydrostatic_Pressure.md
│   ├── Chapter_04_Live_Loads.md
│   ├── Chapter_05_Flood_Loads.md
│   ├── Chapter_06_Tsunami_Loads_and_Effects.md
│   ├── Chapter_07_Snow_Loads.md
│   ├── Chapter_10_Ice_Loads_Atmospheric_Icing.md
│   ├── Chapter_11_Seismic_Design_Criteria.md
│   ├── Chapter_12_Seismic_Design_Requirements_Building.md
│   ├── Chapter_13-23_*.md (13 seismic chapters)
│   ├── Chapter_24-25_Reserved_for_Future_Provisions.md
│   └── Chapter_26-32_*.md (7 wind/tornado chapters)
├── scripts/              # Automation tools
│   ├── smart_search.py
│   ├── formula_finder.py
│   └── load_combinator.py
└── references/           # Quick reference guides
    ├── chapter-structure.md
    ├── glossary.md
    ├── load-combinations-index.md
    ├── symbols.md
    └── workflows.md
```

## Example Queries

**Load Combinations:**
- "What LRFD load combinations do I need for dead, live, and wind loads?"
- "Show me ASD load combinations with seismic"

**Wind Loads:**
- "Calculate velocity pressure for 120 mph wind at 30 ft height, Exposure C"
- "What's the difference between Exposure B and C?"

**Seismic:**
- "How do I calculate seismic base shear using ELF method?"
- "What is my Seismic Design Category for SDS = 0.45g?"

**Snow:**
- "Calculate flat roof snow load for 40 psf ground snow"
- "How do I design for snow drift?"

## Key Features

### 1. Complete ASCE 7-22 Coverage
- 30 of 32 chapters fully consolidated (~1.2 MB total)
- 400+ pages of technical content
- All major load types covered
- Complete seismic design chapters (Ch 11-23)
- Full wind and tornado load coverage (Ch 26-32)

### 2. Intelligent Search
- Category-aware keyword mapping
- Relevance scoring across all chapters
- Fast chapter identification
- Support for all load types

### 3. Formula Extraction
- Automatic equation number detection
- Variable definitions with units
- Context preservation (±5 lines)
- Works across all 30 chapters

### 4. Load Combination Generation
- LRFD and ASD support
- Seismic/flood/ice special combinations
- Automatic filtering by applicable loads
- Complete Chapter 2 coverage

## Tips for Best Results

1. **Be specific about loads**: "D, L, W, S, E" not just "typical building"
2. **State design method**: LRFD or ASD
3. **Provide building context**: Height, occupancy, location, seismic zone
4. **Ask for sections**: "Show Section 12.8" for targeted info
5. **Specify load type**: Wind, seismic, snow, tsunami, tornado, etc.

## Limitations

- Chapters 8 (Rain Loads) and 9 (Reserved) not available
- Commentary sections not yet included
- Maps and figures described in text only
- Some tables may be text-formatted rather than visual

## Support

For issues or questions:
- Check SKILL.md for detailed workflows
- Review reference files in `references/` directory
- Run scripts with `--help` flag for usage

## License

ASCE 7-22 content is copyright American Society of Civil Engineers.
This skill provides access for authorized users only.

---

**Version:** 2.0
**Last Updated:** 2025-11-20
**Coverage:** 30 of 32 ASCE 7-22 chapters
**Status:** Production Ready

**Generated with Claude Code**
