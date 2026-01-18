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

# 공통 타입 임포트
try:
    from common import Point2D, Point3D, TaskStatus, MCPToolGenerator
    COMMON_AVAILABLE = True
except ImportError:
    COMMON_AVAILABLE = False

# Isometric Renderer 임포트
try:
    from isometric_renderer import (
        IsometricRenderer, SteelSection,
        draw_multi_bay_portal_frame, scale_for_canvas
    )
    # Point2D, Point3D는 common에서 임포트
    ISOMETRIC_AVAILABLE = True
except ImportError:
    ISOMETRIC_AVAILABLE = False

# Positional Line Extractor 임포트 (위치 기반 선 추출 - 사진→좌표)
try:
    from positional_line_extractor import (
        PositionalLineExtractor, MCPSequenceGenerator,
        ExtractionResult, PositionalLine, extract_and_draw
    )
    LINE_EXTRACTOR_AVAILABLE = True
except ImportError:
    LINE_EXTRACTOR_AVAILABLE = False

# Image Vectorizer 임포트 (vtracer 기반 이미지→벡터 변환)
try:
    from image_vectorizer import (
        ImageVectorizer, BinaryImage, GrayscaleImage, EdgeDetector,
        ContourTracer, PathSimplifier, write_lines_to_dxf,
        cli_vectorize, cli_vectorize_base64, cli_vectorize_base64_to_dxf,
        cli_info as vectorizer_info
    )
    IMAGE_VECTORIZER_AVAILABLE = True
except ImportError:
    IMAGE_VECTORIZER_AVAILABLE = False


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
        "context_manager": CONTEXT_AVAILABLE,
        "common_types": COMMON_AVAILABLE,
        "isometric_renderer": ISOMETRIC_AVAILABLE,
        "line_extractor": LINE_EXTRACTOR_AVAILABLE,
        "image_vectorizer": IMAGE_VECTORIZER_AVAILABLE
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


# ========== 이미지 분석 기능 ==========

