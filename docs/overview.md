# Overview — AIC-Reference-Clients

## Why reference clients

AIC protocol ideas (Ethical Kernel decisions, SSI lifecycle sketches, parallel-net isolation) are easier to discuss and test when small clients exist outside the main C++ TestNet tree.

This repository supplies **minimal** clients that:

- share a small vocabulary (Decision, Request, SSI ops),
- default toward fail-closed validation,
- can run against in-process mocks without any network,
- stay explicitly experimental.

## Design choices

1. **Small surface** — evaluate-style calls and abstract SSI ops first; no full agent runtime.
2. **Language polyglot intent** — Python is the complete minimal reference; Rust and Go hold skeletons so naming stays aligned.
3. **Mock-first** — examples work offline; any real endpoint is optional and experimental.
4. **Aligned with formal intent** — Decision ∈ {Allow, Deny, NeedHuman}; revoked identities stay inactive in the SSI sketch.

## What “interop” means here

Interop testing means: *can another process or language construct messages and interpret decisions consistently with this sketch?*  
It does **not** mean certified compatibility with a frozen production protocol (none is declared).