---
name: kds-building-standards
description: "한국 건축구조기준(KDS) 75개 문서를 검색하고 구조계산을 수행하며, 설계 워크플로우를 제공합니다. 내진설계, 콘크리트/강구조, 기초, 하중, 가설구조 등 모든 KDS 기준을 지원하며, 공식 추출, 이미지 분석, 용어 설명, 기준 비교를 제공합니다. 모든 문서와 이미지 설명이 스킬에 포함되어 있어 독립적으로 사용 가능합니다."
---

# Korean Building Standards (KDS) Expert

Use this skill when users ask questions about Korean building codes, structural design calculations, seismic design, concrete/steel structures, foundations, loads, or any KDS (Korean Design Standards) related queries in Korean or English.

## Trigger Keywords

**Korean**: KDS, 건축구조기준, 건축구조, 내진설계, 지진, 밑면전단력, 콘크리트, 강구조, 철골, 철근, 하중, 풍하중, 적설하중, 기초, 지반, 옹벽, 허용응력, LRFD, ASD, 설계기준, 구조설계, 휨강도, 전단강도, 보, 기둥, 슬래브, 벽체, 가새골조, 모멘트골조, 가설구조, 거푸집, 동바리

**English**: KDS, Korean Design Standard, Korean building code, seismic design, earthquake, base shear, concrete structure, steel structure, foundation design, retaining wall, allowable stress design, load resistance factor design, structural code, wind load, snow load, seismic load, live load, dead load, flexural strength, shear strength, column design, beam design

## Tools Required

- **Grep**: Search keywords in KDS documents
- **Read**: Read specific KDS documents and image descriptions
- **Glob**: Find files by patterns
- **Bash**: Execute Python scripts for searches and calculations
- **Write**: (Optional) Save calculation results

## Document Access Strategy

**All 75 KDS documents and 206 image descriptions are bundled in this skill** at `data/kds-documents/` and `data/image-descriptions/`.

### Progressive Disclosure (3-Level Search)

**Level 1: Metadata Lookup** (Fastest - 0.1s)
- Use `scripts/kds_mapper.py` for instant Korean↔English mapping
- Accepts: KDS ID ("41-12-00"), English keywords ("seismic design"), Korean keywords ("내진설계")
- Returns: Document info, related standards, formula locations, image lists

**Level 2: Reference Files** (Medium - 0.5s)
- `references/glossary.md` - Korean-English terminology (100+ terms)
- `references/workflows.md` - 8 query type workflows, design procedures
- `references/kds-metadata.json` - Complete metadata (130 KB)

**Level 3: Full Document Search** (Detailed - 2-5s)
- Use Grep on `data/kds-documents/*.md`
- Read specific sections with line numbers from metadata
- Load image descriptions from `data/image-descriptions/`

## Workflow by Query Type

### 1. Formula Query (공식 질의)

**User Intent**: Find specific equation from KDS

**Example Queries**:
- "내진설계에서 밑면전단력 공식은?"
- "What is the formula for base shear in KDS?"
- "풍하중 계산식 알려줘"

**Quick Process**:
1. Run `kds_mapper.py` to identify document
2. Check metadata `key_formulas` for line numbers
3. Read document at specific line range
4. Extract formula + variable definitions
5. Present with KDS citation

**Output Format**:
```
📐 공식: V = CₛW
📍 출처: KDS 41 17 00 Section 6.2.1, Line 850-880

변수 정의:
  V = 밑면전단력 (kN)
  Cₛ = 지진응답계수 (무차원)
  W = 유효지진중량 (kN)
```

### 2. Calculation Query (계산 질의)

**User Intent**: Perform actual structural calculations

**Example Queries**:
- "5층 건물 밑면전단력 계산: 지진구역 0.176g, 중요도계수 1.2"
- "Calculate wind load for 20m height building"

**Quick Process**:
1. Find formula (use Formula Query workflow)
2. Gather input parameters from user
3. Generate Python code following KDS formulas
4. Execute calculation
5. Validate against KDS limits
6. Present result + calculation steps + KDS reference

