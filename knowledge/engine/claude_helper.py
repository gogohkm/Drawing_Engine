"""
Claude Helper - Claude Code 세션에서 직접 사용하는 헬퍼 함수들

이 파일의 함수들은 Claude가 세션 시작 시 또는 작업 중 호출하여
지식을 로드하고, 결과를 기록하는 데 사용합니다.

기능:
1. 세션 시작/지식 로드
2. 시퀀스 조회/실행
3. 성공/실패 기록
4. 맥락 관리 (Context Manager 연동)
   - 작업 생성/계획
   - 체크포인트 기록
   - 맥락 복구

사용 예시 (Claude가 Bash로 실행):
    python claude_helper.py session_start
    python claude_helper.py create_task copy_region "도면 복사"
    python claude_helper.py restore <task_id>
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# 경로 설정
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_ROOT = os.path.dirname(SCRIPT_DIR)

# Context Manager 임포트
try:
    from context_manager import ContextManager, CoordinateCalculator
    CONTEXT_AVAILABLE = True
except ImportError:
    CONTEXT_AVAILABLE = False


def session_start() -> str:
    """
    세션 시작 시 호출 - 지식 로드 및 요약 출력

    Returns:
        JSON 형태의 세션 브리핑
    """
    result = {
        "status": "ready",
        "timestamp": datetime.now().isoformat(),
        "knowledge_loaded": {},
        "available_sequences": [],
        "recent_successes": [],
        "warnings": [],
        "tips": [],
        "active_tasks": [],  # 진행 중인 작업
        "context_manager": CONTEXT_AVAILABLE
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

            # Best practices
            best = data.get("best_practices", {}).get("items", [])
            if best:
                result["tips"].extend(best)

    # 실패 기록 로드 - 경고로 변환
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

    # 활성 작업 로드 (Context Manager)
    if CONTEXT_AVAILABLE:
        try:
            ctx = ContextManager()
            result["active_tasks"] = ctx.list_active_tasks()
        except Exception as e:
            result["active_tasks"] = []
            result["warnings"].append({
                "cause": f"Context Manager error: {str(e)}",
                "prevention": "Check context_manager.py"
            })

    return json.dumps(result, ensure_ascii=False, indent=2)


def get_sequence_steps(sequence_name: str) -> str:
    """
    시퀀스의 실행 단계를 MCP 도구 호출 형태로 반환

    Args:
        sequence_name: 실행할 시퀀스 이름

    Returns:
        JSON 형태의 단계별 도구 호출 정보
    """
    seq_path = os.path.join(KNOWLEDGE_ROOT, "references", "example_sequences.json")

    if not os.path.exists(seq_path):
        return json.dumps({"error": "Sequences file not found"})

    with open(seq_path, 'r', encoding='utf-8') as f:
        sequences = json.load(f)

    if sequence_name not in sequences:
        return json.dumps({
            "error": f"Sequence '{sequence_name}' not found",
            "available": [k for k in sequences.keys() if k not in ["version", "description"]]
        })

    seq_data = sequences[sequence_name]
    steps = seq_data.get("sequence", [])

    result = {
        "sequence_name": sequence_name,
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

        # pre_action
        if "pre_action" in step:
            pre = step["pre_action"]
            step_info["mcp_calls"].append({
                "tool": f"mcp__stgen-dxf-viewer__{pre['tool']}",
                "args": pre["args"],
                "note": "pre_action - run first"
            })

        # main tools
        for tool_item in step.get("tools", []):
            step_info["mcp_calls"].append({
                "tool": f"mcp__stgen-dxf-viewer__{tool_item['tool']}",
                "args": tool_item["args"],
                "comment": tool_item.get("comment", "")
            })

        result["steps"].append(step_info)

    return json.dumps(result, ensure_ascii=False, indent=2)


def record_success(task: str, approach: str, key_factors: str,
                   entity_counts: str, tags: str, notes: str = "") -> str:
    """
    성공 기록 추가

    Args:
        task: 완료한 작업 설명
        approach: 사용한 접근법
        key_factors: 성공 요인 (쉼표 구분)
        entity_counts: 엔티티 카운트 JSON 문자열
        tags: 태그 (쉼표 구분)
        notes: 추가 메모

    Returns:
        생성된 기록 ID
    """
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
        "context": "Claude Helper 자동 기록",
        "approach": approach,
        "key_factors": [kf.strip() for kf in key_factors.split(",")],
        "result": {"entity_counts": json.loads(entity_counts)} if entity_counts else {},
        "efficiency_notes": notes,
        "reusable": True,
        "tags": [t.strip() for t in tags.split(",")]
    }

    entries.append(new_entry)
    data["entries"] = entries

    # 통계 업데이트
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
    """
    실패 기록 추가

    Args:
        task: 수행하려던 작업
        error: 발생한 에러
        cause: 근본 원인
        solution: 해결 방법
        prevention: 향후 예방책
        tags: 태그 (쉼표 구분)

    Returns:
        생성된 기록 ID
    """
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
        "context": "Claude Helper 자동 기록",
        "error": error,
        "cause": cause,
        "solution": solution,
        "prevention": prevention,
        "tags": [t.strip() for t in tags.split(",")]
    }

    entries.append(new_entry)
    data["entries"] = entries

    # 통계 업데이트
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


def get_element_pattern(element_type: str) -> str:
    """
    요소별 작도 패턴 조회

    Args:
        element_type: grid, wall, opening, dimension, etc.

    Returns:
        패턴 정보 JSON
    """
    elements_path = os.path.join(KNOWLEDGE_ROOT, "patterns", "elements.json")

    if not os.path.exists(elements_path):
        return json.dumps({"error": "Elements file not found"})

    with open(elements_path, 'r', encoding='utf-8') as f:
        elements = json.load(f)

    if element_type not in elements:
        return json.dumps({
            "error": f"Element type '{element_type}' not found",
            "available": [k for k in elements.keys() if k not in ["version", "description"]]
        })

    return json.dumps(elements[element_type], ensure_ascii=False, indent=2)


def list_all_sequences() -> str:
    """모든 시퀀스 목록과 설명"""
    seq_path = os.path.join(KNOWLEDGE_ROOT, "references", "example_sequences.json")

    if not os.path.exists(seq_path):
        return json.dumps({"error": "Sequences file not found"})

    with open(seq_path, 'r', encoding='utf-8') as f:
        sequences = json.load(f)

    result = []
    for name, data in sequences.items():
        if name in ["version", "description"]:
            continue
        result.append({
            "name": name,
            "description": data.get("description", ""),
            "drawing_type": data.get("drawing_type", ""),
            "verified": data.get("verified", False),
            "step_count": len(data.get("sequence", []))
        })

    return json.dumps(result, ensure_ascii=False, indent=2)


# ========== 맥락 관리 함수 (Context Manager 연동) ==========

def create_task(task_type: str, description: str, source_data: str = "{}") -> str:
    """
    새 작업 생성 - 복잡한 드로잉 작업 시작 전 호출

    Args:
        task_type: 작업 유형 (copy_region, draw_pattern, trace_drawing, etc.)
        description: 작업 설명
        source_data: 원본 데이터 JSON (선택사항)

    Returns:
        생성된 task_id
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        source = json.loads(source_data) if source_data else {}
        task_id = ctx.create_task(task_type, description, source)
        return json.dumps({
            "success": True,
            "task_id": task_id,
            "message": f"Task created. Use 'restore {task_id}' to check context."
        })
    except Exception as e:
        return json.dumps({"error": str(e)})


