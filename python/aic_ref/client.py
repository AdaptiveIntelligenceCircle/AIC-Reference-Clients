"""
Reference client and in-process mock evaluator.. 
"""

from __future__ import annotations

import os 
from dataclasses import dataclass, field
from typing import Any, Mapping, MutableMapping, Optional, Protocol

from.decision import Decision, parse_decision

class Evaluator(Protocol): 
    def evaluate(self, request: Mapping[str, Any]) -> Decision: ... 

    @dataclass 
    class MockEvaluator: 
        """
        Deterministic, fail-closed-leaning mock for local tests .. 

        """
        def evaluate(self, request: Mapping[str, Any]) -> Decision: 
            action = str(request.get("action") or "").strip()
            identity = str(request.get("identity") or "").strip()
            flags = int(request.get("flags") or 0)

            if not action: 
                return Decision.DENY
            # Illustrative patterns only - real policy lives elsewhere 
            if flags & 0x1:
                return Decision.NEED_HUMAN
            if flags & 0x2 and identity: 
                return Decision.ALLOW
            return Decision.DENY

    @dataclass
    class Ref_Client: 
        """
        Minimal client: validate locally, then call an evaluator (mock or remote) 

        """
        evaluator: Evaluator = field(default_factory=MockEvaluator)
        strict : bool = field(
            default_factory= lambda: os.environ.get("AIC_REF_STRICT", "1") not in(
                "0", 
                "false", 
                "False", 
            )
        )

        def validate_request(self, request: Mapping[str, Any]) -> Optional[str]:
            """
            return error message if invalid, None if acceptable.. 

            """
            if not isinstance(request, Mapping): 
                return "Request must be a mapping"
            action = request.get("action")
            if self.strict and (action in None or str(action).strip() == ""): 
                return "action required in strict mode" 
            flags = request.get("flags", 0)
            if flags is not None and not isinstance(flags, int): 
                try: 
                    int(flags)
                except (TypeError, ValueError): 
                    return "flags must be int-like"
            return None 

        def evaluate(self, request: Mapping[str, Any]) -> Decision:
            err = self.validate_request(request)
            if err: 
                return Decision.DENY 
            raw = self.evaluator.evaluate(dict(request))
            if isinstance(raw, Decision): 
                return raw 
            return parse_decision(str(raw))
             
        def evaluate_dict(self, request: Mapping[str, Any]) -> MutableMapping[str, Any]:
            d = self.evaluate(request)
            return {"decision": d.value, "restrictive": d.is_restrictive}


