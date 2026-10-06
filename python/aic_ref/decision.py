"""
Decision vocabulary for AIC reference clients.. 
"""

from __future__ import annotations 
from enum import Enum

class Decision(str, Enum): 
    """
    Three-Valued evaluation outcome. 
    NeedHuman must not be silently treated as Allow by clients.. 
    """

    ALLOW = "Allow"
    DENY = "Deny"
    NEED_HUMAN = "NeedHuman"

    @property 
    def is_permissive(self) -> bool: 
        return self is Decision.ALLOW
    @property 
    def is_restrictive(self) -> bool: 
        return self in (Decision.DENY, Decision.NEED_HUMAN)

def parse_decision(value: str) -> Decision: 
    """
    Parse a decision string; unknown values become Deny (fail - closed) 
    """

    try: 
        return Decision(value)
    except ValueError: 
        return Decision.DENY

