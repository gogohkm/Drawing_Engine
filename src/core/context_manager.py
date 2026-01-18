"""
Context Manager - 맥락 유지 시스템

복잡한 드로잉 작업 중 맥락을 잃어버리는 문제를 해결합니다.

4가지 핵심 기능:
1. 작업 전 시퀀스 자동 생성 - 도면 분석 후 실행 계획을 JSON으로 저장
2. 단계별 체크포인트 - 진행 상황을 파일에 기록하여 복구 가능
3. 좌표 사전 계산 - 모든 좌표를 미리 계산하여 저장
4. 맥락 손실 자동 감지 - 이상 징후 감지 시 자동 복구 트리거

사용법:
    ctx = ContextManager()

    # 1. 작업 시작 - 시퀀스 생성
    task_id = ctx.create_task("copy_region", source_bounds, target_position)

    # 2. 단계 실행 중 체크포인트
    ctx.checkpoint(task_id, step=1, status="completed", result={...})

    # 3. 맥락 복구 (대화 중간에 잊어버렸을 때)
    context = ctx.restore_context(task_id)

    # 4. 맥락 손실 감지 (자동)
    loss = ctx.detect_context_loss(task_id, current_state)
    if loss['lost']:
        context = ctx.restore_context(task_id)
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum
import hashlib

# 공통 타입 임포트
try:
    from common import TaskStatus, MCPToolGenerator
except ImportError:
    # 독립 실행 시 로컬 정의
    class TaskStatus(Enum):
        PLANNING = "planning"
        READY = "ready"
        IN_PROGRESS = "in_progress"
        PAUSED = "paused"
        COMPLETED = "completed"
        FAILED = "failed"

KNOWLEDGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTEXT_DIR = os.path.join(KNOWLEDGE_ROOT, "context")
ACTIVE_TASKS_FILE = os.path.join(CONTEXT_DIR, "active_tasks.json")


@dataclass
class Checkpoint:
    """단계별 체크포인트"""
    step: int
    name: str
    status: str  # pending, in_progress, completed, failed
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    entity_handles: List[str] = field(default_factory=list)  # 생성된 엔티티 핸들
    result: Dict = field(default_factory=dict)
    error: Optional[str] = None


@dataclass
class TaskContext:
    """작업 전체 맥락"""
    task_id: str
    task_type: str
    description: str
    status: TaskStatus
    created_at: str

    # 원본 데이터 (잊어버려도 복구 가능)
    source_data: Dict = field(default_factory=dict)  # 원본 도면 정보
    calculated_coords: List[Dict] = field(default_factory=list)  # 사전 계산된 좌표

    # 실행 계획
    total_steps: int = 0
    steps: List[Dict] = field(default_factory=list)  # 상세 실행 계획

    # 진행 상황
    current_step: int = 0
    checkpoints: List[Checkpoint] = field(default_factory=list)

    # 메타데이터
    last_updated: str = ""
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        result = asdict(self)
        result['status'] = self.status.value
        result['checkpoints'] = [asdict(cp) for cp in self.checkpoints]
        return result

    @classmethod
    def from_dict(cls, data: Dict) -> 'TaskContext':
        data['status'] = TaskStatus(data['status'])
        data['checkpoints'] = [Checkpoint(**cp) for cp in data.get('checkpoints', [])]
        return cls(**data)


class CoordinateCalculator:
    """좌표 사전 계산기"""

    @staticmethod
    def extract_from_region(entities: List[Dict], base_point: Dict = None) -> List[Dict]:
        """
        영역의 엔티티들에서 좌표 추출 및 정규화

        Args:
            entities: extract_region 결과
            base_point: 기준점 (없으면 자동 계산)

        Returns:
            정규화된 좌표 목록
        """
        if not entities:
            return []

        # 기준점 계산 (최소 x, y)
        if base_point is None:
            min_x = float('inf')
            min_y = float('inf')
            for e in entities:
                coords = CoordinateCalculator._get_entity_coords(e)
                for c in coords:
                    min_x = min(min_x, c.get('x', float('inf')))
                    min_y = min(min_y, c.get('y', float('inf')))
            base_point = {'x': min_x, 'y': min_y}

        # 상대 좌표로 변환
        normalized = []
        for e in entities:
            norm_entity = {
                'type': e.get('type'),
                'handle': e.get('handle'),
                'layer': e.get('layer'),
                'original': e,
                'relative_coords': []
            }

            coords = CoordinateCalculator._get_entity_coords(e)
            for c in coords:
                norm_entity['relative_coords'].append({
                    'x': c.get('x', 0) - base_point['x'],
                    'y': c.get('y', 0) - base_point['y']
                })

            # 타입별 추가 속성
            if e.get('type') == 'CIRCLE':
                norm_entity['radius'] = e.get('radius')
            elif e.get('type') == 'ARC':
                norm_entity['radius'] = e.get('radius')
                norm_entity['startAngle'] = e.get('startAngle')
                norm_entity['endAngle'] = e.get('endAngle')
            elif e.get('type') == 'TEXT':
                norm_entity['text'] = e.get('text')
                norm_entity['height'] = e.get('height')
                norm_entity['rotation'] = e.get('rotation', 0)

            normalized.append(norm_entity)

        return normalized

    @staticmethod
    def _get_entity_coords(entity: Dict) -> List[Dict]:
        """엔티티에서 좌표 추출 - 여러 형식 자동 감지"""
        entity_type = entity.get('type', '')

        if entity_type == 'LINE':
            # 형식 1: start/end 객체 (MCP get_selected_entities 결과)
            if 'start' in entity and isinstance(entity['start'], dict):
                return [entity['start'], entity['end']]
            # 형식 2: startX/startY 개별 필드
            return [
                {'x': entity.get('startX'), 'y': entity.get('startY')},
                {'x': entity.get('endX'), 'y': entity.get('endY')}
            ]
        elif entity_type in ['CIRCLE', 'ARC']:
            # 형식 1: center 객체
            if 'center' in entity and isinstance(entity['center'], dict):
                return [entity['center']]
            # 형식 2: centerX/centerY 개별 필드
            return [{'x': entity.get('centerX'), 'y': entity.get('centerY')}]
        elif entity_type == 'TEXT':
            # 형식 1: position 객체
            if 'position' in entity and isinstance(entity['position'], dict):
                return [entity['position']]
            # 형식 2: x/y 개별 필드
            return [{'x': entity.get('x'), 'y': entity.get('y')}]
        elif entity_type == 'LWPOLYLINE':
            vertices = entity.get('vertices', [])
            return [{'x': v.get('x'), 'y': v.get('y')} for v in vertices]
        else:
            return []

    @staticmethod
    def apply_offset(normalized_coords: List[Dict], target_point: Dict) -> List[Dict]:
        """
        정규화된 좌표에 오프셋 적용하여 실제 좌표 생성

        Args:
            normalized_coords: extract_from_region 결과
            target_point: 목표 위치

        Returns:
            실제 좌표가 적용된 엔티티 목록
        """
        result = []
        for entity in normalized_coords:
            new_entity = entity.copy()
            new_entity['absolute_coords'] = []

            for rel_coord in entity.get('relative_coords', []):
                new_entity['absolute_coords'].append({
                    'x': rel_coord['x'] + target_point['x'],
                    'y': rel_coord['y'] + target_point['y']
                })

            result.append(new_entity)

        return result

    @staticmethod
    def generate_mcp_calls(entities_with_coords: List[Dict], layer: str = None) -> List[Dict]:
        """
        좌표가 적용된 엔티티 목록에서 MCP 도구 호출 생성

        Args:
            entities_with_coords: apply_offset 결과
            layer: 대상 레이어 (없으면 원본 레이어 사용)

        Returns:
            MCP 도구 호출 목록
        """
        calls = []

        for entity in entities_with_coords:
            entity_type = entity.get('type')
            coords = entity.get('absolute_coords', [])
            target_layer = layer or entity.get('layer', '0')

            if entity_type == 'LINE' and len(coords) >= 2:
                calls.append({
                    'tool': 'create_line',
                    'args': {
                        'start': coords[0],
                        'end': coords[1],
                        'layer': target_layer
                    }
                })

            elif entity_type == 'CIRCLE' and len(coords) >= 1:
                calls.append({
                    'tool': 'create_circle',
                    'args': {
                        'center': coords[0],
                        'radius': entity.get('radius'),
                        'layer': target_layer
                    }
                })

            elif entity_type == 'ARC' and len(coords) >= 1:
                calls.append({
                    'tool': 'create_arc',
                    'args': {
                        'center': coords[0],
                        'radius': entity.get('radius'),
                        'startAngle': entity.get('startAngle'),
                        'endAngle': entity.get('endAngle'),
                        'layer': target_layer
                    }
                })

            elif entity_type == 'TEXT' and len(coords) >= 1:
                calls.append({
                    'tool': 'create_text',
                    'args': {
                        'position': coords[0],
                        'text': entity.get('text', ''),
                        'height': entity.get('height', 2.5),
                        'rotation': entity.get('rotation', 0),
                        'layer': target_layer
                    }
                })

            elif entity_type == 'LWPOLYLINE' and len(coords) >= 2:
                calls.append({
                    'tool': 'create_polyline',
                    'args': {
                        'vertices': coords,
                        'closed': entity.get('original', {}).get('closed', False),
                        'layer': target_layer
                    }
                })

        return calls


class ContextManager:
    """맥락 관리자 - 작업 컨텍스트 생성, 저장, 복구"""

    def __init__(self):
        self.coord_calc = CoordinateCalculator()
        self._ensure_context_dir()
        self.active_tasks = self._load_active_tasks()

    def _ensure_context_dir(self):
        """컨텍스트 디렉토리 확인"""
        if not os.path.exists(CONTEXT_DIR):
            os.makedirs(CONTEXT_DIR)

    def _load_active_tasks(self) -> Dict[str, TaskContext]:
        """활성 작업 목록 로드"""
        if os.path.exists(ACTIVE_TASKS_FILE):
            with open(ACTIVE_TASKS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    k: TaskContext.from_dict(v)
                    for k, v in data.get('tasks', {}).items()
                }
        return {}

    def _save_active_tasks(self):
        """활성 작업 목록 저장"""
        data = {
            'last_updated': datetime.now().isoformat(),
            'tasks': {k: v.to_dict() for k, v in self.active_tasks.items()}
        }
        with open(ACTIVE_TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _generate_task_id(self, task_type: str) -> str:
        """고유 작업 ID 생성"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        hash_suffix = hashlib.md5(f"{task_type}{timestamp}".encode()).hexdigest()[:6]
        return f"{task_type}_{timestamp}_{hash_suffix}"

    # ========== 1. 작업 전 시퀀스 자동 생성 ==========

    def validate_task_ready(self, task_id: str) -> Dict:
        """
        작업 실행 준비 상태 검증

        Returns:
            {"valid": bool, "issues": [...], "suggestions": [...]}
        """
        context = self.active_tasks.get(task_id)
        issues = []
        suggestions = []

        if not context:
            return {"valid": False, "issues": ["Task not found"], "suggestions": ["Create a new task with create_task()"]}

        if context.total_steps == 0:
            issues.append("No execution plan registered")
            suggestions.append("Call set_task_plan() or create_task_with_entities() to set up execution steps")

        if len(context.checkpoints) == 0:
            issues.append("No checkpoints initialized")
            suggestions.append("Execution plan will auto-create checkpoints when set")

        if context.status == TaskStatus.PLANNING:
            issues.append("Task still in PLANNING status")
            suggestions.append("Set execution plan to change status to READY")

        if context.status == TaskStatus.COMPLETED:
            issues.append("Task already completed")
            suggestions.append("Create a new task for additional work")

        if context.status == TaskStatus.FAILED:
            issues.append("Task is in FAILED status")
            suggestions.append("Review errors and create a new task or resume")

        return {
            "valid": len(issues) == 0,
            "status": context.status.value,
            "issues": issues,
            "suggestions": suggestions,
            "ready_to_execute": context.status in [TaskStatus.READY, TaskStatus.IN_PROGRESS]
        }

    def create_task_with_entities(self, task_type: str, description: str,
                                   entities: List[Dict], target_offset: Dict,
                                   batch_size: int = 20) -> Dict:
        """
        엔티티 기반 자동 계획 생성 - create_task + set_execution_plan 통합

        Args:
            task_type: 작업 유형
            description: 작업 설명
            entities: 원본 엔티티 목록 (MCP get_selected_entities 결과)
            target_offset: 목표 오프셋 {"dx": float, "dy": float}
            batch_size: 배치 크기 (기본 20개)

        Returns:
            {
                "task_id": str,
                "total_entities": int,
                "total_steps": int,
                "total_mcp_calls": int,
                "batches": [{"step": int, "entity_count": int, "types": {...}}]
            }
        """
        # 1. 작업 생성
        task_id = self.create_task(task_type, description, {
            "entity_count": len(entities),
            "target_offset": target_offset
        })

        context = self.active_tasks[task_id]

        # 2. 좌표 변환
        dx = target_offset.get('dx', 0)
        dy = target_offset.get('dy', 0)

        transformed_entities = []
        for e in entities:
            transformed = self._transform_entity(e, dx, dy)
            if transformed:
                transformed_entities.append(transformed)

        # 3. 타입별 분류 후 배치 생성
        by_type = {}
        for e in transformed_entities:
            t = e['type']
            if t not in by_type:
                by_type[t] = []
            by_type[t].append(e)

        # 4. 실행 계획 생성 (타입별 → 배치별)
        steps = []
        step_num = 0
        batches_info = []

        for entity_type, type_entities in by_type.items():
            # 해당 타입의 엔티티를 배치로 나눔
            for i in range(0, len(type_entities), batch_size):
                step_num += 1
                batch = type_entities[i:i+batch_size]

                tools = []
                for e in batch:
                    mcp_call = self._entity_to_mcp_call(e)
                    if mcp_call:
                        tools.append(mcp_call)

                steps.append({
                    'name': f'{entity_type} batch {i//batch_size + 1} ({len(batch)} entities)',
                    'entity_type': entity_type,
                    'parallel': True,
                    'tools': tools
                })

                batches_info.append({
                    'step': step_num,
                    'entity_type': entity_type,
                    'entity_count': len(batch),
                    'tool_count': len(tools)
                })

        # 5. 실행 계획 등록
        self.set_execution_plan(task_id, steps)

        # 6. 변환된 좌표 저장
        context.calculated_coords = transformed_entities
        context.source_data['original_entities'] = entities
        self._save_active_tasks()
        self._save_task_file(context)

        return {
            "task_id": task_id,
            "total_entities": len(entities),
            "transformed_entities": len(transformed_entities),
            "total_steps": len(steps),
            "total_mcp_calls": sum(len(s['tools']) for s in steps),
            "batches": batches_info,
            "status": "ready"
        }

    def _transform_entity(self, entity: Dict, dx: float, dy: float) -> Optional[Dict]:
        """엔티티 좌표 변환"""
        entity_type = entity.get('type', '')
        result = {'type': entity_type, 'layer': entity.get('layer', '0')}

        if entity_type == 'LINE':
            start = entity.get('start', {})
            end = entity.get('end', {})
            result['start'] = {'x': start.get('x', 0) + dx, 'y': start.get('y', 0) + dy}
            result['end'] = {'x': end.get('x', 0) + dx, 'y': end.get('y', 0) + dy}

        elif entity_type == 'CIRCLE':
            center = entity.get('center', {})
            result['center'] = {'x': center.get('x', 0) + dx, 'y': center.get('y', 0) + dy}
            result['radius'] = entity.get('radius', 1)

        elif entity_type == 'ARC':
            center = entity.get('center', {})
            result['center'] = {'x': center.get('x', 0) + dx, 'y': center.get('y', 0) + dy}
            result['radius'] = entity.get('radius', 1)
            result['startAngle'] = entity.get('startAngle', 0)
            result['endAngle'] = entity.get('endAngle', 360)

        elif entity_type == 'TEXT':
            pos = entity.get('position', {})
            result['position'] = {'x': pos.get('x', 0) + dx, 'y': pos.get('y', 0) + dy}
            result['text'] = entity.get('text', '')
            result['height'] = entity.get('height', 2.5)
            result['rotation'] = entity.get('rotation', 0)

        elif entity_type == 'LWPOLYLINE':
            vertices = entity.get('vertices', [])
            result['vertices'] = [
                {'x': v.get('x', 0) + dx, 'y': v.get('y', 0) + dy}
                for v in vertices
            ]
            result['closed'] = entity.get('closed', False)

        else:
            return None  # 지원하지 않는 타입

        return result

    def _entity_to_mcp_call(self, entity: Dict) -> Optional[Dict]:
        """변환된 엔티티를 MCP 도구 호출로 변환"""
        entity_type = entity.get('type', '')
        layer = entity.get('layer', '0')

        if entity_type == 'LINE':
            return {
                'tool': 'create_line',
                'args': {
                    'start': entity['start'],
                    'end': entity['end'],
                    'layer': layer
                }
            }
        elif entity_type == 'CIRCLE':
            return {
                'tool': 'create_circle',
                'args': {
                    'center': entity['center'],
                    'radius': entity['radius'],
                    'layer': layer
                }
            }
        elif entity_type == 'ARC':
            return {
                'tool': 'create_arc',
                'args': {
                    'center': entity['center'],
                    'radius': entity['radius'],
                    'startAngle': entity['startAngle'],
                    'endAngle': entity['endAngle'],
                    'layer': layer
                }
            }
        elif entity_type == 'TEXT':
            return {
                'tool': 'create_text',
                'args': {
                    'position': entity['position'],
                    'text': entity['text'],
                    'height': entity['height'],
                    'rotation': entity.get('rotation', 0),
                    'layer': layer
                }
            }
        elif entity_type == 'LWPOLYLINE':
            return {
                'tool': 'create_polyline',
                'args': {
                    'vertices': entity['vertices'],
                    'closed': entity.get('closed', False),
                    'layer': layer
                }
            }
        return None

    def create_task(self, task_type: str, description: str,
                    source_data: Dict = None) -> str:
        """
        새 작업 생성 및 컨텍스트 초기화

        Args:
            task_type: 작업 유형 (copy_region, draw_pattern, etc.)
            description: 작업 설명
            source_data: 원본 데이터 (도면 정보, 영역 등)

        Returns:
            task_id
        """
        task_id = self._generate_task_id(task_type)

        context = TaskContext(
            task_id=task_id,
            task_type=task_type,
            description=description,
            status=TaskStatus.PLANNING,
            created_at=datetime.now().isoformat(),
            source_data=source_data or {},
            last_updated=datetime.now().isoformat()
        )

        self.active_tasks[task_id] = context
        self._save_active_tasks()
        self._save_task_file(context)

        return task_id

    def set_calculated_coords(self, task_id: str, coords: List[Dict]):
        """사전 계산된 좌표 저장"""
        if task_id not in self.active_tasks:
            raise ValueError(f"Task not found: {task_id}")

        context = self.active_tasks[task_id]
        context.calculated_coords = coords
        context.last_updated = datetime.now().isoformat()

        self._save_active_tasks()
        self._save_task_file(context)

    def set_execution_plan(self, task_id: str, steps: List[Dict]):
        """
        실행 계획 설정

        Args:
            task_id: 작업 ID
            steps: 단계 목록 [{"name": "...", "tools": [...], "parallel": bool}, ...]
        """
        if task_id not in self.active_tasks:
            raise ValueError(f"Task not found: {task_id}")

        context = self.active_tasks[task_id]
        context.steps = steps
        context.total_steps = len(steps)
        context.status = TaskStatus.READY

        # 체크포인트 초기화
        context.checkpoints = [
            Checkpoint(step=i+1, name=s.get('name', f'Step {i+1}'), status='pending')
            for i, s in enumerate(steps)
        ]

        context.last_updated = datetime.now().isoformat()
        self._save_active_tasks()
        self._save_task_file(context)

    def generate_copy_sequence(self, task_id: str, source_entities: List[Dict],
                                base_point: Dict, target_point: Dict) -> List[Dict]:
        """
        영역 복사를 위한 시퀀스 자동 생성

        Args:
            task_id: 작업 ID
            source_entities: 원본 엔티티 목록 (extract_region 결과)
            base_point: 원본 기준점
            target_point: 목표 위치

        Returns:
            생성된 MCP 호출 목록
        """
        # 좌표 계산
        normalized = self.coord_calc.extract_from_region(source_entities, base_point)
        with_offset = self.coord_calc.apply_offset(normalized, target_point)
        mcp_calls = self.coord_calc.generate_mcp_calls(with_offset)

        # 컨텍스트에 저장
        context = self.active_tasks.get(task_id)
        if context:
            context.calculated_coords = with_offset
            context.source_data['base_point'] = base_point
            context.source_data['target_point'] = target_point
            context.source_data['entity_count'] = len(source_entities)

            # 실행 계획 생성 (레이어별로 그룹화)
            layers = {}
            for call in mcp_calls:
                layer = call['args'].get('layer', '0')
                if layer not in layers:
                    layers[layer] = []
                layers[layer].append(call)

            steps = []
            for layer, calls in layers.items():
                steps.append({
                    'name': f'Draw on layer {layer}',
                    'layer': layer,
                    'parallel': True,
                    'tools': calls
                })

            self.set_execution_plan(task_id, steps)

        return mcp_calls

    # ========== 2. 단계별 체크포인트 ==========

    def start_step(self, task_id: str, step: int):
        """단계 시작 기록"""
        context = self.active_tasks.get(task_id)
        if not context:
            raise ValueError(f"Task not found: {task_id}")

        # 체크포인트 미등록 시 명확한 에러
        if not context.checkpoints:
            raise ValueError(
                f"No execution plan registered for task '{task_id}'. "
                f"Call set_execution_plan() or use create_task_with_entities() first. "
                f"Current task status: {context.status.value}"
            )

        if step < 1 or step > len(context.checkpoints):
            raise ValueError(
                f"Invalid step {step} for task '{task_id}'. "
                f"Valid range: 1-{len(context.checkpoints)}. "
                f"Hint: Use validate_task_ready() to check task prerequisites."
            )

        cp = context.checkpoints[step - 1]
        cp.status = 'in_progress'
        cp.started_at = datetime.now().isoformat()

        context.current_step = step
        context.status = TaskStatus.IN_PROGRESS
        context.last_updated = datetime.now().isoformat()

        self._save_active_tasks()
        self._save_task_file(context)

    def complete_step(self, task_id: str, step: int,
                      entity_handles: List[str] = None, result: Dict = None):
        """단계 완료 기록"""
        context = self.active_tasks.get(task_id)
        if not context:
            raise ValueError(f"Task not found: {task_id}")

        if not context.checkpoints:
            raise ValueError(
                f"No execution plan registered for task '{task_id}'. "
                f"Cannot complete step without execution plan."
            )

        if step < 1 or step > len(context.checkpoints):
            raise ValueError(
                f"Invalid step {step}. Valid range: 1-{len(context.checkpoints)}"
            )

        cp = context.checkpoints[step - 1]
        cp.status = 'completed'
        cp.completed_at = datetime.now().isoformat()
        cp.entity_handles = entity_handles or []
        cp.result = result or {}

        # 모든 단계 완료 확인
        all_completed = all(c.status == 'completed' for c in context.checkpoints)
        if all_completed:
            context.status = TaskStatus.COMPLETED

        context.last_updated = datetime.now().isoformat()
        self._save_active_tasks()
        self._save_task_file(context)

    def fail_step(self, task_id: str, step: int, error: str):
        """단계 실패 기록"""
        context = self.active_tasks.get(task_id)
        if not context:
            raise ValueError(f"Task not found: {task_id}")

        if not context.checkpoints:
            raise ValueError(
                f"No execution plan registered for task '{task_id}'. "
                f"Cannot record failure without execution plan."
            )

        if step < 1 or step > len(context.checkpoints):
            raise ValueError(
                f"Invalid step {step}. Valid range: 1-{len(context.checkpoints)}"
            )

        cp = context.checkpoints[step - 1]
        cp.status = 'failed'
        cp.error = error
        cp.completed_at = datetime.now().isoformat()

        context.status = TaskStatus.PAUSED
        context.last_updated = datetime.now().isoformat()
        context.notes.append(f"Step {step} failed: {error}")

        self._save_active_tasks()
        self._save_task_file(context)

    def checkpoint(self, task_id: str, step: int, status: str,
                   entity_handles: List[str] = None, result: Dict = None,
                   error: str = None):
        """
        체크포인트 기록 (통합 메서드)

        Args:
            task_id: 작업 ID
            step: 단계 번호
            status: 상태 (in_progress, completed, failed)
            entity_handles: 생성된 엔티티 핸들 목록
            result: 결과 데이터
            error: 에러 메시지 (실패 시)
        """
        if status == 'in_progress':
            self.start_step(task_id, step)
        elif status == 'completed':
            self.complete_step(task_id, step, entity_handles, result)
        elif status == 'failed':
            self.fail_step(task_id, step, error or "Unknown error")

    # ========== 3. 맥락 복구 ==========

    def restore_context(self, task_id: str) -> Dict:
        """
        맥락 복구 - 대화 중간에 잊어버렸을 때 호출

        Args:
            task_id: 작업 ID

        Returns:
            복구된 컨텍스트 요약
        """
        # 파일에서 직접 로드 (메모리보다 파일이 더 신뢰성 있음)
        task_file = os.path.join(CONTEXT_DIR, f"task_{task_id}.json")

        if os.path.exists(task_file):
            with open(task_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                context = TaskContext.from_dict(data)
        elif task_id in self.active_tasks:
            context = self.active_tasks[task_id]
        else:
            return {"error": f"Task not found: {task_id}"}

        # 복구 요약 생성
        completed_steps = [cp for cp in context.checkpoints if cp.status == 'completed']
        pending_steps = [cp for cp in context.checkpoints if cp.status == 'pending']
        current_step_info = None

        if context.current_step > 0 and context.current_step <= len(context.checkpoints):
            current_step_info = context.steps[context.current_step - 1] if context.steps else None

        # 다음에 실행할 도구 호출 목록
        remaining_calls = []
        for i, step in enumerate(context.steps):
            if i + 1 > len(completed_steps):
                remaining_calls.extend(step.get('tools', []))

        return {
            "task_id": task_id,
            "task_type": context.task_type,
            "description": context.description,
            "status": context.status.value,

            "progress": {
                "total_steps": context.total_steps,
                "completed": len(completed_steps),
                "current_step": context.current_step,
                "pending": len(pending_steps)
            },

            "source_data": context.source_data,
            "calculated_coords_count": len(context.calculated_coords),

            "next_actions": {
                "current_step_name": current_step_info.get('name') if current_step_info else None,
                "remaining_tool_calls": len(remaining_calls),
                "next_tools": remaining_calls[:5]  # 다음 5개만 미리보기
            },

            "created_entities": [
                handle
                for cp in completed_steps
                for handle in cp.entity_handles
            ],

            "notes": context.notes
        }

    def get_remaining_calls(self, task_id: str) -> List[Dict]:
        """남은 MCP 호출 목록 반환"""
        context = self.active_tasks.get(task_id)
        if not context:
            return []

        completed_count = sum(1 for cp in context.checkpoints if cp.status == 'completed')
        remaining = []

        for i, step in enumerate(context.steps):
            if i >= completed_count:
                remaining.extend(step.get('tools', []))

        return remaining

    def get_step_tools(self, task_id: str, step: int) -> List[Dict]:
        """특정 단계의 도구 호출 목록 반환"""
        context = self.active_tasks.get(task_id)
        if not context or step < 1 or step > len(context.steps):
            return []

        return context.steps[step - 1].get('tools', [])

    # ========== 4. 맥락 손실 감지 ==========

    def detect_context_loss(self, task_id: str, current_state: Dict = None) -> Dict:
        """
        맥락 손실 감지 - 여러 지표를 확인하여 맥락 손실 여부 판단

        Args:
            task_id: 작업 ID
            current_state: 현재 상태 정보 (선택)
                - claimed_step: Claude가 인식하는 현재 단계
                - claimed_entities: Claude가 인식하는 생성된 엔티티 수
                - last_action: 마지막으로 실행한 작업
                - drawing_bounds: 현재 도면 bounds

        Returns:
            {
                "lost": bool,           # 맥락 손실 여부
                "confidence": float,    # 신뢰도 (0-1)
                "indicators": [...],    # 감지된 지표들
                "recommendation": str,  # 권장 조치
                "auto_restore": bool    # 자동 복구 필요 여부
            }
        """
        context = self.active_tasks.get(task_id)
        if not context:
            # 작업을 찾을 수 없음 - 파일에서 로드 시도
            task_file = os.path.join(CONTEXT_DIR, f"task_{task_id}.json")
            if os.path.exists(task_file):
                with open(task_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    context = TaskContext.from_dict(data)
                    self.active_tasks[task_id] = context
            else:
                return {
                    "lost": True,
                    "confidence": 1.0,
                    "indicators": ["task_not_found"],
                    "recommendation": "Task not found. Start a new task.",
                    "auto_restore": False
                }

        indicators = []
        confidence = 0.0
        current_state = current_state or {}

        # 1. 단계 불일치 감지
        if 'claimed_step' in current_state:
            actual_step = context.current_step
            claimed_step = current_state['claimed_step']
            if claimed_step != actual_step:
                indicators.append({
                    "type": "step_mismatch",
                    "actual": actual_step,
                    "claimed": claimed_step,
                    "severity": "high"
                })
                confidence += 0.4

        # 2. 엔티티 수 불일치 감지
        if 'claimed_entities' in current_state:
            actual_entities = sum(
                len(cp.entity_handles)
                for cp in context.checkpoints
                if cp.status == 'completed'
            )
            claimed_entities = current_state['claimed_entities']
            diff_ratio = abs(actual_entities - claimed_entities) / max(actual_entities, 1)
            if diff_ratio > 0.2:  # 20% 이상 차이
                indicators.append({
                    "type": "entity_count_mismatch",
                    "actual": actual_entities,
                    "claimed": claimed_entities,
                    "diff_ratio": diff_ratio,
                    "severity": "medium"
                })
                confidence += 0.3

        # 3. 시간 간격 감지 (마지막 업데이트로부터 오래됨)
        try:
            last_update = datetime.fromisoformat(context.last_updated)
            elapsed = (datetime.now() - last_update).total_seconds()
            if elapsed > 300:  # 5분 이상 경과
                indicators.append({
                    "type": "long_gap",
                    "elapsed_seconds": elapsed,
                    "severity": "low"
                })
                confidence += 0.1
        except:
            pass

        # 4. 진행 중 단계가 오래된 경우
        in_progress_steps = [
            cp for cp in context.checkpoints
            if cp.status == 'in_progress'
        ]
        for cp in in_progress_steps:
            if cp.started_at:
                try:
                    started = datetime.fromisoformat(cp.started_at)
                    elapsed = (datetime.now() - started).total_seconds()
                    if elapsed > 600:  # 10분 이상 in_progress 상태
                        indicators.append({
                            "type": "stuck_step",
                            "step": cp.step,
                            "elapsed_seconds": elapsed,
                            "severity": "medium"
                        })
                        confidence += 0.2
                except:
                    pass

        # 5. 작업이 PAUSED 상태인 경우
        if context.status == TaskStatus.PAUSED:
            indicators.append({
                "type": "task_paused",
                "reason": context.notes[-1] if context.notes else "Unknown",
                "severity": "high"
            })
            confidence += 0.3

        # 최종 판정
        confidence = min(confidence, 1.0)
        lost = confidence >= 0.3 or len(indicators) >= 2

        # 권장 조치 결정
        if not lost:
            recommendation = "Context appears intact. Continue normally."
            auto_restore = False
        elif confidence >= 0.7:
            recommendation = "High confidence of context loss. Auto-restore recommended."
            auto_restore = True
        else:
            recommendation = "Possible context loss. Review and restore if needed."
            auto_restore = confidence >= 0.5

        return {
            "lost": lost,
            "confidence": confidence,
            "indicators": indicators,
            "recommendation": recommendation,
            "auto_restore": auto_restore,
            "task_id": task_id,
            "actual_state": {
                "current_step": context.current_step,
                "total_steps": context.total_steps,
                "completed_steps": sum(1 for cp in context.checkpoints if cp.status == 'completed'),
                "status": context.status.value
            }
        }

    def check_and_auto_restore(self, task_id: str, current_state: Dict = None) -> Dict:
        """
        맥락 손실 확인 및 자동 복구

        Args:
            task_id: 작업 ID
            current_state: 현재 상태 (detect_context_loss 참조)

        Returns:
            복구 결과 또는 정상 상태 메시지
        """
        detection = self.detect_context_loss(task_id, current_state)

        if not detection['lost']:
            return {
                "action": "none",
                "message": "Context is intact",
                "detection": detection
            }

        if detection['auto_restore']:
            restored = self.restore_context(task_id)
            return {
                "action": "auto_restored",
                "message": "Context loss detected and auto-restored",
                "detection": detection,
                "restored_context": restored
            }
        else:
            return {
                "action": "manual_review",
                "message": "Possible context loss. Manual review recommended.",
                "detection": detection,
                "restore_command": f"python claude_helper.py restore {task_id}"
            }

    def get_context_health(self, task_id: str) -> Dict:
        """
        작업 컨텍스트 건강 상태 조회

        Returns:
            현재 상태 요약 (Claude가 자기 상태를 확인할 때 사용)
        """
        context = self.active_tasks.get(task_id)
        if not context:
            return {"error": f"Task not found: {task_id}"}

        completed = sum(1 for cp in context.checkpoints if cp.status == 'completed')
        in_progress = sum(1 for cp in context.checkpoints if cp.status == 'in_progress')
        failed = sum(1 for cp in context.checkpoints if cp.status == 'failed')

        return {
            "task_id": task_id,
            "status": context.status.value,
            "health": "good" if context.status == TaskStatus.IN_PROGRESS else "needs_attention",
            "progress": {
                "completed": completed,
                "in_progress": in_progress,
                "failed": failed,
                "total": context.total_steps,
                "percentage": (completed / context.total_steps * 100) if context.total_steps > 0 else 0
            },
            "current_step": context.current_step,
            "last_updated": context.last_updated,
            "notes": context.notes[-3:] if context.notes else []  # 최근 3개 노트
        }

    # ========== 유틸리티 ==========

    def _save_task_file(self, context: TaskContext):
        """개별 작업 파일 저장"""
        task_file = os.path.join(CONTEXT_DIR, f"task_{context.task_id}.json")
        with open(task_file, 'w', encoding='utf-8') as f:
            json.dump(context.to_dict(), f, ensure_ascii=False, indent=2)

    def list_active_tasks(self) -> List[Dict]:
        """활성 작업 목록"""
        return [
            {
                "task_id": ctx.task_id,
                "type": ctx.task_type,
                "description": ctx.description,
                "status": ctx.status.value,
                "progress": f"{sum(1 for cp in ctx.checkpoints if cp.status == 'completed')}/{ctx.total_steps}",
                "last_updated": ctx.last_updated
            }
            for ctx in self.active_tasks.values()
            if ctx.status not in [TaskStatus.COMPLETED, TaskStatus.FAILED]
        ]

    def cleanup_completed(self, keep_days: int = 7):
        """완료된 작업 정리"""
        cutoff = datetime.now().timestamp() - (keep_days * 86400)
        to_remove = []

        for task_id, ctx in self.active_tasks.items():
            if ctx.status in [TaskStatus.COMPLETED, TaskStatus.FAILED]:
                created = datetime.fromisoformat(ctx.created_at).timestamp()
                if created < cutoff:
                    to_remove.append(task_id)

        for task_id in to_remove:
            del self.active_tasks[task_id]
            task_file = os.path.join(CONTEXT_DIR, f"task_{task_id}.json")
            if os.path.exists(task_file):
                os.remove(task_file)

        self._save_active_tasks()
        return len(to_remove)


# CLI 인터페이스
if __name__ == "__main__":
    import sys

    ctx = ContextManager()

    if len(sys.argv) < 2:
        print("Usage: python context_manager.py <command> [args...]")
        print("Commands:")
        print("  list              - 활성 작업 목록")
        print("  restore <task_id> - 맥락 복구")
        print("  remaining <task_id> - 남은 호출 목록")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "list":
        tasks = ctx.list_active_tasks()
        print(json.dumps(tasks, ensure_ascii=False, indent=2))

    elif cmd == "restore" and len(sys.argv) > 2:
        result = ctx.restore_context(sys.argv[2])
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif cmd == "remaining" and len(sys.argv) > 2:
        calls = ctx.get_remaining_calls(sys.argv[2])
        print(json.dumps(calls, ensure_ascii=False, indent=2))