def set_task_plan(task_id: str, steps_json: str) -> str:
    """
    작업 실행 계획 설정

    Args:
        task_id: 작업 ID
        steps_json: 단계 목록 JSON
            [{"name": "...", "tools": [...], "parallel": bool}, ...]

    Returns:
        성공 여부
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        steps = json.loads(steps_json)
        ctx.set_execution_plan(task_id, steps)
        return json.dumps({
            "success": True,
            "task_id": task_id,
            "total_steps": len(steps)
        })
    except Exception as e:
        return json.dumps({"error": str(e)})


def save_coords(task_id: str, coords_json: str) -> str:
    """
    사전 계산된 좌표 저장

    Args:
        task_id: 작업 ID
        coords_json: 좌표 목록 JSON

    Returns:
        성공 여부
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        coords = json.loads(coords_json)
        ctx.set_calculated_coords(task_id, coords)
        return json.dumps({
            "success": True,
            "task_id": task_id,
            "coords_count": len(coords)
        })
    except Exception as e:
        return json.dumps({"error": str(e)})


def checkpoint(task_id: str, step: str, status: str,
               handles: str = "[]", result: str = "{}", error: str = "") -> str:
    """
    체크포인트 기록

    Args:
        task_id: 작업 ID
        step: 단계 번호 (문자열)
        status: 상태 (in_progress, completed, failed)
        handles: 생성된 엔티티 핸들 JSON 배열
        result: 결과 데이터 JSON
        error: 에러 메시지 (실패 시)

    Returns:
        성공 여부
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        entity_handles = json.loads(handles) if handles else []
        result_data = json.loads(result) if result else {}

        ctx.checkpoint(
            task_id=task_id,
            step=int(step),
            status=status,
            entity_handles=entity_handles,
            result=result_data,
            error=error if error else None
        )

        return json.dumps({
            "success": True,
            "task_id": task_id,
            "step": int(step),
            "status": status
        })
    except Exception as e:
        return json.dumps({"error": str(e)})


def restore(task_id: str) -> str:
    """
    맥락 복구 - 대화 중간에 맥락을 잃어버렸을 때 호출

    Args:
        task_id: 작업 ID

    Returns:
        복구된 컨텍스트 정보 (진행 상황, 남은 작업, 좌표 등)
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        context = ctx.restore_context(task_id)
        return json.dumps(context, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def get_remaining(task_id: str) -> str:
    """
    남은 MCP 호출 목록 조회

    Args:
        task_id: 작업 ID

    Returns:
        남은 도구 호출 목록
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        calls = ctx.get_remaining_calls(task_id)
        return json.dumps({
            "task_id": task_id,
            "remaining_count": len(calls),
            "calls": calls
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def get_step_tools(task_id: str, step: str) -> str:
    """
    특정 단계의 도구 호출 목록 조회

    Args:
        task_id: 작업 ID
        step: 단계 번호

    Returns:
        해당 단계의 도구 호출 목록
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        tools = ctx.get_step_tools(task_id, int(step))
        return json.dumps({
            "task_id": task_id,
            "step": int(step),
            "tools_count": len(tools),
            "tools": tools
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def list_tasks() -> str:
    """활성 작업 목록 조회"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        tasks = ctx.list_active_tasks()
        return json.dumps({
            "active_count": len(tasks),
            "tasks": tasks
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def detect_loss(task_id: str, claimed_step: str = "", claimed_entities: str = "") -> str:
    """
    맥락 손실 감지 - Claude가 자기 상태를 확인할 때 사용

    Args:
        task_id: 작업 ID
        claimed_step: 내가 인식하는 현재 단계 (선택)
        claimed_entities: 내가 인식하는 생성된 엔티티 수 (선택)

    Returns:
        감지 결과 + 자동 복구 필요 여부
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        current_state = {}

        if claimed_step:
            current_state['claimed_step'] = int(claimed_step)
        if claimed_entities:
            current_state['claimed_entities'] = int(claimed_entities)

        result = ctx.detect_context_loss(task_id, current_state)
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def auto_check(task_id: str, claimed_step: str = "", claimed_entities: str = "") -> str:
    """
    맥락 확인 및 필요시 자동 복구

    Claude가 작업 중간에 "내가 지금 뭘 하고 있었지?" 싶을 때 호출.
    맥락 손실이 감지되면 자동으로 복구된 컨텍스트 반환.

    Args:
        task_id: 작업 ID
        claimed_step: 내가 인식하는 현재 단계
        claimed_entities: 내가 인식하는 생성된 엔티티 수

    Returns:
        {
            "action": "none" | "auto_restored" | "manual_review",
            "message": "...",
            "restored_context": {...}  # 자동 복구된 경우
        }
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        current_state = {}

        if claimed_step:
            current_state['claimed_step'] = int(claimed_step)
        if claimed_entities:
            current_state['claimed_entities'] = int(claimed_entities)

        result = ctx.check_and_auto_restore(task_id, current_state)
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def health(task_id: str) -> str:
    """
    작업 컨텍스트 건강 상태 확인

    Args:
        task_id: 작업 ID

    Returns:
        현재 상태 요약
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        result = ctx.get_context_health(task_id)
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def create_task_auto(task_type: str, description: str, entities_json: str,
                     offset_dx: str, offset_dy: str, batch_size: str = "20") -> str:
    """
    엔티티 기반 자동 작업 생성 - create_task + set_execution_plan 통합

    엔티티 목록을 받아서:
    1. 작업 생성
    2. 좌표 변환 계산
    3. 배치 분할
    4. 실행 계획 자동 등록

    Args:
        task_type: 작업 유형 (redraw, copy_manual, etc.)
        description: 작업 설명
        entities_json: 엔티티 목록 JSON (get_selected_entities 결과)
        offset_dx: X 오프셋
        offset_dy: Y 오프셋
        batch_size: 배치 크기 (기본 20)

    Returns:
        {task_id, total_entities, total_steps, batches_info}
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        entities = json.loads(entities_json)
        target_offset = {"dx": float(offset_dx), "dy": float(offset_dy)}

        result = ctx.create_task_with_entities(
            task_type=task_type,
            description=description,
            entities=entities,
            target_offset=target_offset,
            batch_size=int(batch_size)
        )

        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def validate(task_id: str) -> str:
    """
    작업 실행 준비 상태 검증

    checkpoint 호출 전에 미리 문제점을 확인.

    Args:
        task_id: 작업 ID

    Returns:
        {valid: bool, issues: [...], suggestions: [...]}
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        result = ctx.validate_task_ready(task_id)
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def prepare_copy_task(task_id: str, entities_json: str,
                      base_x: str, base_y: str,
                      target_x: str, target_y: str) -> str:
    """
    영역 복사 작업 준비 - 좌표 계산 및 시퀀스 생성

    Args:
        task_id: 작업 ID
        entities_json: 원본 엔티티 목록 (extract_region 결과)
        base_x, base_y: 원본 기준점
        target_x, target_y: 목표 위치

    Returns:
        생성된 MCP 호출 목록
    """
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        ctx = ContextManager()
        entities = json.loads(entities_json)
        base_point = {"x": float(base_x), "y": float(base_y)}
        target_point = {"x": float(target_x), "y": float(target_y)}

        mcp_calls = ctx.generate_copy_sequence(task_id, entities, base_point, target_point)

        return json.dumps({
            "success": True,
            "task_id": task_id,
            "total_calls": len(mcp_calls),
            "calls": mcp_calls
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


# CLI 인터페이스
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python claude_helper.py <command> [args...]")
        print("")
        print("=== 기본 명령 ===")
        print("  session_start              - 세션 시작, 지식 로드")
        print("  get_sequence <name>        - 시퀀스 단계 조회")
        print("  list_sequences             - 시퀀스 목록")
        print("  get_pattern <type>         - 요소 패턴 조회")
        print("  record_success ...         - 성공 기록")
        print("  record_failure ...         - 실패 기록")
        print("")
        print("=== 맥락 관리 (Context Manager) ===")
        print("  create_task <type> <desc>  - 새 작업 생성 (수동)")
        print("  create_task_auto <type> <desc> <entities_json> <dx> <dy> [batch] - 자동 작업 생성")
        print("  validate <task_id>         - 실행 준비 상태 검증")
        print("  list_tasks                 - 활성 작업 목록")
        print("  restore <task_id>          - 맥락 복구")
        print("  checkpoint <id> <step> <status> - 체크포인트 기록")
        print("  get_remaining <task_id>    - 남은 호출 목록")
        print("  get_step_tools <id> <step> - 단계별 도구 목록")
        print("")
        print("=== 맥락 손실 감지 ===")
        print("  detect_loss <task_id> [step] [entities] - 맥락 손실 감지")
        print("  auto_check <task_id> [step] [entities]  - 자동 확인 및 복구")
        print("  health <task_id>                        - 건강 상태 확인")
        print("")
        print("=== 추천 워크플로우 ===")
        print("  1. create_task_auto - 엔티티와 오프셋으로 자동 계획 생성")
        print("  2. validate - 실행 전 준비 상태 확인")
        print("  3. checkpoint - 단계별 진행 기록")
        print("  4. auto_check - 맥락 손실 시 자동 복구")
        sys.exit(1)

    command = sys.argv[1]

    # 기본 명령
    if command == "session_start":
        print(session_start())
    elif command == "get_sequence" and len(sys.argv) > 2:
        print(get_sequence_steps(sys.argv[2]))
    elif command == "list_sequences":
        print(list_all_sequences())
    elif command == "get_pattern" and len(sys.argv) > 2:
        print(get_element_pattern(sys.argv[2]))

    # 맥락 관리 명령
    elif command == "create_task" and len(sys.argv) > 3:
        source_data = sys.argv[4] if len(sys.argv) > 4 else "{}"
        print(create_task(sys.argv[2], sys.argv[3], source_data))
    elif command == "create_task_auto" and len(sys.argv) > 6:
        batch_size = sys.argv[7] if len(sys.argv) > 7 else "20"
        print(create_task_auto(sys.argv[2], sys.argv[3], sys.argv[4],
                               sys.argv[5], sys.argv[6], batch_size))
    elif command == "validate" and len(sys.argv) > 2:
        print(validate(sys.argv[2]))
    elif command == "list_tasks":
        print(list_tasks())
    elif command == "restore" and len(sys.argv) > 2:
        print(restore(sys.argv[2]))
    elif command == "checkpoint" and len(sys.argv) > 4:
        handles = sys.argv[5] if len(sys.argv) > 5 else "[]"
        result = sys.argv[6] if len(sys.argv) > 6 else "{}"
        error = sys.argv[7] if len(sys.argv) > 7 else ""
        print(checkpoint(sys.argv[2], sys.argv[3], sys.argv[4], handles, result, error))
    elif command == "get_remaining" and len(sys.argv) > 2:
        print(get_remaining(sys.argv[2]))
    elif command == "get_step_tools" and len(sys.argv) > 3:
        print(get_step_tools(sys.argv[2], sys.argv[3]))

    # 맥락 손실 감지 명령
    elif command == "detect_loss" and len(sys.argv) > 2:
        claimed_step = sys.argv[3] if len(sys.argv) > 3 else ""
        claimed_entities = sys.argv[4] if len(sys.argv) > 4 else ""
        print(detect_loss(sys.argv[2], claimed_step, claimed_entities))
    elif command == "auto_check" and len(sys.argv) > 2:
        claimed_step = sys.argv[3] if len(sys.argv) > 3 else ""
        claimed_entities = sys.argv[4] if len(sys.argv) > 4 else ""
        print(auto_check(sys.argv[2], claimed_step, claimed_entities))
    elif command == "health" and len(sys.argv) > 2:
        print(health(sys.argv[2]))

    else:
        print(json.dumps({"error": f"Unknown command or missing args: {command}"}))
