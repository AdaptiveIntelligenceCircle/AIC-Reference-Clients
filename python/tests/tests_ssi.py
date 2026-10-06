from aic_ref import SsiStore


def test_bind_revoke_rotate():
    s = SsiStore()
    assert s.bind("a")
    assert not s.bind("a")
    assert s.rotate("a", "b")
    assert not s.is_active("a")
    assert s.is_active("b")
    assert s.revoke("b")
    assert not s.bind("b")
    assert s.invariant_ok()


def test_rotate_rejects_revoked_new():
    s = SsiStore()
    s.bind("a")
    s.revoke("c")
    assert not s.rotate("a", "c")
    assert s.is_active("a")