"""
Drawing Engine - JSON 시퀀스 자동 실행 및 학습 시스템
Claude Code MCP 도구와 연동하여 사용

사용법:
    engine = DrawingEngine()
    engine.load_knowledge()  # 세션 시작 시 지식 로드
    result = engine.execute_sequence("simple_room")  # 시퀀스 실행
    engine.record_result(result)  # 결과 기록
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from enum import Enum

# 경로 설정
KNOWLEDGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"


@dataclass
class ExecutionResult:
    """실행 결과 데이터 클래스"""
    sequence_name: str
    status: TaskStatus
    steps_completed: int
    total_steps: int
    entity_counts: Dict[str, int] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    duration_ms: int = 0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict:
        result = asdict(self)
        result['status'] = self.status.value
        return result


class KnowledgeStore:
    """지식 저장소 관리"""

    def __init__(self, root_path: str = KNOWLEDGE_ROOT):
        self.root = root_path
        self.patterns = {}
        self.sequences = {}
        self.successes = []
        self.failures = []
        self.best_practices = []

    def load_all(self) -> Dict[str, Any]:
        """모든 지식 파일 로드"""
        loaded = {}

        # 패턴 로드
        patterns_path = os.path.join(self.root, "patterns")
        if os.path.exists(patterns_path):
            for filename in ["elements.json", "drawing_types.json", "calculations.json"]:
                filepath = os.path.join(patterns_path, filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        key = filename.replace('.json', '')
                        self.patterns[key] = json.load(f)
                        loaded[f"patterns/{filename}"] = True

        # 시퀀스 로드
        sequences_path = os.path.join(self.root, "references", "example_sequences.json")
        if os.path.exists(sequences_path):
            with open(sequences_path, 'r', encoding='utf-8') as f:
                self.sequences = json.load(f)
                loaded["references/example_sequences.json"] = True

        # 학습 기록 로드
        successes_path = os.path.join(self.root, "lessons", "successes.json")
        if os.path.exists(successes_path):
            with open(successes_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.successes = data.get("entries", [])
                self.best_practices = data.get("best_practices", {}).get("items", [])
                loaded["lessons/successes.json"] = len(self.successes)

        failures_path = os.path.join(self.root, "lessons", "failures.json")
        if os.path.exists(failures_path):
            with open(failures_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.failures = data.get("entries", [])
                loaded["lessons/failures.json"] = len(self.failures)

        return loaded

    def get_sequence(self, name: str) -> Optional[Dict]:
        """시퀀스 조회"""
        return self.sequences.get(name)

    def get_element_pattern(self, element_type: str) -> Optional[Dict]:
        """요소별 패턴 조회"""
        elements = self.patterns.get("elements", {})
        return elements.get(element_type)

    def get_lessons_for_task(self, task_type: str) -> Dict[str, List]:
        """특정 작업 유형에 관련된 교훈 조회"""
        relevant_successes = [
            s for s in self.successes
            if task_type in s.get("tags", []) or task_type in s.get("task", "")
        ]
        relevant_failures = [
            f for f in self.failures
            if task_type in f.get("tags", []) or task_type in f.get("task", "")
        ]
        return {
            "successes": relevant_successes,
            "failures": relevant_failures,
            "best_practices": self.best_practices
        }

    def add_success(self, entry: Dict) -> str:
        """성공 기록 추가"""
        # ID 생성
        existing_ids = [s.get("id", "S000") for s in self.successes]
        max_num = max([int(id[1:]) for id in existing_ids if id.startswith("S")], default=0)
        new_id = f"S{max_num + 1:03d}"

        entry["id"] = new_id
        entry["date"] = datetime.now().strftime("%Y-%m-%d")
        self.successes.append(entry)

        self._save_lessons("successes")
        return new_id

    def add_failure(self, entry: Dict) -> str:
        """실패 기록 추가"""
        existing_ids = [f.get("id", "F000") for f in self.failures]
        max_num = max([int(id[1:]) for id in existing_ids if id.startswith("F")], default=0)
        new_id = f"F{max_num + 1:03d}"

        entry["id"] = new_id
        entry["date"] = datetime.now().strftime("%Y-%m-%d")
        self.failures.append(entry)

        self._save_lessons("failures")
        return new_id

    def _save_lessons(self, lesson_type: str):
        """학습 기록 저장"""
        filepath = os.path.join(self.root, "lessons", f"{lesson_type}.json")

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if lesson_type == "successes":
            data["entries"] = self.successes
            data["statistics"]["total_count"] = len([s for s in self.successes if s["id"] != "S000"])
            # 태그별 통계 업데이트
            tag_counts = {}
            for s in self.successes:
                for tag in s.get("tags", []):
                    if tag != "template":
                        tag_counts[tag] = tag_counts.get(tag, 0) + 1
            data["statistics"]["by_tag"] = tag_counts
        else:
            data["entries"] = self.failures
            data["statistics"]["total_count"] = len([f for f in self.failures if f["id"] != "F000"])
            tag_counts = {}
            for f in self.failures:
                for tag in f.get("tags", []):
                    if tag != "template":
                        tag_counts[tag] = tag_counts.get(tag, 0) + 1
            data["statistics"]["by_tag"] = tag_counts

        data["statistics"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


class SequenceExecutor:
    """시퀀스 실행기 - MCP 도구 호출 명령 생성"""

    def __init__(self, knowledge: KnowledgeStore):
        self.knowledge = knowledge

    def prepare_sequence(self, sequence_name: str) -> List[Dict]:
        """시퀀스를 MCP 도구 호출 목록으로 변환"""
        sequence_data = self.knowledge.get_sequence(sequence_name)
        if not sequence_data:
            raise ValueError(f"Sequence not found: {sequence_name}")

        steps = sequence_data.get("sequence", [])
        mcp_calls = []

        for step in steps:
            step_calls = {
                "step": step.get("step"),
                "name": step.get("name"),
                "parallel": step.get("parallel", False),
                "tools": []
            }

            # pre_action 처리
            if "pre_action" in step:
                pre = step["pre_action"]
                step_calls["tools"].append({
                    "tool": pre["tool"],
                    "args": pre["args"],
                    "is_pre_action": True
                })

            # 메인 도구들
            for tool_item in step.get("tools", []):
                step_calls["tools"].append({
                    "tool": tool_item["tool"],
                    "args": tool_item["args"],
                    "comment": tool_item.get("comment", "")
                })

            mcp_calls.append(step_calls)

        return mcp_calls

    def generate_mcp_command(self, tool_name: str, args: Dict) -> str:
        """MCP 도구 호출 명령 생성 (Claude가 실행할 형태)"""
        # mcp__stgen-dxf-viewer__ 접두사 추가
        full_tool_name = f"mcp__stgen-dxf-viewer__{tool_name}"
        return {
            "tool": full_tool_name,
            "args": args
        }


class DrawingEngine:
    """메인 드로잉 엔진"""

    def __init__(self):
        self.knowledge = KnowledgeStore()
        self.executor = SequenceExecutor(self.knowledge)
        self.current_task: Optional[str] = None
        self.execution_log: List[Dict] = []

    def load_knowledge(self) -> Dict:
        """세션 시작 시 지식 로드"""
        loaded = self.knowledge.load_all()

        # 로드 요약 생성
        summary = {
            "loaded_files": loaded,
            "available_sequences": list(self.knowledge.sequences.keys()) if self.knowledge.sequences else [],
            "success_count": len([s for s in self.knowledge.successes if s.get("id") != "S000"]),
            "failure_count": len([f for f in self.knowledge.failures if f.get("id") != "F000"]),
            "best_practices": self.knowledge.best_practices
        }

        # 최근 실패에서 주의사항 추출
        if self.knowledge.failures:
            recent_failures = sorted(
                [f for f in self.knowledge.failures if f.get("id") != "F000"],
                key=lambda x: x.get("date", ""),
                reverse=True
            )[:3]
            summary["recent_warnings"] = [
                {"cause": f.get("cause"), "prevention": f.get("prevention")}
                for f in recent_failures
            ]

        return summary

    def get_sequence_plan(self, sequence_name: str) -> Dict:
        """시퀀스 실행 계획 조회"""
        try:
            mcp_calls = self.executor.prepare_sequence(sequence_name)
            sequence_data = self.knowledge.get_sequence(sequence_name)

            return {
                "name": sequence_data.get("name"),
                "description": sequence_data.get("description"),
                "total_steps": len(mcp_calls),
                "steps": mcp_calls,
                "expected_result": sequence_data.get("expected_result", {})
            }
        except ValueError as e:
            return {"error": str(e)}

    def record_success(self, task: str, approach: str, key_factors: List[str],
                       result: Dict, tags: List[str], notes: str = "") -> str:
        """성공 기록"""
        entry = {
            "task": task,
            "context": f"Drawing Engine 자동 기록",
            "approach": approach,
            "key_factors": key_factors,
            "result": result,
            "efficiency_notes": notes,
            "reusable": True,
            "tags": tags
        }
        return self.knowledge.add_success(entry)

    def record_failure(self, task: str, error: str, cause: str,
                       solution: str, prevention: str, tags: List[str]) -> str:
        """실패 기록"""
        entry = {
            "task": task,
            "context": f"Drawing Engine 자동 기록",
            "error": error,
            "cause": cause,
            "solution": solution,
            "prevention": prevention,
            "tags": tags
        }
        return self.knowledge.add_failure(entry)

    def get_recommendations(self, task_description: str) -> Dict:
        """작업에 대한 추천 제공"""
        recommendations = {
            "suggested_sequence": None,
            "relevant_lessons": [],
            "warnings": []
        }

        # 키워드 매칭으로 시퀀스 추천
        keywords = task_description.lower()
        for seq_name, seq_data in self.knowledge.sequences.items():
            if seq_name in ["version", "description"]:
                continue
            seq_desc = seq_data.get("description", "").lower()
            if any(kw in seq_desc for kw in keywords.split()):
                recommendations["suggested_sequence"] = seq_name
                break

        # 관련 교훈 조회
        for tag in ["floor_plan", "grid", "wall", "dimension", "bolt"]:
            if tag in keywords:
                lessons = self.knowledge.get_lessons_for_task(tag)
                recommendations["relevant_lessons"].extend(lessons.get("successes", []))
                for f in lessons.get("failures", []):
                    recommendations["warnings"].append(f.get("prevention"))

        return recommendations


# 유틸리티 함수 - Claude가 직접 호출할 수 있는 형태
def load_engine() -> Dict:
    """엔진 초기화 및 지식 로드"""
    engine = DrawingEngine()
    return engine.load_knowledge()


def get_sequence(name: str) -> Dict:
    """시퀀스 계획 조회"""
    engine = DrawingEngine()
    engine.load_knowledge()
    return engine.get_sequence_plan(name)


def list_sequences() -> List[str]:
    """사용 가능한 시퀀스 목록"""
    engine = DrawingEngine()
    engine.load_knowledge()
    return [k for k in engine.knowledge.sequences.keys()
            if k not in ["version", "description"]]


if __name__ == "__main__":
    # 테스트
    print("=== Drawing Engine Test ===\n")

    engine = DrawingEngine()
    summary = engine.load_knowledge()

    print("Loaded Knowledge:")
    print(f"  - Sequences: {summary['available_sequences']}")
    print(f"  - Successes: {summary['success_count']}")
    print(f"  - Failures: {summary['failure_count']}")

    print("\n--- simple_room sequence plan ---")
    plan = engine.get_sequence_plan("simple_room")
    if "error" not in plan:
        print(f"Name: {plan['name']}")
        print(f"Steps: {plan['total_steps']}")
        for step in plan['steps']:
            parallel_mark = "[P]" if step['parallel'] else "[S]"
            print(f"  {step['step']}. {parallel_mark} {step['name']} - {len(step['tools'])} tools")
