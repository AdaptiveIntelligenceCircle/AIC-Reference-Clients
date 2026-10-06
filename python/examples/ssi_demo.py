#!/usr/bin/env python3
"""Demo: abstract SSI store (no cryptography)."""

from aic_ref import SsiStore


def main() -> None:
    store = SsiStore()
    print("SSI abstract demo — bind / revoke / rotate")
    print("No cryptography. Experimental only.\n")

    assert store.bind("alice") is True
    assert store.bind("alice") is False  # already active
    assert store.is_active("alice")
    assert store.rotate("alice", "alice-2") is True
    assert not store.is_active("alice")
    assert store.is_active("alice-2")
    assert store.revoke("alice-2") is True
    assert store.bind("alice-2") is False  # revoked
    assert store.invariant_ok()

    print("active:", sorted(store.active))
    print("revoked:", sorted(store.revoked))
    print("invariant_ok:", store.invariant_ok())
    print("\nDone.")


if __name__ == "__main__":
    main()