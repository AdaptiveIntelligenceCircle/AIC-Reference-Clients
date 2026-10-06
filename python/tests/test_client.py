from aic_ref import RefClient, Decision


def test_empty_action_denied_strict():
    c = RefClient(strict=True)
    assert c.evaluate({"action": "", "flags": 0x2}) is Decision.DENY


def test_need_human_flag():
    c = RefClient(strict=True)
    d = c.evaluate({"action": "x", "identity": "a", "flags": 0x1})
    assert d is Decision.NEED_HUMAN


def test_allow_path():
    c = RefClient(strict=True)
    d = c.evaluate({"action": "x", "identity": "a", "flags": 0x2})
    assert d is Decision.ALLOW


def test_evaluate_dict():
    c = RefClient()
    out = c.evaluate_dict({"action": "x", "flags": 0})
    assert out["decision"] in ("Allow", "Deny", "NeedHuman")
    assert "restrictive" in out