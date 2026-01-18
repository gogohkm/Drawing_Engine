"""
Session CLI - 세션 시작 및 지식 관리
"""
import json
import os
from datetime import datetime
from typing import Dict, List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
KNOWLEDGE_ROOT = os.path.join(PROJECT_ROOT, "knowledge")


def session_start() -> str:
    """세션 시작 시 호출 - 지식 로드 및 요약 출력"""
    result = {
        "status": "ready",
        "timestamp": datetime.now().isoformat(),
        "knowledge_loaded": {},
        "available_sequences": [],
        "recent_successes": [],
        "warnings": [],
        "tips": [],
        "active_tasks": [],
    }

    # 시퀀스 로드
    seq_path = os.path.join(KNOWLEDGE_ROOT, "references", "example_sequences.json")
    if os.path.exists(seq_path):
        with open(seq_path, 'r', encoding='utf-8') as f:
            sequences = json.load(f)
            result["available_sequences"] = [
                {"name": k, "description": v.get("description", "")}
                for k, v in sequences.items()
                if k not in ["version", "description"]
            ]
            result["knowledge_loaded"]["sequences"] = len(result["available_sequences"])

    # 성공 기록 로드
    success_path = os.path.join(KNOWLEDGE_ROOT, "lessons", "successes.json")
    if os.path.exists(success_path):
        with open(success_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            entries = [e for e in data.get("entries", []) if e.get("id") != "S000"]
            result["recent_successes"] = entries[-3:] if entries else []
            result["knowledge_loaded"]["successes"] = len(entries)
            best = data.get("best_practices", {}).get("items", [])
            if best:
                result["tips"].extend(best)

    # 실패 기록 로드
    failure_path = os.path.join(KNOWLEDGE_ROOT, "lessons", "failures.json")
    if os.path.exists(failure_path):
        with open(failure_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            entries = [e for e in data.get("entries", []) if e.get("id") != "F000"]
            result["knowledge_loaded"]["failures"] = len(entries)
            for entry in entries[-3:]:
                result["warnings"].append({
                    "cause": entry.get("cause"),
                    "prevention": entry.get("prevention")
                })

    # 활성 작업 로드
    try:
        from src.core import ContextManager
        ctx = ContextManager()
        result["active_tasks"] = ctx.list_active_tasks()
    except Exception:
        result["active_tasks"] = []

    return json.dumps(result, ensure_ascii=False, indent=2)


def list_sequences() -> str:
    """사용 가능한 시퀀스 목록"""
    seq_path = os.path.join(KNOWLEDGE_ROOT, "references", "example_sequences.json")
    if not os.path.exists(seq_path):
        return json.dumps({"error": "Sequences file not found"})

    with open(seq_path, 'r', encoding='utf-8') as f:
        sequences = json.load(f)

    result = [
        {"name": k, "description": v.get("description", "")}
        for k, v in sequences.items()
        if k not in ["version", "description"]
    ]
    return json.dumps(result, ensure_ascii=False, indent=2)


def get_sequence(name: str) -> str:
    """시퀀스 상세 조회"""
    seq_path = os.path.join(KNOWLEDGE_ROOT, "references", "example_sequences.json")
    if not os.path.exists(seq_path):
        return json.dumps({"error": "Sequences file not found"})

    with open(seq_path, 'r', encoding='utf-8') as f:
        sequences = json.load(f)

    if name not in sequences:
        return json.dumps({
            "error": f"Sequence '{name}' not found",
            "available": [k for k in sequences.keys() if k not in ["version", "description"]]
        })

    seq_data = sequences[name]
    steps = seq_data.get("sequence", [])

    result = {
        "sequence_name": name,
        "description": seq_data.get("description"),
        "total_steps": len(steps),
        "steps": [],
        "expected_result": seq_data.get("expected_result", {})
    }

    for step in steps:
        step_info = {
            "step": step.get("step"),
            "name": step.get("name"),
            "parallel": step.get("parallel", False),
            "mcp_calls": []
        }

        if "pre_action" in step:
            pre = step["pre_action"]
            step_info["mcp_calls"].append({
                "tool": f"mcp__stgen-dxf-viewer__{pre['tool']}",
                "args": pre["args"],
                "note": "pre_action"
            })

        for tool_item in step.get("tools", []):
            step_info["mcp_calls"].append({
                "tool": f"mcp__stgen-dxf-viewer__{tool_item['tool']}",
                "args": tool_item["args"],
                "comment": tool_item.get("comment", "")
            })

        result["steps"].append(step_info)

    return json.dumps(result, ensure_ascii=False, indent=2)


def get_pattern(pattern_name: str) -> str:
    """요소 패턴 조회"""
    patterns_path = os.path.join(KNOWLEDGE_ROOT, "patterns", "elements.json")
    if not os.path.exists(patterns_path):
        return json.dumps({"error": "Patterns file not found"})

    with open(patterns_path, 'r', encoding='utf-8') as f:
        patterns = json.load(f)

    if pattern_name not in patterns:
        return json.dumps({
            "error": f"Pattern '{pattern_name}' not found",
            "available": list(patterns.keys())
        })

    return json.dumps(patterns[pattern_name], ensure_ascii=False, indent=2)


def record_success(task: str, approach: str, key_factors: str,
                   entity_counts: str, tags: str, notes: str = "") -> str:
    """성공 기록 추가"""
    success_path = os.path.join(KNOWLEDGE_ROOT, "lessons", "successes.json")

    with open(success_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    entries = data.get("entries", [])
    existing_ids = [e.get("id", "S000") for e in entries]
    max_num = max([int(id[1:]) for id in existing_ids if id.startswith("S")], default=0)
    new_id = f"S{max_num + 1:03d}"

    new_entry = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "task": task,
        "context": "CLI 자동 기록",
        "approach": approach,
        "key_factors": [kf.strip() for kf in key_factors.split(",")],
        "result": {"entity_counts": json.loads(entity_counts)} if entity_counts else {},
        "efficiency_notes": notes,
        "reusable": True,
        "tags": [t.strip() for t in tags.split(",")]
    }

    entries.append(new_entry)
    data["entries"] = entries

    real_entries = [e for e in entries if e.get("id") != "S000"]
    data["statistics"]["total_count"] = len(real_entries)
    tag_counts = {}
    for e in real_entries:
        for tag in e.get("tags", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    data["statistics"]["by_tag"] = tag_counts
    data["statistics"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    with open(success_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return json.dumps({"success": True, "id": new_id})


def record_failure(task: str, error: str, cause: str,
                   solution: str, prevention: str, tags: str) -> str:
    """실패 기록 추가"""
    failure_path = os.path.join(KNOWLEDGE_ROOT, "lessons", "failures.json")

    with open(failure_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    entries = data.get("entries", [])
    existing_ids = [e.get("id", "F000") for e in entries]
    max_num = max([int(id[1:]) for id in existing_ids if id.startswith("F")], default=0)
    new_id = f"F{max_num + 1:03d}"

    new_entry = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "task": task,
        "context": "CLI 자동 기록",
        "error": error,
        "cause": cause,
        "solution": solution,
        "prevention": prevention,
        "tags": [t.strip() for t in tags.split(",")]
    }

    entries.append(new_entry)
    data["entries"] = entries

    real_entries = [e for e in entries if e.get("id") != "F000"]
    data["statistics"]["total_count"] = len(real_entries)
    tag_counts = {}
    for e in real_entries:
        for tag in e.get("tags", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    data["statistics"]["by_tag"] = tag_counts
    data["statistics"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    with open(failure_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return json.dumps({"success": True, "id": new_id})