def image_checklist() -> str:
    """
    이미지 분석 체크리스트 반환

    Claude가 이미지를 분석할 때 확인해야 할 항목들을 반환합니다.

    Returns:
        분석 체크리스트, 프롬프트, 흔한 실수 목록
    """
    if not IMAGE_ANALYZER_AVAILABLE:
        return json.dumps({"error": "Image Analyzer not available"})

    try:
        analyzer = ImageAnalyzer()
        return json.dumps(analyzer.get_analysis_checklist(), ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def image_prompt(stage: str) -> str:
    """
    단계별 이미지 분석 프롬프트 반환

    Args:
        stage: 분석 단계 (1, 2, 3)

    Returns:
        해당 단계의 분석 프롬프트
    """
    if not IMAGE_ANALYZER_AVAILABLE:
        return json.dumps({"error": "Image Analyzer not available"})

    try:
        analyzer = ImageAnalyzer()
        prompt = analyzer.get_analysis_prompt(int(stage))
        return json.dumps({"stage": int(stage), "prompt": prompt}, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def image_save_analysis(analysis_json: str) -> str:
    """
    이미지 분석 결과 저장

    Args:
        analysis_json: 분석 결과 JSON
            필수 필드:
            - structure_type: 구조 유형 (portal_frame_truss, simple_gable_frame 등)
            - width_height_ratio: 가로세로 비율
            - roof_pitch_degrees: 지붕 경사각
            - eave_height_ratio: 처마높이 비율
            - truss_panels: 트러스 패널 수
            - purlins_per_slope: 경사면당 퍼린 수
            - vertical_webs: 수직 웹부재 수
            - diagonal_webs: 대각 웹부재 수

    Returns:
        {success: true, analysis_id: "analysis_20260111_..."}
    """
    if not IMAGE_ANALYZER_AVAILABLE:
        return json.dumps({"error": "Image Analyzer not available"})

    try:
        analyzer = ImageAnalyzer()
        data = json.loads(analysis_json)
        analysis_id = analyzer.save_analysis(data)
        return json.dumps({
            "success": True,
            "analysis_id": analysis_id,
            "message": "분석 결과가 저장되었습니다. 다음 단계: image_coords로 좌표 계산"
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def image_coords(analysis_id: str, width: str = "800",
                 height: str = "500", margin: str = "50") -> str:
    """
    분석 결과 기반 좌표 계산

    Args:
        analysis_id: 분석 ID (image_save_analysis에서 반환됨)
        width: 캔버스 너비
        height: 캔버스 높이
        margin: 여백

    Returns:
        계산된 좌표 (기둥, 트러스, 퍼린, 가새 등)
    """
    if not IMAGE_ANALYZER_AVAILABLE:
        return json.dumps({"error": "Image Analyzer not available"})

    try:
        analyzer = ImageAnalyzer()
        analyzer.load_analysis(analysis_id)
        coords = analyzer.calculate_coordinates(
            float(width), float(height), float(margin)
        )
        return json.dumps(coords, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def image_sequence(analysis_id: str, detail_level: str = "L2_structural") -> str:
    """
    MCP 도구 호출 시퀀스 생성

    Args:
        analysis_id: 분석 ID
        detail_level: 상세 수준
            - L1_outline: 외곽선만
            - L2_structural: 구조 부재 (기본값)
            - L3_detailed: 상세 (볼트, 치수 등)

    Returns:
        단계별 MCP 도구 호출 시퀀스
    """
    if not IMAGE_ANALYZER_AVAILABLE:
        return json.dumps({"error": "Image Analyzer not available"})

    try:
        analyzer = ImageAnalyzer()
        analyzer.load_analysis(analysis_id)
        analyzer.calculate_coordinates()
        sequence = analyzer.generate_drawing_sequence(detail_level)
        return json.dumps({
            "analysis_id": analysis_id,
            "detail_level": detail_level,
            "total_steps": len(sequence),
            "sequence": sequence
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def image_draw_from_analysis(analysis_json: str, width: str = "800",
                              height: str = "500", margin: str = "50",
                              detail_level: str = "L2_structural") -> str:
    """
    분석 → 좌표 계산 → 시퀀스 생성을 한 번에 수행

    Claude가 이미지 분석 후 바로 실행할 수 있는 시퀀스를 생성합니다.

    Args:
        analysis_json: 분석 결과 JSON
        width, height, margin: 캔버스 설정
        detail_level: 상세 수준

    Returns:
        실행 가능한 전체 시퀀스
    """
    if not IMAGE_ANALYZER_AVAILABLE:
        return json.dumps({"error": "Image Analyzer not available"})

    try:
        analyzer = ImageAnalyzer()
        data = json.loads(analysis_json)

        # 1. 분석 결과 저장
        analysis_id = analyzer.save_analysis(data)

        # 2. 좌표 계산
        coords = analyzer.calculate_coordinates(
            float(width), float(height), float(margin)
        )

        # 3. 시퀀스 생성
        sequence = analyzer.generate_drawing_sequence(detail_level)

        return json.dumps({
            "success": True,
            "analysis_id": analysis_id,
            "canvas": {
                "width": float(width),
                "height": float(height),
                "margin": float(margin)
            },
            "detail_level": detail_level,
            "total_steps": len(sequence),
            "total_tools": sum(len(s.get("tools", [])) for s in sequence),
            "sequence": sequence,
            "key_coordinates": {
                "left_x": coords["bounds"]["left_x"],
                "right_x": coords["bounds"]["right_x"],
                "bottom_y": coords["bounds"]["bottom_y"],
                "eave_y": coords["roof"]["eave_y"],
                "ridge_y": coords["roof"]["ridge_y"]
            }
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


# ========== 등각투상(Isometric) 렌더링 ==========

def iso_portal(num_bays: str = "2", bay_width: str = "6000",
               depth: str = "20000", eave_height: str = "6000",
               ridge_height: str = "7500", purlin_count: str = "6",
               canvas_width: str = "800", canvas_height: str = "500") -> str:
    """
    등각투상(isometric) 뷰로 다중 베이 포털 프레임 건물 그리기

    사진과 유사한 3D 뷰를 생성합니다.

    Args:
        num_bays: 베이(스팬) 수 (기본: 2)
        bay_width: 베이 폭 mm (기본: 6000)
        depth: 건물 깊이 mm (기본: 20000)
        eave_height: 처마 높이 mm (기본: 6000)
        ridge_height: 용마루 높이 mm (기본: 7500)
        purlin_count: 경사면당 퍼린 수 (기본: 6)
        canvas_width: 캔버스 너비 (기본: 800)
        canvas_height: 캔버스 높이 (기본: 500)

    Returns:
        MCP 도구 호출 시퀀스 JSON
    """
    if not ISOMETRIC_AVAILABLE:
        return json.dumps({"error": "Isometric Renderer not available"})

    try:
        # 파라미터 변환
        n_bays = int(num_bays)
        b_width = float(bay_width)
        b_depth = float(depth)
        e_height = float(eave_height)
        r_height = float(ridge_height)
        p_count = int(purlin_count)
        c_width = float(canvas_width)
        c_height = float(canvas_height)

        # 스케일 및 원점 계산
        total_width = b_width * n_bays
        scale, origin = scale_for_canvas(total_width, r_height, c_width, c_height, 50)

        # 렌더러 생성
        renderer = IsometricRenderer(angle=30, scale=scale, origin=origin)

        # 포털 프레임 그리기
        elements = draw_multi_bay_portal_frame(
            renderer=renderer,
            num_bays=n_bays,
            bay_width=b_width,
            building_depth=b_depth,
            eave_height=e_height,
            ridge_height=r_height,
            purlin_count=p_count
        )

        # MCP 명령 생성
        commands = renderer.get_mcp_commands()

        # 레이어별로 그룹화
        layers_setup = [
            {"tool": "create_layer", "args": {"name": "COLUMN", "color": 7}},
            {"tool": "create_layer", "args": {"name": "BEAM", "color": 4}},
            {"tool": "create_layer", "args": {"name": "PURLIN", "color": 3}},
            {"tool": "create_layer", "args": {"name": "BRACING", "color": 5}}
        ]

        # 시퀀스 구성
        sequence = [
            {
                "step": 1,
                "name": "레이어 생성",
                "tools": layers_setup,
                "parallel": True
            },
            {
                "step": 2,
                "name": "등각투상 도면 그리기",
                "description": f"총 {len(commands)}개 LINE 생성",
                "tools": [
                    {
                        "tool": "create_line",
                        "args": {
                            "start": cmd["start"],
                            "end": cmd["end"],
                            "layer": cmd.get("layer", "0")
                        }
                    }
                    for cmd in commands
                ],
                "parallel": True
            }
        ]

        return json.dumps({
            "success": True,
            "view_type": "isometric",
            "projection_angle": 30,
            "scale": scale,
            "origin": {"x": origin.x, "y": origin.y},
            "building_params": {
                "num_bays": n_bays,
                "bay_width": b_width,
                "depth": b_depth,
                "eave_height": e_height,
                "ridge_height": r_height
            },
            "elements_summary": elements,
            "total_lines": len(commands),
            "sequence": sequence
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def iso_h_beam(start_x: str, start_y: str, start_z: str,
               end_x: str, end_y: str, end_z: str,
               height: str = "400", width: str = "200",
               layer: str = "COLUMN") -> str:
    """
    등각투상 뷰로 H형강 부재 그리기

    Args:
        start_x, start_y, start_z: 시작점 3D 좌표
        end_x, end_y, end_z: 끝점 3D 좌표
        height: H형강 높이 mm (기본: 400)
        width: H형강 폭 mm (기본: 200)
        layer: 레이어 이름

    Returns:
        MCP 도구 호출 시퀀스 JSON
    """
    if not ISOMETRIC_AVAILABLE:
        return json.dumps({"error": "Isometric Renderer not available"})

    try:
        renderer = IsometricRenderer(angle=30, scale=0.05)
        section = SteelSection.h_beam(float(height), float(width))

        start = Point3D(float(start_x), float(start_y), float(start_z))
        end = Point3D(float(end_x), float(end_y), float(end_z))

        renderer.draw_h_beam_segment(start, end, section, layer)
        commands = renderer.get_mcp_commands()

        return json.dumps({
            "success": True,
            "section": f"H-{height}x{width}",
            "total_lines": len(commands),
            "tools": [
                {
                    "tool": "create_line",
                    "args": {
                        "start": cmd["start"],
                        "end": cmd["end"],
                        "layer": cmd.get("layer", "0")
                    }
                }
                for cmd in commands
            ]
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def iso_purlin_array(start_x: str, start_y: str, start_z: str,
                     end_x: str, end_y: str, end_z: str,
                     count: str, purlin_length: str,
                     layer: str = "PURLIN") -> str:
    """
    등각투상 뷰로 퍼린 배열 그리기

    경사 보(래프터)를 따라 퍼린을 등간격으로 배치합니다.
    퍼린은 깊이(Z) 방향으로 연장됩니다.

    Args:
        start_x, start_y, start_z: 래프터 시작점
        end_x, end_y, end_z: 래프터 끝점
        count: 퍼린 개수
        purlin_length: 퍼린 길이 (깊이 방향)
        layer: 레이어 이름

    Returns:
        MCP 도구 호출 시퀀스 JSON
    """
    if not ISOMETRIC_AVAILABLE:
        return json.dumps({"error": "Isometric Renderer not available"})

    try:
        renderer = IsometricRenderer(angle=30, scale=0.05)
        section = SteelSection.c_channel(150, 75)

        rafter_start = Point3D(float(start_x), float(start_y), float(start_z))
        rafter_end = Point3D(float(end_x), float(end_y), float(end_z))

        renderer.draw_purlin_array(
            rafter_start, rafter_end,
            int(count), float(purlin_length),
            section, layer
        )
        commands = renderer.get_mcp_commands()

        return json.dumps({
            "success": True,
            "purlin_count": int(count),
            "purlin_length": float(purlin_length),
            "total_lines": len(commands),
            "tools": [
                {
                    "tool": "create_line",
                    "args": {
                        "start": cmd["start"],
                        "end": cmd["end"],
                        "layer": cmd.get("layer", "0")
                    }
                }
                for cmd in commands
            ]
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def iso_project(x: str, y: str, z: str, angle: str = "30", scale: str = "1.0") -> str:
    """
    3D 좌표를 2D 등각투상 좌표로 변환

    Args:
        x, y, z: 3D 좌표
        angle: 투상 각도 (기본: 30)
        scale: 스케일 (기본: 1.0)

    Returns:
        2D 좌표 {x_2d, y_2d}
    """
    if not ISOMETRIC_AVAILABLE:
        return json.dumps({"error": "Isometric Renderer not available"})

    try:
        renderer = IsometricRenderer(angle=float(angle), scale=float(scale))
        x_2d, y_2d = renderer.project_point(float(x), float(y), float(z))

        return json.dumps({
            "input_3d": {"x": float(x), "y": float(y), "z": float(z)},
            "output_2d": {"x": x_2d, "y": y_2d},
            "projection_angle": float(angle),
            "scale": float(scale)
        })
    except Exception as e:
        return json.dumps({"error": str(e)})


def iso_template_info() -> str:
    """
    등각투상 템플릿 정보 반환

    사용 가능한 템플릿과 파라미터 정보를 반환합니다.

    Returns:
        템플릿 정보 JSON
    """
    templates_path = os.path.join(KNOWLEDGE_ROOT, "patterns", "structure_templates.json")

    try:
        with open(templates_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 3D/등각투상 템플릿만 추출
        iso_templates = {}
        for name, template in data.get("templates", {}).items():
            if template.get("view_type") == "isometric" or "3d" in name.lower():
                iso_templates[name] = {
                    "name": template.get("name"),
                    "description": template.get("description"),
                    "default_dimensions": template.get("default_dimensions", {}),
                    "typical_elements": template.get("typical_elements", {})
                }

        return json.dumps({
            "isometric_available": ISOMETRIC_AVAILABLE,
            "projection_info": {
                "default_angle": 30,
                "coordinate_system": {
                    "x": "left-right (horizontal)",
                    "y": "up-down (vertical)",
                    "z": "front-back (depth)"
                }
            },
            "templates": iso_templates,
            "commands": [
                "iso_portal - 다중 베이 포털 프레임 그리기",
                "iso_h_beam - H형강 부재 그리기",
                "iso_purlin_array - 퍼린 배열 그리기",
                "iso_project - 3D→2D 좌표 변환"
            ]
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


# ========== 2D 뷰 렌더링 (사진→2D 도면 변환) ==========

def view2d_from_photo(analysis_json: str, width: str = "800",
                       origin_x: str = "50", origin_y: str = "50") -> str:
    """
    사진 분석 결과를 바탕으로 2D 정면도 생성

    이 함수는 사진에서 추출한 비율 정보를 바탕으로
    사진과 동일한 모습의 2D 도면을 생성합니다.

    **핵심 개념**:
    - 3D 투영이 아닌, 사진에서 "보이는 그대로"를 2D로 재현
    - 비율 기반 좌표 계산으로 정확한 배치
    - 반복 요소(기둥, 퍼린, 트러스) 자동 등간격 배치

    Args:
        analysis_json: 사진 분석 결과 JSON
            필수 필드:
            - width_height_ratio: 가로:세로 비율 (예: 2.5)
            - roof_pitch_degrees: 지붕 경사각 (예: 10)
            - eave_height_ratio: 처마높이/전체높이 (예: 0.7)
            - column_count: 기둥 개수
            - truss_panel_count: 트러스 패널 수
            - purlin_count_per_slope: 경사면당 퍼린 수
            - truss_type: 트러스 유형 (warren/pratt/howe)

        width: 도면 전체 폭 (기본: 800)
        origin_x: 시작 X 좌표 (기본: 50)
        origin_y: 시작 Y 좌표 (기본: 50)

    Returns:
        MCP 도구 호출 시퀀스 JSON

    예시:
        view2d_from_photo '{"width_height_ratio": 2.5, "roof_pitch_degrees": 8, ...}'
    """
    if not VIEW2D_AVAILABLE:
        return json.dumps({"error": "View 2D Renderer not available"})

    try:
        data = json.loads(analysis_json)

        # 렌더러 생성
        renderer = create_drawing_from_photo_analysis(
            data,
            total_width=float(width),
            origin_x=float(origin_x),
            origin_y=float(origin_y)
        )

        # 도면 생성
        result = renderer.draw_complete_elevation(
            include_truss=data.get("include_truss", True),
            include_purlins=data.get("include_purlins", True),
            include_bracing=data.get("include_bracing", True)
        )

        # MCP 명령 시퀀스 구성
        commands = renderer.get_mcp_commands()

        # 레이어별로 그룹화
        layer_groups = {}
        for cmd in commands:
            layer = cmd.get("layer", "0")
            if layer not in layer_groups:
                layer_groups[layer] = []
            layer_groups[layer].append(cmd)

        # 시퀀스 구성
        sequence = [
            {
                "step": 1,
                "name": "레이어 생성",
                "tools": [
                    {"tool": "create_layer", "args": {"name": "COLUMN", "color": 7}},
                    {"tool": "create_layer", "args": {"name": "BEAM", "color": 4}},
                    {"tool": "create_layer", "args": {"name": "TRUSS", "color": 6}},
                    {"tool": "create_layer", "args": {"name": "PURLIN", "color": 3}},
                    {"tool": "create_layer", "args": {"name": "BRACING", "color": 5}},
                    {"tool": "create_layer", "args": {"name": "FOUNDATION", "color": 8}}
                ],
                "parallel": True
            }
        ]

        step_num = 2
        for layer, layer_cmds in layer_groups.items():
            sequence.append({
                "step": step_num,
                "name": f"{layer} 레이어 그리기",
                "tools": [
                    {
                        "tool": "create_line",
                        "args": {
                            "start": cmd["start"],
                            "end": cmd["end"],
                            "layer": cmd.get("layer", "0")
                        }
                    }
                    for cmd in layer_cmds
                ],
                "parallel": True
            })
            step_num += 1

        # 계산된 주요 좌표
        key_points = renderer.calculate_key_points()

        return json.dumps({
            "success": True,
            "view_type": "2d_elevation",
            "description": "사진과 동일한 2D 정면도",
            "canvas": {
                "width": float(width),
                "origin_x": float(origin_x),
                "origin_y": float(origin_y)
            },
            "proportions_used": {
                "width_height_ratio": renderer.proportions.width_height_ratio,
                "roof_pitch_ratio": renderer.proportions.roof_pitch_ratio,
                "eave_height_ratio": renderer.proportions.eave_height_ratio,
                "column_count": renderer.proportions.column_count,
                "truss_type": renderer.proportions.truss_type
            },
            "key_coordinates": {
                "bottom_left": key_points["bottom_left"].to_dict(),
                "bottom_right": key_points["bottom_right"].to_dict(),
                "eave_left": key_points["eave_left"].to_dict(),
                "eave_right": key_points["eave_right"].to_dict(),
                "ridge": key_points["ridge"].to_dict()
            },
            "elements_summary": result["elements"],
            "total_entities": result["total_entities"],
            "sequence": sequence
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def view2d_calculate_coords(analysis_json: str, width: str = "800",
                             origin_x: str = "50", origin_y: str = "50") -> str:
    """
    사진 분석 결과에서 주요 좌표 계산

    도면을 그리기 전에 주요 좌표를 미리 확인할 수 있습니다.

    Args:
        analysis_json: 사진 분석 결과 JSON
        width: 도면 전체 폭
        origin_x, origin_y: 시작 좌표

    Returns:
        계산된 좌표 정보
    """
    if not VIEW2D_AVAILABLE:
        return json.dumps({"error": "View 2D Renderer not available"})

    try:
        data = json.loads(analysis_json)

        renderer = create_drawing_from_photo_analysis(
            data,
            total_width=float(width),
            origin_x=float(origin_x),
            origin_y=float(origin_y)
        )

        key_points = renderer.calculate_key_points()
        column_xs = renderer.calculate_column_positions()

        # 퍼린 위치 계산
        left_purlins = renderer.calculate_purlin_positions(
            key_points["eave_left"],
            key_points["ridge"],
            renderer.proportions.purlin_count_per_slope
        )

        return json.dumps({
            "success": True,
            "key_points": {
                "bottom_left": key_points["bottom_left"].to_dict(),
                "bottom_right": key_points["bottom_right"].to_dict(),
                "bottom_center": key_points["bottom_center"].to_dict(),
                "eave_left": key_points["eave_left"].to_dict(),
                "eave_right": key_points["eave_right"].to_dict(),
                "ridge": key_points["ridge"].to_dict()
            },
            "column_positions": column_xs,
            "purlin_positions_left": [p.to_dict() for p in left_purlins],
            "calculated_dimensions": {
                "total_width": float(width),
                "calculated_height": key_points["ridge"].y - key_points["bottom_left"].y,
                "eave_height": key_points["eave_left"].y - key_points["bottom_left"].y,
                "ridge_height": key_points["ridge"].y - key_points["bottom_left"].y
            }
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def view2d_truss_only(analysis_json: str, side: str = "left",
                       width: str = "800", origin_x: str = "50",
                       origin_y: str = "50") -> str:
    """
    트러스만 그리기

    지정된 측면의 트러스 구조만 생성합니다.

    Args:
        analysis_json: 사진 분석 결과 JSON
        side: "left" 또는 "right"
        width, origin_x, origin_y: 캔버스 설정

    Returns:
        트러스 MCP 도구 호출 시퀀스
    """
    if not VIEW2D_AVAILABLE:
        return json.dumps({"error": "View 2D Renderer not available"})

    try:
        data = json.loads(analysis_json)

        renderer = create_drawing_from_photo_analysis(
            data,
            total_width=float(width),
            origin_x=float(origin_x),
            origin_y=float(origin_y)
        )

        renderer.calculate_key_points()
        counts = renderer.draw_truss_frame(side)

        commands = renderer.get_mcp_commands()

        return json.dumps({
            "success": True,
            "side": side,
            "truss_type": renderer.proportions.truss_type,
            "element_counts": counts,
            "total_lines": len(commands),
            "tools": [
                {
                    "tool": "create_line",
                    "args": {
                        "start": cmd["start"],
                        "end": cmd["end"],
                        "layer": cmd.get("layer", "TRUSS")
                    }
                }
                for cmd in commands
            ]
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def view2d_info() -> str:
    """
    2D 뷰 렌더러 정보 및 사용법 반환

    Returns:
        사용 가능한 명령과 파라미터 정보
    """
    return json.dumps({
        "view_2d_available": VIEW2D_AVAILABLE,
        "description": "사진을 보고 똑같은 2D 도면을 그리는 기능",
        "core_concept": {
            "NOT": "3D 좌표를 2D로 투영하는 것",
            "YES": "사진에서 보이는 그대로를 2D 선으로 재현",
            "method": "비율 기반 좌표 계산 + 반복 요소 등간격 배치"
        },
        "workflow": [
            "1. 사진 분석: 비율, 요소 개수 추출",
            "2. view2d_calculate_coords: 좌표 미리보기",
            "3. view2d_from_photo: 전체 도면 생성",
            "4. MCP 도구 호출 실행"
        ],
        "required_analysis_fields": {
            "width_height_ratio": "가로:세로 비율 (예: 2.5 = 가로가 세로의 2.5배)",
            "roof_pitch_degrees": "지붕 경사각 (도)",
            "eave_height_ratio": "처마높이/전체높이 (예: 0.7 = 70%)",
            "column_count": "기둥 개수",
            "truss_panel_count": "트러스 패널 수 (상현재 분할 수)",
            "purlin_count_per_slope": "한쪽 경사면의 퍼린 수",
            "truss_type": "warren, pratt, howe 중 선택"
        },
        "optional_fields": {
            "has_bracing": "가새 포함 여부 (기본: true)",
            "include_truss": "트러스 포함 여부 (기본: true)",
            "include_purlins": "퍼린 포함 여부 (기본: true)"
        },
        "commands": [
            "view2d_from_photo - 사진 분석 결과로 전체 2D 도면 생성",
            "view2d_calculate_coords - 주요 좌표 미리 계산",
            "view2d_truss_only - 트러스만 그리기",
            "view2d_info - 이 도움말"
        ],
        "example_analysis": {
            "width_height_ratio": 2.5,
            "roof_pitch_degrees": 8,
            "eave_height_ratio": 0.72,
            "column_count": 4,
            "truss_panel_count": 10,
            "purlin_count_per_slope": 6,
            "truss_type": "pratt",
            "has_bracing": True
        }
    }, ensure_ascii=False, indent=2)


# ========== Positional Line Extractor (위치 기반 선 추출) ==========

def line_extract(image_path: str, min_length: str = "30",
                 use_lsd: str = "true") -> str:
    """
    이미지에서 모든 선을 위치 기반으로 추출

    **핵심 철학**:
    - 선을 "기둥", "보" 등으로 분류하지 않음
    - 순수하게 "위치"만 기록 (사진의 어느 영역에 있는지)
    - 모든 선을 빠짐없이 추출하는 것이 목표

    Args:
        image_path: 이미지 파일 경로
        min_length: 최소 선 길이 (픽셀, 기본: 30)
        use_lsd: LSD 알고리즘 사용 여부 (기본: true)

    Returns:
        추출된 선 정보 JSON:
        - total_lines: 총 선 개수
        - lines_by_region: 영역별 선 개수
        - lines_by_orientation: 방향별 선 개수
        - lines: 각 선의 상세 정보
            - id: 선 ID
            - start_px, end_px: 픽셀 좌표
            - start_norm, end_norm: 정규화 좌표 (0~1)
            - start_region, end_region: 영역 (예: "top-left", "middle-center")
            - orientation: 방향 (horizontal, vertical, diagonal-up, diagonal-down)
            - position_description: 위치 설명
    """
    if not LINE_EXTRACTOR_AVAILABLE:
        return json.dumps({"error": "Line Extractor not available. Install OpenCV: pip install opencv-python"})

    try:
        extractor = PositionalLineExtractor(min_line_length=int(min_length))

        if use_lsd.lower() == "true":
            result = extractor.extract_lines_lsd(image_path)
        else:
            result = extractor.extract_lines(image_path)

        return json.dumps({
            "success": True,
            "image_path": image_path,
            "image_size": {"width": result.image_width, "height": result.image_height},
            "total_lines": result.total_lines,
            "lines_by_region": result.lines_by_region,
            "lines_by_orientation": result.lines_by_orientation,
            "lines": [line.to_dict() for line in result.lines[:50]],  # 처음 50개만 출력
            "note": f"Showing first 50 of {result.total_lines} lines" if result.total_lines > 50 else None
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def line_extract_to_mcp(image_path: str, drawing_width: str = "1000",
                        drawing_height: str = "600", min_length: str = "30",
                        use_lsd: str = "true", by_region: str = "true") -> str:
    """
    이미지에서 선을 추출하고 MCP 시퀀스로 변환

    추출된 모든 선을 DXF 도면으로 그릴 수 있는 MCP 명령어 시퀀스를 생성합니다.

    Args:
        image_path: 이미지 파일 경로
        drawing_width: 도면 너비 (기본: 1000)
        drawing_height: 도면 높이 (기본: 600)
        min_length: 최소 선 길이 (픽셀, 기본: 30)
        use_lsd: LSD 알고리즘 사용 여부 (기본: true)
        by_region: 영역별 레이어 분리 (기본: true)
            - true: 각 영역(top-left, middle-center 등)을 별도 레이어에 배치
            - false: 모든 선을 단일 레이어에 배치

    Returns:
        MCP 시퀀스 JSON:
        - total_lines: 추출된 선 개수
        - total_commands: MCP 명령어 수
        - sequence: 실행할 MCP 명령어 목록
    """
    if not LINE_EXTRACTOR_AVAILABLE:
        return json.dumps({"error": "Line Extractor not available. Install OpenCV: pip install opencv-python"})

    try:
        extractor = PositionalLineExtractor(min_line_length=int(min_length))

        if use_lsd.lower() == "true":
            result = extractor.extract_lines_lsd(image_path)
        else:
            result = extractor.extract_lines(image_path)

        generator = MCPSequenceGenerator(
            drawing_width=float(drawing_width),
            drawing_height=float(drawing_height)
        )

        if by_region.lower() == "true":
            mcp_sequence = generator.generate_region_based_mcp(result)
        else:
            mcp_sequence = generator.generate_mcp_sequence(result)

        return json.dumps({
            "success": True,
            "image_path": image_path,
            "image_size": {"width": result.image_width, "height": result.image_height},
            "drawing_size": {"width": float(drawing_width), "height": float(drawing_height)},
            "total_lines": result.total_lines,
            "total_commands": len(mcp_sequence),
            "lines_by_region": result.lines_by_region,
            "lines_by_orientation": result.lines_by_orientation,
            "sequence": mcp_sequence
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def line_extract_save(image_path: str, output_json: str,
                      drawing_width: str = "1000", drawing_height: str = "600",
                      min_length: str = "30") -> str:
    """
    이미지에서 선을 추출하고 JSON 파일로 저장

    Args:
        image_path: 이미지 파일 경로
        output_json: 출력 JSON 파일 경로
        drawing_width: 도면 너비
        drawing_height: 도면 높이
        min_length: 최소 선 길이

    Returns:
        저장 결과 JSON
    """
    if not LINE_EXTRACTOR_AVAILABLE:
        return json.dumps({"error": "Line Extractor not available. Install OpenCV: pip install opencv-python"})

    try:
        result, mcp_sequence = extract_and_draw(
            image_path=image_path,
            output_json=output_json,
            drawing_width=float(drawing_width),
            drawing_height=float(drawing_height),
            min_line_length=int(min_length)
        )

        return json.dumps({
            "success": True,
            "output_file": output_json,
            "total_lines": result.total_lines,
            "total_commands": len(mcp_sequence),
            "lines_by_region": result.lines_by_region,
            "message": f"결과가 {output_json}에 저장되었습니다."
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def line_info() -> str:
    """
    위치 기반 선 추출기 정보 및 사용법

    Returns:
        사용 가능한 명령과 핵심 개념 설명
    """
    return json.dumps({
        "line_extractor_available": LINE_EXTRACTOR_AVAILABLE,
        "description": "사진에서 모든 선을 위치 기반으로 추출 (분류 없이)",
        "core_philosophy": {
            "DO_NOT": "선을 '기둥', '보', '퍼린'으로 분류",
            "DO": "선의 위치만 기록 (상단, 하단, 좌측, 우측 등)",
            "GOAL": "빠지는 선 없이 모든 선을 추출"
        },
        "position_context": {
            "regions": [
                "top-left", "top-center", "top-right",
                "middle-left", "middle-center", "middle-right",
                "bottom-left", "bottom-center", "bottom-right"
            ],
            "orientations": [
                "horizontal (0°~15° or 165°~180°)",
                "vertical (75°~105°)",
                "diagonal-up (15°~75°)",
                "diagonal-down (105°~165°)"
            ]
        },
        "workflow": [
            "1. line_extract <image_path> - 선 추출 및 분석",
            "2. line_extract_to_mcp <image_path> - MCP 시퀀스 생성",
            "3. MCP 도구 호출 실행 - DXF에 선 그리기"
        ],
        "commands": [
            "line_info - 이 도움말",
            "line_extract <path> [min_len] [use_lsd] - 선 추출",
            "line_extract_to_mcp <path> [width] [height] [min_len] [use_lsd] [by_region] - MCP 생성",
            "line_extract_save <path> <output> [width] [height] [min_len] - JSON 저장"
        ],
        "example_output": {
            "line": {
                "id": 42,
                "start_px": [150, 200],
                "end_px": [350, 200],
                "start_norm": [0.15, 0.33],
                "end_norm": [0.35, 0.33],
                "start_region": "top-left",
                "end_region": "top-center",
                "orientation": "horizontal",
                "position_description": "top-left to top-center, horizontal"
            }
        },
        "tips": [
            "min_length를 조절하여 노이즈 필터링",
            "use_lsd=true가 더 정확한 결과를 제공",
            "by_region=true로 영역별 레이어 분리 가능"
        ]
    }, ensure_ascii=False, indent=2)


# ============ Image Vectorizer 함수 (vtracer 기반) ============

def vectorize_info() -> str:
    """
    Image Vectorizer 정보 및 사용법

    vtracer 알고리즘 기반 이미지→벡터 변환 엔진
    """
    if not IMAGE_VECTORIZER_AVAILABLE:
        return json.dumps({
            "error": "Image Vectorizer not available",
            "available": False
        })

    return vectorizer_info()


def vectorize(image_path: str, bg_json: str, options_json: str = "{}") -> str:
    """
    이미지 파일을 벡터화하여 MCP 시퀀스 생성

    Args:
        image_path: 이미지 파일 경로
        bg_json: 배경 영역 {"x":-73,"y":-77,"width":178,"height":100}
        options_json: 옵션 JSON
            - mode: 'binary' (이진화), 'edge' (Sobel), 'edge_simple'
            - threshold: 이진화 임계값 (기본: 128)
            - edge_threshold: 엣지 감지 임계값 (기본: 50)
            - epsilon: 단순화 오차 (기본: 2.0)
            - min_length: 최소 윤곽선 길이 (기본: 10)
            - min_area: 최소 연결 요소 크기 (기본: 16)
            - layer: 출력 레이어 이름 (기본: TRACE)

    Returns:
        MCP 시퀀스 JSON
    """
    if not IMAGE_VECTORIZER_AVAILABLE:
        return json.dumps({
            "error": "Image Vectorizer not available. Check import errors.",
            "tip": "PPM/PGM 형식은 의존성 없이 사용 가능"
        })

    return cli_vectorize(image_path, bg_json, options_json)


def vectorize_base64(base64_data: str, bg_json: str, options_json: str = "{}") -> str:
    """
    Base64 이미지를 벡터화하여 MCP 시퀀스 생성

    Args:
        base64_data: Base64 인코딩된 이미지 데이터
        bg_json: 배경 영역
        options_json: 옵션 JSON

    Returns:
        MCP 시퀀스 JSON
    """
    if not IMAGE_VECTORIZER_AVAILABLE:
        return json.dumps({
            "error": "Image Vectorizer not available",
            "tip": "image_vectorizer.py를 확인하세요"
        })

    return cli_vectorize_base64(base64_data, bg_json, options_json)


def vectorize_base64_to_dxf(base64_data: str, bg_json: str, dxf_path: str, options_json: str = "{}") -> str:
    """
    Base64 이미지를 벡터화하여 DXF 파일에 직접 저장 (빠른 배치 처리)

    PIL 없이 순수 Python으로 PNG/JPEG 디코딩 가능

    Args:
        base64_data: Base64 인코딩된 이미지 데이터 (PNG 또는 JPEG)
        bg_json: 배경 영역 {"x":..., "y":..., "width":..., "height":...}
        dxf_path: 저장할 DXF 파일 경로
        options_json: 옵션 JSON
            - mode: 'binary' (이진화, 기본) 또는 'edge' (엣지 감지)
            - threshold: 이진화 임계값 (기본 200, 흑백 도면용)
            - epsilon: 단순화 허용 오차 (기본 1.0)
            - min_length: 최소 윤곽선 길이 (기본 5)
            - layer: 출력 레이어 이름 (기본 TRACE)

    Returns:
        결과 JSON (추가된 선 수, 소요 시간 등)
    """
    if not IMAGE_VECTORIZER_AVAILABLE:
        return json.dumps({
            "error": "Image Vectorizer not available",
            "tip": "image_vectorizer.py를 확인하세요"
        })

    return cli_vectorize_base64_to_dxf(base64_data, bg_json, dxf_path, options_json)


def save_base64_to_png(base64_data: str, output_path: str) -> str:
    """
    Base64 이미지를 PNG 파일로 저장 (PIL 불필요)

    Args:
        base64_data: Base64 인코딩된 이미지 (data:image/png;base64,... 형식 포함 가능)
        output_path: 저장할 PNG 파일 경로

    Returns:
        결과 JSON
    """
    import base64

    try:
        # data:image/png;base64, 접두어 제거
        if ',' in base64_data:
            base64_data = base64_data.split(',')[1]

        image_data = base64.b64decode(base64_data)

        with open(output_path, 'wb') as f:
            f.write(image_data)

        return json.dumps({
            "success": True,
            "path": output_path,
            "size": len(image_data)
        })

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
        print("=== 이미지 분석 (Image Analyzer) ===")
        print("  image_checklist                - 이미지 분석 체크리스트")
        print("  image_prompt <stage>           - 단계별 분석 프롬프트 (1,2,3)")
        print("  image_save '<analysis_json>'   - 분석 결과 저장")
        print("  image_coords <id> [w] [h] [m]  - 좌표 계산")
        print("  image_sequence <id> [level]    - MCP 시퀀스 생성")
        print("  image_draw '<json>' [w] [h] [m] [level] - 분석→좌표→시퀀스 통합")
        print("")
        print("=== 추천 워크플로우 ===")
        print("  [기존 도면 작업]")
        print("  1. create_task_auto - 엔티티와 오프셋으로 자동 계획 생성")
        print("  2. validate - 실행 전 준비 상태 확인")
        print("  3. checkpoint - 단계별 진행 기록")
        print("  4. auto_check - 맥락 손실 시 자동 복구")
        print("")
        print("  [이미지 기반 작도]")
        print("  1. image_checklist - 분석할 항목 확인")
        print("  2. image_save - 분석 결과 저장")
        print("  3. image_coords - 좌표 계산")
        print("  4. image_sequence - 시퀀스 생성 후 실행")
        print("  또는: image_draw - 1~4 통합 실행")
        print("")
        print("=== 등각투상(Isometric) 렌더링 ===")
        print("  iso_template_info              - 등각투상 템플릿 정보")
        print("  iso_portal [bays] [width] [depth] [eave] [ridge] [purlins] - 포털 프레임")
        print("  iso_h_beam <sx> <sy> <sz> <ex> <ey> <ez> [h] [w] - H형강 부재")
        print("  iso_purlin_array <sx> <sy> <sz> <ex> <ey> <ez> <count> <len> - 퍼린 배열")
        print("  iso_project <x> <y> <z> [angle] [scale] - 3D→2D 좌표 변환")
        print("")
        print("=== 등각투상 워크플로우 ===")
        print("  1. iso_template_info - 사용 가능한 템플릿 확인")
        print("  2. iso_portal - 건물 전체 시퀀스 생성")
        print("  3. 생성된 시퀀스의 MCP 도구 호출 실행")
        print("")
        print("=== 2D 뷰 렌더링 (사진→2D 도면) ===")
        print("  view2d_info                      - 2D 뷰 렌더러 정보 및 사용법")
        print("  view2d_from_photo '<json>' [w] [x] [y] - 사진 분석 결과로 2D 도면 생성")
        print("  view2d_calculate_coords '<json>' [w] [x] [y] - 좌표 미리 계산")
        print("  view2d_truss_only '<json>' [side] [w] [x] [y] - 트러스만 그리기")
        print("")
        print("=== 2D 뷰 워크플로우 (사진과 똑같은 도면) - 레거시 ===")
        print("  1. 사진 분석: 비율, 요소 개수 추출")
        print("  2. view2d_calculate_coords - 좌표 미리보기 (선택)")
        print("  3. view2d_from_photo - 전체 도면 시퀀스 생성")
        print("  4. 생성된 시퀀스의 MCP 도구 호출 실행")
        print("")
        print("=== 위치 기반 선 추출 (Line Extractor) ===")
        print("  line_info                      - 선 추출기 정보 및 사용법")
        print("  line_extract <path> [min_len] [use_lsd] - 이미지에서 선 추출")
        print("  line_extract_to_mcp <path> [width] [height] [min_len] [use_lsd] [by_region]")
        print("                                 - 추출된 선을 MCP 시퀀스로 변환")
        print("  line_extract_save <path> <output> [width] [height] [min_len]")
        print("                                 - 결과를 JSON으로 저장")
        print("")
        print("=== 위치 기반 선 추출 워크플로우 (신규) ===")
        print("  핵심: 선을 '기둥', '보'로 분류하지 않고 순수 위치만 기록")
        print("  1. line_extract <image.jpg> - 선 추출 및 위치 분석")
        print("  2. line_extract_to_mcp <image.jpg> - MCP 시퀀스 생성")
        print("  3. 시퀀스의 tools를 MCP로 실행")
        print("")
        print("  위치 컨텍스트:")
        print("    영역: top-left, top-center, middle-right, bottom-center 등")
        print("    방향: horizontal, vertical, diagonal-up, diagonal-down")
        print("    설명: 'top-left to top-center, horizontal'")
        print("")
        print("=== Image Vectorizer (vtracer 기반 벡터화) - 권장 ===")
        print("  vectorize_info                 - 벡터화 엔진 정보")
        print("  vectorize <path> '<bg>' '[options]' - 이미지 벡터화")
        print("  vectorize_base64 '<data>' '<bg>' '[options]' - Base64 벡터화")
        print("")
        print("=== Image Vectorizer 워크플로우 (권장) ===")
        print("  핵심: vtracer 알고리즘 기반 윤곽선 추출 및 단순화")
        print("  1. MCP get_background_images로 배경 이미지 좌표 확인")
        print("  2. vectorize <이미지경로> '<bg_json>' - 벡터화 및 MCP 시퀀스 생성")
        print("  3. 시퀀스의 tools를 MCP로 실행")
        print("")
        print("  모드:")
        print("    binary: 단순 이진화 (도면, 스케치용)")
        print("    edge: Sobel 엣지 감지 (사진용)")
        print("    edge_simple: 빠른 엣지 감지")
        print("")
        print("  예시:")
        print('    vectorize "photo.jpg" \'{"x":-73,"y":-77,"width":178,"height":100}\' \\')
        print('      \'{"mode":"edge","edge_threshold":30,"epsilon":3.0}\'')
        print("")
        print("  지원 형식:")
        print("    PPM/PGM: 의존성 없이 사용 가능")
        print("    JPG/PNG: PIL/Pillow 필요")
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

    # 이미지 분석 명령
    elif command == "image_checklist":
        print(image_checklist())
    elif command == "image_prompt" and len(sys.argv) > 2:
        print(image_prompt(sys.argv[2]))
    elif command == "image_save" and len(sys.argv) > 2:
        print(image_save_analysis(sys.argv[2]))
    elif command == "image_coords" and len(sys.argv) > 2:
        w = sys.argv[3] if len(sys.argv) > 3 else "800"
        h = sys.argv[4] if len(sys.argv) > 4 else "500"
        m = sys.argv[5] if len(sys.argv) > 5 else "50"
        print(image_coords(sys.argv[2], w, h, m))
    elif command == "image_sequence" and len(sys.argv) > 2:
        level = sys.argv[3] if len(sys.argv) > 3 else "L2_structural"
        print(image_sequence(sys.argv[2], level))
    elif command == "image_draw" and len(sys.argv) > 2:
        w = sys.argv[3] if len(sys.argv) > 3 else "800"
        h = sys.argv[4] if len(sys.argv) > 4 else "500"
        m = sys.argv[5] if len(sys.argv) > 5 else "50"
        level = sys.argv[6] if len(sys.argv) > 6 else "L2_structural"
        print(image_draw_from_analysis(sys.argv[2], w, h, m, level))

    # 등각투상 명령
    elif command == "iso_template_info":
        print(iso_template_info())
    elif command == "iso_portal":
        bays = sys.argv[2] if len(sys.argv) > 2 else "2"
        width = sys.argv[3] if len(sys.argv) > 3 else "6000"
        depth = sys.argv[4] if len(sys.argv) > 4 else "20000"
        eave = sys.argv[5] if len(sys.argv) > 5 else "6000"
        ridge = sys.argv[6] if len(sys.argv) > 6 else "7500"
        purlins = sys.argv[7] if len(sys.argv) > 7 else "6"
        c_width = sys.argv[8] if len(sys.argv) > 8 else "800"
        c_height = sys.argv[9] if len(sys.argv) > 9 else "500"
        print(iso_portal(bays, width, depth, eave, ridge, purlins, c_width, c_height))
    elif command == "iso_h_beam" and len(sys.argv) > 7:
        h = sys.argv[8] if len(sys.argv) > 8 else "400"
        w = sys.argv[9] if len(sys.argv) > 9 else "200"
        layer = sys.argv[10] if len(sys.argv) > 10 else "COLUMN"
        print(iso_h_beam(sys.argv[2], sys.argv[3], sys.argv[4],
                         sys.argv[5], sys.argv[6], sys.argv[7], h, w, layer))
    elif command == "iso_purlin_array" and len(sys.argv) > 9:
        layer = sys.argv[10] if len(sys.argv) > 10 else "PURLIN"
        print(iso_purlin_array(sys.argv[2], sys.argv[3], sys.argv[4],
                               sys.argv[5], sys.argv[6], sys.argv[7],
                               sys.argv[8], sys.argv[9], layer))
    elif command == "iso_project" and len(sys.argv) > 4:
        angle = sys.argv[5] if len(sys.argv) > 5 else "30"
        scale = sys.argv[6] if len(sys.argv) > 6 else "1.0"
        print(iso_project(sys.argv[2], sys.argv[3], sys.argv[4], angle, scale))

    # 2D 뷰 렌더링 명령
    elif command == "view2d_info":
        print(view2d_info())
    elif command == "view2d_from_photo" and len(sys.argv) > 2:
        w = sys.argv[3] if len(sys.argv) > 3 else "800"
        ox = sys.argv[4] if len(sys.argv) > 4 else "50"
        oy = sys.argv[5] if len(sys.argv) > 5 else "50"
        print(view2d_from_photo(sys.argv[2], w, ox, oy))
    elif command == "view2d_calculate_coords" and len(sys.argv) > 2:
        w = sys.argv[3] if len(sys.argv) > 3 else "800"
        ox = sys.argv[4] if len(sys.argv) > 4 else "50"
        oy = sys.argv[5] if len(sys.argv) > 5 else "50"
        print(view2d_calculate_coords(sys.argv[2], w, ox, oy))
    elif command == "view2d_truss_only" and len(sys.argv) > 2:
        side = sys.argv[3] if len(sys.argv) > 3 else "left"
        w = sys.argv[4] if len(sys.argv) > 4 else "800"
        ox = sys.argv[5] if len(sys.argv) > 5 else "50"
        oy = sys.argv[6] if len(sys.argv) > 6 else "50"
        print(view2d_truss_only(sys.argv[2], side, w, ox, oy))

    # 위치 기반 선 추출 명령
    elif command == "line_info":
        print(line_info())
    elif command == "line_extract" and len(sys.argv) > 2:
        min_len = sys.argv[3] if len(sys.argv) > 3 else "30"
        use_lsd = sys.argv[4] if len(sys.argv) > 4 else "true"
        print(line_extract(sys.argv[2], min_len, use_lsd))
    elif command == "line_extract_to_mcp" and len(sys.argv) > 2:
        width = sys.argv[3] if len(sys.argv) > 3 else "1000"
        height = sys.argv[4] if len(sys.argv) > 4 else "600"
        min_len = sys.argv[5] if len(sys.argv) > 5 else "30"
        use_lsd = sys.argv[6] if len(sys.argv) > 6 else "true"
        by_region = sys.argv[7] if len(sys.argv) > 7 else "true"
        print(line_extract_to_mcp(sys.argv[2], width, height, min_len, use_lsd, by_region))
    elif command == "line_extract_save" and len(sys.argv) > 3:
        width = sys.argv[4] if len(sys.argv) > 4 else "1000"
        height = sys.argv[5] if len(sys.argv) > 5 else "600"
        min_len = sys.argv[6] if len(sys.argv) > 6 else "30"
        print(line_extract_save(sys.argv[2], sys.argv[3], width, height, min_len))

    # Image Vectorizer 명령 (vtracer 기반 이미지→벡터 변환)
    elif command == "vectorize_info":
        print(vectorize_info())
    elif command == "vectorize" and len(sys.argv) >= 4:
        options = sys.argv[4] if len(sys.argv) > 4 else "{}"
        print(vectorize(sys.argv[2], sys.argv[3], options))
    elif command == "vectorize_base64" and len(sys.argv) >= 4:
        options = sys.argv[4] if len(sys.argv) > 4 else "{}"
        print(vectorize_base64(sys.argv[2], sys.argv[3], options))

    elif command == "vectorize_base64_to_dxf" and len(sys.argv) >= 5:
        # Base64 이미지 → DXF 직접 쓰기 (빠름, PIL 불필요)
        options = sys.argv[5] if len(sys.argv) > 5 else "{}"
        print(vectorize_base64_to_dxf(sys.argv[2], sys.argv[3], sys.argv[4], options))

    elif command == "save_base64_to_png" and len(sys.argv) >= 4:
        # Base64 → PNG 파일 저장
        print(save_base64_to_png(sys.argv[2], sys.argv[3]))

    else:
        print(json.dumps({"error": f"Unknown command or missing args: {command}"}))