**KDS-Specific Checks**:
- ✅ Version specified (22.10, 21.02, etc.)
- ✅ Units in SI (MPa, kN, m, mm)
- ✅ Korean seismic zone coefficients
- ✅ Load combinations per KDS 41 12 00
- ✅ Material properties in MPa

### 3. Image Description Query (이미지 질의)

**User Intent**: View technical diagrams/charts

**Example Queries**:
- "풍력계수 그래프 보여줘"
- "Show me response spectrum diagram"
- "지진구역도 있어?"

**Quick Process**:
1. Use `kds_mapper.py` to identify document
2. Check metadata `images` list
3. Run `scripts/image_linker.py KDS_XX_YY_ZZ --image N`
4. Present ASCII art + technical description

**Example**:
```
🖼️ Image 26: 지붕 경사각에 따른 풍력계수
📍 KDS 41 12 00, Section 5.4.3

[ASCII art diagram showing wind pressure coefficients vs roof slope]
```

### 4. Terminology Query (용어 질의)

**User Intent**: Understand Korean/English technical terms

**Example Queries**:
- "반응수정계수가 뭐야?"
- "What is lateral-torsional buckling in Korean?"

**Quick Process**:
1. Check `references/glossary.md`
2. If not found, search "용어의 정의" section in relevant KDS
3. Present: 한글 | English | Definition | Units

### 5. Comparison Query (비교 질의)

**User Intent**: Compare KDS with international codes or different methods

**Example Queries**:
- "KDS와 IBC 내진설계 차이는?"
- "LRFD vs ASD 차이"

**Quick Process**:
1. Identify comparison items
2. Extract key differences:
   - Design philosophy
   - Key coefficients
   - Load combinations
   - Application scope
3. Present in comparison table

**KDS vs International Codes**:
- Seismic: Korean seismic zone map vs ASCE 7
- Wind: Korean basic wind speed vs ASCE 7
- Units: SI units (MPa, kN, m) standard

### 6. Related Standards Query (관련 기준 질의)

**User Intent**: Find related KDS documents

**Example Queries**:
- "콘크리트 구조설계에 필요한 KDS는?"
- "What standards are related to KDS 41 17 00?"

**Quick Process**:
1. Use `kds_mapper.py` to lookup document
2. Check metadata `related_standards`
3. Present document hierarchy with roles

### 7-8. Symbol Query & Design Example Query

See `references/workflows.md` for detailed procedures.

## Quick Reference Tables

### Document Categories (75 documents organized)

| Category | Korean | Key Documents | Common Keywords |
|----------|--------|---------------|-----------------|
| **Loads** | 하중 | KDS_41_12_00 | 풍하중, 적설하중, 지진하중, wind, snow |
| **Seismic** | 내진 | KDS_41_17_00, 17_10_00 | 지진, 밑면전단력, base shear, response spectrum |
| **Concrete** | 콘크리트 | KDS_41_20_00, 14_20_** | 철근, 휨강도, flexural, shear, rebar |
| **Steel** | 강구조 | KDS_41_30_10, 14_31_** | LRFD, ASD, 좌굴, buckling |
| **Foundation** | 기초 | KDS_41_19_00, 11_50_** | 지반, 지지력, bearing capacity |
| **Temporary** | 가설 | KDS_21_** | 거푸집, 동바리, formwork, shoring |
| **Wood** | 목구조 | KDS_41_50_** | 목재, timber, wood |
| **Masonry** | 조적 | KDS_41_60_** | 벽돌, block, brick |
| **Composite** | 합성 | KDS_41_40_**, 14_31_80 | 강-콘크리트, steel-concrete |
| **Aluminum/Glass** | 알루미늄/유리 | KDS_41_80_** | aluminum, glass |

### Common Search Patterns

