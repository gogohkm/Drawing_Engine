#!/usr/bin/env python3
"""
ASCE 7-22 Smart Search

Category-aware search for ASCE 7 load standards.
Maps user queries to relevant chapters using keyword analysis.

Usage:
    python3 smart_search.py "wind load calculation"
    python3 smart_search.py "seismic design category"
    python3 smart_search.py "load combinations LRFD"
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict
from dataclasses import dataclass

@dataclass
class SearchResult:
    """Search result with relevance scoring"""
    chapter: str
    title: str
    filename: str
    relevance_score: float
    matched_keywords: List[str]

# Category-to-chapter mappings
CATEGORY_KEYWORDS = {
    'load-combinations': {
        'keywords': ['load combination', 'LRFD', 'ASD', 'strength design', 'allowable stress',
                     'factored load', 'load factor', 'extraordinary event'],
        'chapters': ['2'],
        'weight': 1.0
    },
    'dead-loads': {
        'keywords': ['dead load', 'self weight', 'soil load', 'hydrostatic pressure',
                     'lateral earth pressure'],
        'chapters': ['3'],
        'weight': 0.8
    },
    'live-loads': {
        'keywords': ['live load', 'occupancy', 'floor load', 'roof live load',
                     'concentrated load', 'uniform load', 'reduction'],
        'chapters': ['4'],
        'weight': 0.8
    },
    'flood': {
        'keywords': ['flood', 'flood zone', 'V zone', 'A zone', 'coastal', 'ASCE 24',
                     'base flood elevation', 'BFE'],
        'chapters': ['5'],
        'weight': 0.7
    },
    'tsunami': {
        'keywords': ['tsunami', 'tsunami wave', 'runup', 'inundation', 'tsunami force'],
        'chapters': ['6'],
        'weight': 0.7
    },
    'snow': {
        'keywords': ['snow load', 'snow drift', 'ground snow', 'flat roof snow',
                     'sloped roof snow', 'balanced snow', 'unbalanced snow', 'rain on snow'],
        'chapters': ['7'],
        'weight': 1.0
    },
    'rain': {
        'keywords': ['rain load', 'ponding', 'secondary drainage', 'primary drainage'],
        'chapters': ['8'],
        'weight': 0.6
    },
    'ice': {
        'keywords': ['ice load', 'atmospheric icing', 'freezing rain', 'wind on ice',
                     'ice thickness', 'glaze ice'],
        'chapters': ['10'],
        'weight': 0.8
    },
    'seismic-criteria': {
        'keywords': ['seismic design category', 'SDC', 'risk category', 'site class',
                     'spectral response', 'Ss', 'S1', 'Fa', 'Fv', 'seismic map'],
        'chapters': ['11'],
        'weight': 1.0
    },
    'seismic-building': {
        'keywords': ['seismic design', 'base shear', 'equivalent lateral force', 'ELF',
                     'period', 'response spectrum', 'response modification', 'R factor',
                     'diaphragm', 'drift', 'redundancy', 'irregularity', 'structural system'],
        'chapters': ['12'],
        'weight': 1.0
    },
    'seismic-nonstructural': {
        'keywords': ['nonstructural', 'component', 'cladding', 'partition', 'ceiling',
                     'equipment anchorage', 'Fp'],
        'chapters': ['13'],
        'weight': 0.7
    },
    'wind-general': {
        'keywords': ['wind load', 'wind speed', 'basic wind speed', 'exposure',
                     'exposure B', 'exposure C', 'exposure D', 'topographic factor',
                     'velocity pressure', 'gust factor', 'enclosure', 'wind hazard'],
        'chapters': ['26'],
        'weight': 1.0
    },
    'wind-mwfrs': {
        'keywords': ['MWFRS', 'main wind force', 'directional procedure', 'envelope procedure',
                     'pressure coefficient', 'Cp', 'GCp', 'rigid structure', 'flexible structure'],
        'chapters': ['27'],
        'weight': 1.0
    },
}

# Chapter information
CHAPTER_INFO = {
    '2': ('Combinations of Loads', 'Chapter_02_Combinations_of_Loads.md'),
    '3': ('Dead Loads, Soil Loads, Hydrostatic Pressure', 'Chapter_03_Dead_Loads_Soil_Hydrostatic.md'),
    '4': ('Live Loads', 'Chapter_04_Live_Loads.md'),
    '5': ('Flood Loads', 'Chapter_05_Flood_Loads.md'),
    '6': ('Tsunami Loads and Effects', 'Chapter_06_Tsunami_Loads_and_Effects.md'),
    '7': ('Snow Loads', 'Chapter_07_Snow_Loads.md'),
    '8': ('Rain Loads', 'Chapter_08_Rain_Loads.md'),
    '10': ('Ice Loads - Atmospheric Icing', 'Chapter_10_Ice_Loads_Atmospheric_Icing.md'),
    '11': ('Seismic Design Criteria', 'Chapter_11_Seismic_Design_Criteria.md'),
    '12': ('Seismic Design Requirements for Building Structures', 'Chapter_12_Seismic_Design_Requirements_Building.md'),
    '13': ('Seismic Design Requirements for Nonstructural Components', 'Chapter_13_Seismic_Design_Nonstructural.md'),
    '26': ('Wind Loads: General Requirements', 'Chapter_26_Wind_Loads_General_Requirements.md'),
    '27': ('Wind Loads on Buildings: MWFRS (Directional Procedure)', 'Chapter_27_Wind_Loads_MWFRS_Directional.md'),
}

def calculate_relevance(query: str, category_data: dict) -> Tuple[float, List[str]]:
    """Calculate relevance score for a category"""
    query_lower = query.lower()
    matched_keywords = []
    score = 0.0

    for keyword in category_data['keywords']:
        if keyword.lower() in query_lower:
            matched_keywords.append(keyword)
            # Longer keywords get higher weight
            keyword_score = len(keyword.split()) * 10
            score += keyword_score

    # Apply category weight
    score *= category_data['weight']

    return score, matched_keywords

def search_chapters(query: str, top_n: int = 5) -> List[SearchResult]:
    """Search for relevant chapters based on query"""
    chapter_scores: Dict[str, SearchResult] = {}

    # Score each category
    for category, category_data in CATEGORY_KEYWORDS.items():
        relevance, matched_kw = calculate_relevance(query, category_data)

        if relevance > 0:
            for chapter in category_data['chapters']:
                if chapter not in CHAPTER_INFO:
                    continue

                title, filename = CHAPTER_INFO[chapter]

                if chapter in chapter_scores:
                    # Accumulate scores if chapter matches multiple categories
                    chapter_scores[chapter].relevance_score += relevance
                    chapter_scores[chapter].matched_keywords.extend(matched_kw)
                else:
                    chapter_scores[chapter] = SearchResult(
                        chapter=chapter,
                        title=title,
                        filename=filename,
                        relevance_score=relevance,
                        matched_keywords=matched_kw
                    )

    # Sort by relevance
    results = sorted(chapter_scores.values(), key=lambda x: x.relevance_score, reverse=True)

    return results[:top_n]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 smart_search.py <query>")
        print("\nExamples:")
        print('  python3 smart_search.py "wind load calculation"')
        print('  python3 smart_search.py "seismic design category"')
        print('  python3 smart_search.py "load combinations"')
        return 1

    query = ' '.join(sys.argv[1:])
    results = search_chapters(query)

    if not results:
        print(f"No relevant chapters found for: '{query}'")
        print("\nTry keywords like:")
        print("  - wind, snow, seismic, load combination")
        print("  - LRFD, ASD, MWFRS, SDC, drift")
        return 1

    print(f"\n{'='*80}")
    print(f"Search Results for: '{query}'")
    print(f"{'='*80}\n")

    for i, result in enumerate(results, 1):
        print(f"{i}. Chapter {result.chapter}: {result.title}")
        print(f"   File: {result.filename}")
        print(f"   Relevance: {result.relevance_score:.1f}")
        print(f"   Matched: {', '.join(set(result.matched_keywords[:5]))}")
        print()

    # Show full path to data directory
    data_dir = Path(__file__).parent.parent / 'data'
    print(f"Data directory: {data_dir.absolute()}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
