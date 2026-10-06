# AIC-Reference-Clients

**Minimal reference clients (Python, with Rust/Go skeletons) for interop and integration testing against AIC protocol sketches.**

Status: **pre-Covenant**, experimental, under-claim.  

These clients are **design and test aids**. They are not production SDKs, not full protocol implementations, and not a claim that any network is ready for public reliance.

## Purpose

- Provide small, readable clients that speak a **minimal shared vocabulary** (Decision, SSI lifecycle sketches, request envelopes).
- Help contributors test interop ideas against Parallel TestNet stubs or local mocks without pulling the entire C++ stack.
- Keep language and defaults aligned with AIC principles: fail-closed, NeedHuman as first-class, no token rule-power, under-claim.

## Explicit non-goals

| This repository does | This repository does **not** |
|----------------------|------------------------------|
| Offer minimal reference clients for experiments | Ship a production-ready multi-language SDK |
| Encode Allow / Deny / NeedHuman and simple SSI ops | Implement full cryptography or consensus |
| Support local mock / loopback testing | Connect to a declared mainnet (none is declared) |
| Stay under-claim and pre-Covenant | Certify interop or compliance |

## Layout

```
AIC-Reference-Clients/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/
│   ├── overview.md
│   ├── protocol-sketch.md
│   ├── running.md
│   └── limitations.md
├── python/                 # most complete minimal client
│   ├── aic_ref/
│   ├── examples/
│   └── tests/
├── rust/                   # skeleton
├── go/                     # skeleton
├── schemas/                # optional JSON message shapes
└── scripts/
```

## Quick start (Python)

```bash
cd python
python3 -m venv .venv && source .venv/bin/activate   # optional
pip install -e .                                    # if pyproject present
python examples/evaluate_demo.py
python -m pytest tests/ -q
```

See `docs/running.md` for details.

## Relationship to other AIC repositories

- **AIC-TestNet / Parallel TestNet** — eventual real endpoints; clients here may target stubs first.
- **AIC-Formal** — Decision and SSI properties inform client-side checks.
- **AIC-Security-Harness** — harnesses may drive similar entry points; clients stay higher-level and multi-language oriented.
- **AIC-Start-Here / Localization** — orientation only.

## Principles observed

- **Under-claim**: no production or Covenant claims.
- **Fail-closed**: client-side validation prefers Deny / error on malformed input.
- **NeedHuman**: represented explicitly in the Decision type.
- **No token rule-power**: no economic fields in the minimal protocol sketch.
- **Entity ≠ immunity**: clients do not grant special status to any party.
- **Pre-Covenant**: nothing here declares a main surface.

## License

GPL-3.0-or-later (see LICENSE).

## Maintenance note

During reduced maintainer availability the repository remains public.  
Small, readable, under-claim-preserving contributions are welcome.
