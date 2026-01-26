#!/usr/bin/env python3
"""
Extract reference files from ADM2020 Symbols.md
Creates: symbols.md, glossary.md, abbreviations.md
"""

import re
from pathlib import Path

def extract_symbols(content):
    """Extract mathematical symbols section"""
    # Find symbols section (before glossary)
    symbol_section = re.search(r'## Symbols\s*$(.*?)(?=## GLOSSARY|$)', content, re.DOTALL | re.MULTILINE)

    if not symbol_section:
        return "# Symbols\n\nNo symbols found.\n"

    symbols_text = symbol_section.group(1)

    # Format as reference file
    output = """# ADM 2020 Mathematical Symbols

Quick reference for mathematical notation used in the Aluminum Design Manual.

## Symbol Definitions

"""
    output += symbols_text.strip()
    output += "\n\n---\n\n*Extracted from ADM 2020 Front Matter*\n"

    return output

def extract_glossary(content):
    """Extract glossary section"""
    # Find glossary section
    glossary_section = re.search(r'## GLOSSARY\s*$(.*?)$', content, re.DOTALL | re.MULTILINE)

    if not glossary_section:
        return "# Glossary\n\nNo glossary found.\n"

    glossary_text = glossary_section.group(1)

    # Format as reference file
    output = """# ADM 2020 Glossary

Technical terms and definitions for aluminum structural design.

## Definitions

"""
    output += glossary_text.strip()
    output += "\n\n---\n\n*Extracted from ADM 2020 Front Matter*\n"

    return output

def create_abbreviations():
    """Create abbreviations reference file"""
    return """# ADM 2020 Abbreviations

Common abbreviations used in aluminum structural design.

## Standard Abbreviations

### Organizations
- **ADM**: Aluminum Design Manual
- **AA**: The Aluminum Association
- **ASTM**: American Society for Testing and Materials
- **AWS**: American Welding Society
- **ASCE**: American Society of Civil Engineers
- **AISC**: American Institute of Steel Construction (for comparison)

### Design Methods
- **ASD**: Allowable Strength Design
- **LRFD**: Load and Resistance Factor Design (NOT used in ADM - steel only)

### Material & Properties
- **HAZ**: Heat-Affected Zone (welding)
- **Fty**: Tensile yield strength
- **Ftu**: Tensile ultimate strength
- **Fcy**: Compressive yield strength
- **Fsu**: Shear ultimate strength
- **E**: Modulus of elasticity (10,100 ksi for aluminum)

### Temper Designations
- **T4**: Solution heat treated, naturally aged
- **T5**: Cooled from elevated temperature, artificially aged
- **T6**: Solution heat treated, artificially aged
- **H**: Strain-hardened (non-heat-treatable alloys)
- **O**: Annealed (softest condition)

### Structural Elements
- **W-shape**: Wide-flange I-beam
- **HSS**: Hollow Structural Section (tube)
- **CJP**: Complete Joint Penetration (weld)
- **PJP**: Partial Joint Penetration (weld)

### Loading & Analysis
- **DL**: Dead Load
- **LL**: Live Load
- **WL**: Wind Load
- **SL**: Snow Load
- **EQ**: Earthquake Load
- **P-Δ**: P-Delta effect (second-order)

### Quality Control
- **QC**: Quality Control
- **QA**: Quality Assurance
- **NDT**: Non-Destructive Testing

### Connections
- **CJP**: Complete Joint Penetration
- **PJP**: Partial Joint Penetration
- **SMAW**: Shielded Metal Arc Welding
- **GMAW**: Gas Metal Arc Welding

---

*Compiled for ADM 2020*
"""

def main():
    # Read source file
    source_file = Path(__file__).parent.parent / "data" / "Symbols.md"

    if not source_file.exists():
        print(f"Error: {source_file} not found")
        return

    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Output directory
    output_dir = Path(__file__).parent.parent / "references"
    output_dir.mkdir(exist_ok=True)

    # Extract and save symbols
    symbols = extract_symbols(content)
    with open(output_dir / "symbols.md", 'w', encoding='utf-8') as f:
        f.write(symbols)
    print(f"✓ Created: references/symbols.md")

    # Extract and save glossary
    glossary = extract_glossary(content)
    with open(output_dir / "glossary.md", 'w', encoding='utf-8') as f:
        f.write(glossary)
    print(f"✓ Created: references/glossary.md")

    # Create abbreviations
    abbreviations = create_abbreviations()
    with open(output_dir / "abbreviations.md", 'w', encoding='utf-8') as f:
        f.write(abbreviations)
    print(f"✓ Created: references/abbreviations.md")

    print("\n✓ Reference extraction complete!")

if __name__ == '__main__':
    main()
