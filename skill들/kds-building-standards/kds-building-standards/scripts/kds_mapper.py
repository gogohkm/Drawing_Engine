#!/usr/bin/env python3
"""
KDS Document Mapper
한글 문서명과 영문 키워드를 매핑하여 검색 가능하게 함
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
import re
import sys

class KDSMapper:
    def __init__(self, metadata_path: Optional[str] = None):
        """KDS 메타데이터 로드"""
        if metadata_path is None:
            # 스크립트 위치 기준으로 메타데이터 경로 설정
            script_dir = Path(__file__).parent
            metadata_path = script_dir.parent / "references" / "kds-metadata.json"

        self.metadata_path = Path(metadata_path)

        try:
            with open(self.metadata_path, 'r', encoding='utf-8') as f:
                self.metadata = json.load(f)
        except FileNotFoundError:
            print(f"❌ 메타데이터 파일을 찾을 수 없습니다: {self.metadata_path}")
            sys.exit(1)

        self.documents = self.metadata['documents']
        self.categories = self.metadata['categories']
        self.aliases = self.metadata['search_aliases']

    def find_by_kds_id(self, query: str) -> Optional[Dict]:
        """KDS ID로 검색"""
        numbers = re.findall(r'\d+', query)
        if len(numbers) >= 3:
            kds_id = f"KDS_{numbers[0]}_{numbers[1]}_{numbers[2]}"
            return self.documents.get(kds_id)
        return None

    def find_by_english(self, query: str) -> List[Dict]:
        """영문 키워드로 검색"""
        query_lower = query.lower()
        results = []

        if query_lower in self.aliases:
            kds_id = self.aliases[query_lower]
            results.append(self.documents[kds_id])
            return results

        for doc_id, doc in self.documents.items():
            for keyword in doc['keywords_english']:
                if query_lower in keyword.lower():
                    results.append(doc)
                    break

        return results

    def find_by_korean(self, query: str) -> List[Dict]:
        """한글 키워드로 검색"""
        results = []

        for doc_id, doc in self.documents.items():
            if query in doc['korean_title']:
                results.append(doc)
                continue

            for keyword in doc['keywords_korean']:
                if query in keyword:
                    results.append(doc)
                    break

        return results

    def smart_search(self, query: str, max_results: int = 5) -> List[Dict]:
        """통합 스마트 검색"""
        results = []

        if re.search(r'\d{2}[-_\s]?\d{2}[-_\s]?\d{2}', query):
            result = self.find_by_kds_id(query)
            if result:
                return [result]

        has_korean = bool(re.search(r'[가-힣]', query))

        if has_korean:
            results = self.find_by_korean(query)
        else:
            results = self.find_by_english(query)

        scored_results = []
        for doc in results:
            score = 0
            all_keywords = doc['keywords_korean'] + doc['keywords_english']
            for keyword in all_keywords:
                if query.lower() in keyword.lower():
                    score += 1

            if query in doc['korean_title'] or query.lower() in doc['english_title'].lower():
                score += 5

            scored_results.append((score, doc))

        scored_results.sort(key=lambda x: x[0], reverse=True)

        return [doc for score, doc in scored_results[:max_results]]

    def get_document_path(self, kds_id: str) -> Optional[Path]:
        """KDS ID로 실제 문서 경로 반환"""
        if kds_id in self.documents:
            filename = self.documents[kds_id]['filename']
            script_dir = Path(__file__).parent
            doc_path = script_dir.parent / "data" / "kds-documents" / filename
            return doc_path if doc_path.exists() else None
        return None

def main():
    """CLI 인터페이스"""
    import argparse

    parser = argparse.ArgumentParser(description='KDS 문서 검색 도구')
    parser.add_argument('query', nargs='*', help='검색어')
    parser.add_argument('--stats', action='store_true', help='통계')

    args = parser.parse_args()

    mapper = KDSMapper()

    if args.stats:
        print(f"총 문서: {mapper.metadata['total_documents']}개")
        print(f"총 이미지: {mapper.metadata['total_images']}개")
        return

    if not args.query:
        parser.print_help()
        return

    query = " ".join(args.query)
    results = mapper.smart_search(query)

    print(f"\n검색어: '{query}'")
    print(f"결과: {len(results)}개\n")

    for i, doc in enumerate(results, 1):
        print(f"[{i}] {doc['korean_title']} ({doc['english_title']})")
        print(f"    ID: {doc['id']}, 파일: {doc['filename']}\n")

if __name__ == "__main__":
    main()
