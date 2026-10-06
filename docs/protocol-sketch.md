# Protocol sketch (minimal)

**Experimental. Pre-Covenant. Not a final wire protocol.**

## Decision

```
Decision = "Allow" | "Deny" | "NeedHuman"
```

- **Allow** — modeled permission under current constraints.
- **Deny** — fail-closed outcome.
- **NeedHuman** — human gate required; clients must not silently upgrade this to Allow.

## Request (evaluate)

Minimal fields for the reference client:

| Field | Type | Notes |
|-------|------|--------|
| `action` | string | Required for non-Deny paths in strict mode |
| `identity` | string | Optional depending on policy |
| `flags` | integer | Opaque to the reference client; server-defined |
| `context` | object | Optional key-value hints |

Client-side validation may reject empty `action` before sending (fail-closed leaning).

## SSI ops (abstract)

| Op | Meaning |
|----|---------|
| `bind(id)` | Activate identity if not revoked |
| `revoke(id)` | Deactivate and mark revoked |
| `rotate(old, new)` | Revoke old, bind new under constraints |

No cryptography is implemented in the reference clients.  
These ops exist for state-machine and interop testing only.

## Envelope (optional JSON)

See `schemas/request.schema.json` and `schemas/decision.schema.json`.  
Schemas are descriptive, not a guarantee of server behavior.

## Transport

- **In-process mock** — default for examples and tests.
- **HTTP loopback** — optional example only.
- **Real Parallel TestNet** — out of scope until endpoints and versioning are documented upstream; still experimental if used.