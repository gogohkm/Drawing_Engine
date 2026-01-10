"""
QA Rules (Sample)

규칙은 '결정론적'이어야 하며,
가능하면 stgen의 분석/추출 tool 결과만으로 판단한다.
"""

from __future__ import annotations

from typing import Any, Dict, List


def _check(severity: str, rule: str, message: str, evidence: Dict[str, Any] | None = None) -> Dict[str, Any]:
    return {
        "severity": severity,
        "rule": rule,
        "message": message,
        "evidence": evidence or {}
    }


def rule_required_layers(layers_result: Dict[str, Any], required_layers: List[str]) -> List[Dict[str, Any]]:
    layers = layers_result.get("layers") or []
    existing = {l.get("name") for l in layers if isinstance(l, dict)}
    missing = [l for l in required_layers if l not in existing]
    if missing:
        return [_check("ERROR", "required_layers", f"필수 레이어 누락: {missing}", {"missing": missing})]
    return []


def rule_no_entities_on_layer(layers_result: Dict[str, Any], layer_name: str = "0") -> List[Dict[str, Any]]:
    layers = layers_result.get("layers") or []
    for l in layers:
        if not isinstance(l, dict):
            continue
        if l.get("name") == layer_name and (l.get("entity_count", 0) or 0) > 0:
            return [_check("WARN", "no_entities_on_layer", f"레이어 '{layer_name}'에 엔티티 존재: {l.get('entity_count')}", {"layer": l})]
    return []


def rule_placeholder_texts(texts_result: Dict[str, Any]) -> List[Dict[str, Any]]:
    texts = texts_result.get("texts") or []
    bad = []
    for t in texts:
        if not isinstance(t, dict):
            continue
        s = (t.get("text") or "").upper()
        if "TBD" in s or "??" in s:
            bad.append(t)
    if bad:
        return [_check("WARN", "placeholder_texts", f"Placeholder 텍스트 발견({len(bad)}개)", {"items": bad[:20]})]
    return []


def rule_min_dimension_count(dim_result: Dict[str, Any], min_count: int = 1) -> List[Dict[str, Any]]:
    dims = dim_result.get("dimensions") or []
    if len(dims) < min_count:
        return [_check("WARN", "min_dimension_count", f"치수 개수가 너무 적음: {len(dims)} (<{min_count})", {"count": len(dims)})]
    return []
