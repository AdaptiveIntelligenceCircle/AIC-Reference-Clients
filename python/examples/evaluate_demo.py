#!/usr/bin/env python3
"""Demo: local mock evaluation (pre-Covenant, under-claim)."""

from aic_ref import RefClient, Decision


def main() -> None:
    client = RefClient()

    cases = [
        {"action": "", "identity": "alice", "flags": 0},
        {"action": "read", "identity": "", "flags": 0},
        {"action": "write", "identity": "alice", "flags": 0x1},
        {"action": "write", "identity": "alice", "flags": 0x2},
    ]

    print("AIC reference client — evaluate demo")
    print("Experimental / pre-Covenant / not production\n")

    for req in cases:
        decision = client.evaluate(req)
        print(f"request={req!s}")
        print(f"  -> {decision.value} (restrictive={decision.is_restrictive})")
        assert isinstance(decision, Decision)

    print("\nDone.")


if __name__ == "__main__":
    main()