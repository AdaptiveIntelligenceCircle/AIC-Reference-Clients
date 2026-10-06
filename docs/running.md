# Running

## Python

```bash
cd python
python3 -m pip install -e ".[dev]"   # or pip install -e .
python examples/evaluate_demo.py
python examples/ssi_demo.py
python -m pytest tests/ -q
```

Environment variables (optional):

| Variable | Meaning |
|----------|---------|
| `AIC_REF_ENDPOINT` | If set, client may attempt HTTP (experimental) |
| `AIC_REF_STRICT` | `1` enables stricter client-side validation |

## Rust / Go

Skeletons compile as placeholders. See `rust/README.md` and `go/README.md`.  
They exist to reserve crate/module names and Decision vocabulary, not as feature-complete clients.

## Mock vs remote

Prefer mock mode until a documented TestNet endpoint and message version exist.  
Remote use remains pre-Covenant and best-effort.