| User Query | Category | Primary KDS | Script Command |
|------------|----------|-------------|----------------|
| "풍하중 계산" | Loads | 41_12_00 | `kds_mapper.py 풍하중` |
| "seismic design" | Seismic | 41_17_00 | `kds_mapper.py seismic` |
| "콘크리트 보" | Concrete | 14_20_20 | `kds_mapper.py "콘크리트 휨"` |
| "steel column" | Steel | 14_31_10 | `kds_mapper.py "강구조 압축"` |
| "41-12-00" | Direct | 41_12_00 | `kds_mapper.py 41-12-00` |

### KDS Naming Convention

**Format**: `KDS_XX_YY_ZZ_제목_버전.md`

- **XX**: Major category (10=General, 11=Geotechnical, 14=Materials, 17=Seismic, 21=Temporary, 41=Building)
- **YY**: Subcategory (10=General, 12=Loads, 17=Seismic, 20=Concrete, 30=Steel)
- **ZZ**: Specific topic (00=General, others vary)
- **버전**: YY.MM format (e.g., 22.10 = October 2022)

**Examples**:
- `KDS_41_12_00` = Building (41) > Loads (12) > General (00)
- `KDS_14_20_80` = Materials (14) > Concrete (20) > Seismic (80)
- `KDS_41_17_00` = Building (41) > Seismic (17) > General (00)

## Automation Scripts

Execute from `scripts/` directory:

### 1. kds_mapper.py - Smart Search

**Purpose**: Unified Korean/English/KDS ID search with metadata lookup

**Usage**:
```bash
# Korean search
python3 kds_mapper.py "내진설계"

# English search
python3 kds_mapper.py "seismic design"

# KDS ID search
python3 kds_mapper.py "41-17-00"

# Statistics
python3 kds_mapper.py --stats
```

**Returns**: Document info, filename, category, formulas, images

### 2. formula_finder.py - Formula Extraction

**Purpose**: Extract formulas with context from KDS documents

**Usage**:
```bash
# Find specific formula pattern
python3 formula_finder.py "V =" KDS_41_17_00

# Search by line range
python3 formula_finder.py --line-range 850-900 KDS_41_17_00
```

### 3. image_linker.py - Image Description Access

**Purpose**: Find and display image descriptions

**Usage**:
```bash
# List all images for a document
python3 image_linker.py KDS_41_12_00

# View specific image
python3 image_linker.py KDS_41_12_00 --image 26 --read

# Search in descriptions
python3 image_linker.py KDS_41_12_00 --search "풍력계수"
```

## Response Quality Checklist

Every response should include:

- ✅ **Accurate KDS citation** (KDS XX YY ZZ Section X.Y.Z)
- ✅ **Version specified** (22.10, 21.02, etc.)
- ✅ **Units in SI** (MPa, kN, m, mm - not psi, kip, ft)
- ✅ **Variable definitions** from glossary.md or document
- ✅ **Working Python code** for calculations (tested and validated)
- ✅ **Cross-references** to related standards when relevant
- ✅ **Korean-English bilingual** (terms in both languages when applicable)
- ✅ **Calculation validation** against KDS limits and typical ranges

## Special Features: KDS-Specific Considerations

### 1. Korean Seismic Design Unique Features

**vs. International Codes (IBC/ASCE 7)**:
- **Seismic Zone Map**: Korea-specific (7 zones based on 2017 map)
- **Seismic Zone Coefficient (S)**: 0.11g to 0.22g for most regions
- **Design Philosophy**: Similar to IBC but with Korean-specific factors
- **Soil Classification**: A, B, C, D, E (similar to ASCE 7 but Korean criteria)

**Key Documents**:
- KDS 17 10 00: General seismic design principles
- KDS 41 17 00: Building-specific seismic design
- Material-specific: KDS 14 20 80 (concrete), KDS 14 31 60 (steel)

### 2. Load Combinations

**KDS 41 12 00 Standard Combinations**:
1. 1.2D + 1.6L + 0.5(Lr or S or R)
2. 1.2D + 1.6(Lr or S or R) + (L or 0.5W)
3. 1.2D + 1.0W + L + 0.5(Lr or S or R)
4. 1.2D + 1.0E + L + 0.2S
5. 0.9D + 1.0W
6. 0.9D + 1.0E

