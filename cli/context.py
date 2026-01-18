"""
Context CLI - 맥락 관리 (작업 생성, 체크포인트, 복구)
"""
import json
import sys
import os
from datetime import datetime
from typing import Dict, List, Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

try:
    from src.core import ContextManager, CoordinateCalculator
    CONTEXT_AVAILABLE = True
except ImportError:
    CONTEXT_AVAILABLE = False


def create_task(task_type: str, description: str) -> str:
    """새 작업 생성"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    task_id = ctx.create_task(task_type, description)
    return json.dumps({
        "success": True,
        "task_id": task_id,
        "message": f"Task created: {task_id}"
    })


def create_task_auto(task_type: str, description: str, entities_json: str,
                     dx: str, dy: str, batch_size: str = "20") -> str:
    """엔티티 선택 후 자동 작업 생성"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    try:
        entities = json.loads(entities_json)
        dx_val = float(dx)
        dy_val = float(dy)
        batch_sz = int(batch_size)

        ctx = ContextManager()
        result = ctx.create_task_with_entities(
            task_type, description, entities, dx_val, dy_val, batch_sz
        )
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def list_tasks() -> str:
    """활성 작업 목록"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    tasks = ctx.list_active_tasks()
    return json.dumps(tasks, ensure_ascii=False, indent=2)


def restore(task_id: str) -> str:
    """작업 맥락 복구"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    context = ctx.restore_context(task_id)
    if context is None:
        return json.dumps({"error": f"Task not found: {task_id}"})

    return json.dumps(context, ensure_ascii=False, indent=2)


def checkpoint(task_id: str, step: str, status: str) -> str:
    """체크포인트 기록"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    result = ctx.checkpoint(task_id, int(step), status)
    return json.dumps(result, ensure_ascii=False, indent=2)


def get_remaining(task_id: str) -> str:
    """남은 작업 조회"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    remaining = ctx.get_remaining_steps(task_id)
    return json.dumps(remaining, ensure_ascii=False, indent=2)


def validate(task_id: str) -> str:
    """작업 검증"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    result = ctx.validate_task(task_id)
    return json.dumps(result, ensure_ascii=False, indent=2)


def detect_loss(task_id: str, current_step: str = "0", entity_count: str = "0") -> str:
    """맥락 손실 감지"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    result = ctx.detect_context_loss(task_id, int(current_step), int(entity_count))
    return json.dumps(result, ensure_ascii=False, indent=2)


def auto_check(task_id: str, current_step: str = "0", entity_count: str = "0") -> str:
    """자동 맥락 확인 및 복구"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    loss = ctx.detect_context_loss(task_id, int(current_step), int(entity_count))

    if loss.get("confidence", 0) >= 0.5:
        context = ctx.restore_context(task_id)
        return json.dumps({
            "action": "restored",
            "loss_confidence": loss.get("confidence"),
            "restored_context": context
        }, ensure_ascii=False, indent=2)

    return json.dumps({
        "action": "none",
        "loss_confidence": loss.get("confidence"),
        "message": "Context OK"
    }, ensure_ascii=False, indent=2)


def health(task_id: str) -> str:
    """작업 건강도 점수"""
    if not CONTEXT_AVAILABLE:
        return json.dumps({"error": "Context Manager not available"})

    ctx = ContextManager()
    score = ctx.get_task_health(task_id)
    return json.dumps({"task_id": task_id, "health_score": score})
