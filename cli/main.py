#!/usr/bin/env python3
"""
Drawing Engine CLI - Claude Code 세션 헬퍼

사용법:
    python -m cli.main session_start
    python -m cli.main list_sequences
    python -m cli.main get_sequence simple_room
    python -m cli.main create_task copy_region "도면 복사"
    python -m cli.main restore <task_id>
"""
import sys
import os

# 프로젝트 루트를 path에 추가
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from cli import session, context


def print_help():
    """도움말 출력"""
    help_text = """
Drawing Engine CLI - Claude Code 세션 헬퍼

세션 관리:
    session_start              세션 시작 및 지식 로드
    list_sequences             사용 가능한 시퀀스 목록
    get_sequence <name>        시퀀스 상세 조회
    get_pattern <name>         요소 패턴 조회

기록 관리:
    record_success <task> <approach> <key_factors> <entity_counts> <tags> [notes]
    record_failure <task> <error> <cause> <solution> <prevention> <tags>

맥락 관리:
    create_task <type> <description>
    create_task_auto <type> <description> <entities_json> <dx> <dy> [batch_size]
    list_tasks                 활성 작업 목록
    restore <task_id>          맥락 복구
    checkpoint <task_id> <step> <status>
    get_remaining <task_id>    남은 작업
    validate <task_id>         작업 검증
    detect_loss <task_id> [step] [entity_count]
    auto_check <task_id> [step] [entity_count]
    health <task_id>           작업 건강도
"""
    print(help_text)


def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    # 세션 관리
    if cmd == "session_start":
        print(session.session_start())
    elif cmd == "list_sequences":
        print(session.list_sequences())
    elif cmd == "get_sequence" and len(args) >= 1:
        print(session.get_sequence(args[0]))
    elif cmd == "get_pattern" and len(args) >= 1:
        print(session.get_pattern(args[0]))

    # 기록 관리
    elif cmd == "record_success" and len(args) >= 5:
        notes = args[5] if len(args) > 5 else ""
        print(session.record_success(args[0], args[1], args[2], args[3], args[4], notes))
    elif cmd == "record_failure" and len(args) >= 6:
        print(session.record_failure(args[0], args[1], args[2], args[3], args[4], args[5]))

    # 맥락 관리
    elif cmd == "create_task" and len(args) >= 2:
        print(context.create_task(args[0], args[1]))
    elif cmd == "create_task_auto" and len(args) >= 5:
        batch_size = args[5] if len(args) > 5 else "20"
        print(context.create_task_auto(args[0], args[1], args[2], args[3], args[4], batch_size))
    elif cmd == "list_tasks":
        print(context.list_tasks())
    elif cmd == "restore" and len(args) >= 1:
        print(context.restore(args[0]))
    elif cmd == "checkpoint" and len(args) >= 3:
        print(context.checkpoint(args[0], args[1], args[2]))
    elif cmd == "get_remaining" and len(args) >= 1:
        print(context.get_remaining(args[0]))
    elif cmd == "validate" and len(args) >= 1:
        print(context.validate(args[0]))
    elif cmd == "detect_loss" and len(args) >= 1:
        step = args[1] if len(args) > 1 else "0"
        count = args[2] if len(args) > 2 else "0"
        print(context.detect_loss(args[0], step, count))
    elif cmd == "auto_check" and len(args) >= 1:
        step = args[1] if len(args) > 1 else "0"
        count = args[2] if len(args) > 2 else "0"
        print(context.auto_check(args[0], step, count))
    elif cmd == "health" and len(args) >= 1:
        print(context.health(args[0]))

    # 도움말
    elif cmd in ["help", "-h", "--help"]:
        print_help()

    else:
        print(f"Unknown command: {cmd}")
        print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