### 3. Material Properties Standards

**Concrete** (fck in MPa):
- Common grades: 21, 24, 27, 30, 35, 40 MPa
- High-strength: up to 60 MPa (KDS 14 20 series)

**Steel** (Fy in MPa):
- SS400: Fy = 235 MPa
- SM490: Fy = 325 MPa
- SM520: Fy = 355 MPa

### 4. Image Description System

**206 Technical Diagrams** with ASCII art descriptions:
- Located in `data/image-descriptions/`
- Named: `KDS_XX_YY_ZZ_imageNN_description.md`
- Includes: Diagrams, charts, tables, maps
- Searchable by keyword

**Most Common Images**:
- KDS 41 12 00: 73 images (wind/snow load charts, coefficients)
- KDS 41 30 30: 55 images (cold-formed steel sections)
- KDS 14 31 10: 22 images (steel member design)

### 5. Version Control and Updates

**Version Tracking**:
- Each KDS has version in filename (e.g., `_22.10.md` = October 2022)
- Always cite version in responses
- Check for updates: Most recent versions are 22.10, 21.02, 24.12

**Superseded Standards**:
- Note if referencing older versions
- Recommend checking for latest updates

## Performance Optimization

### Search Strategy Priority

1. **Use `kds_mapper.py` first** (0.1 sec response)
   - Fastest way to find documents
   - Returns comprehensive metadata

2. **Check metadata before full search**
   - Line ranges for formulas
   - Image lists
   - Related documents

3. **Target specific documents** - don't grep all 75 files
   - Use category to narrow search
   - Use KDS ID for direct access

4. **Use line ranges when reading**
   - Metadata provides formula locations
   - Avoid loading entire large documents

### Python Script Usage

Always execute scripts from skill's scripts directory:

```bash
cd .claude/skills/kds-building-standards/scripts
python3 kds_mapper.py <query>
```

## Error Handling

### Common Scenarios

1. **Ambiguous query**:
   - Ask: "Did you mean [KDS A] or [KDS B]?"
   - Offer category options

2. **Missing parameters for calculation**:
   - List required values
   - Provide typical default values

3. **No results found**:
   - Suggest alternative Korean/English keywords
   - Check all categories
   - Offer to search broader terms

4. **Version confusion**:
   - Clarify which KDS version
   - Note if different versions have different provisions

## Validation Checks

For all structural calculations:
- ✅ Verify KDS version and applicability
- ✅ Check units consistency (MPa, kN, m throughout)
- ✅ Confirm load combinations per KDS 41 12 00
- ✅ Validate material properties within KDS ranges
- ✅ Cross-check with examples when available
- ✅ Note all assumptions clearly
- ✅ Warn if parameters outside typical ranges

---

# Quick Start Examples

**Search by Korean keyword**:
```
User: "내진설계 밑면전단력 공식 알려줘"
Assistant: [Executes kds_mapper.py "밑면전단력"] → KDS 41 17 00
          [Reads formula at line 850] → V = CₛW
          [Provides variables + citation]
```

**Search by English keyword**:
```
User: "Show me steel column design formula"
Assistant: [Executes kds_mapper.py "steel column"] → KDS 14 31 10
          [Extracts compression formulas]
```

**Direct KDS ID access**:
```
User: "41-12-00 풍하중 계산 방법"
Assistant: [Executes kds_mapper.py "41-12-00"] → KDS_41_12_00
          [Searches "풍하중" in document]
```

---

**Total Resources in This Skill**:
- ✅ 75 KDS documents (~86,000 lines, ~25 MB)
- ✅ 206 image descriptions (~2 MB)
- ✅ Complete metadata mapping (130 KB)
- ✅ 3 automation scripts
- ✅ 2 reference guides

**Skill is fully self-contained and ready for distribution.**

Always prioritize accuracy, cite KDS sources with versions, validate calculations against KDS limits, and provide bilingual Korean-English support.
