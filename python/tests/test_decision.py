from aic_ref import Decision
from aic_ref.decision import parse_decision


def test_decision_values():
    assert Decision.ALLOW.value == "Allow"
    assert Decision.DENY.is_restrictive
    assert Decision.NEED_HUMAN.is_restrictive
    assert Decision.ALLOW.is_permissive


def test_parse_unknown_is_deny():
    assert parse_decision("Allow") is Decision.ALLOW
    assert parse_decision("not-a-decision") is Decision.DENY