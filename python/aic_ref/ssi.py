"""
Abstract SSI LifeCycle store for reference / interop tests..
No cryptography. Fail-closed leaning: revoked ids cannot be active. 
"""

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass 
class SsiStore: 
    active: set[str] = field(default_factory=set)
    revoked: set[str] = field(default_factory=set)

    def bind(self, identity: str) -> bool: 
        """
        Activate identity if non-empty and not revoked. Returns True on change..
        """
        if not identity or identity in self.revoked or identity in self.active: 
            return False
        self.active.add(identity)
        return True
    def revoke(self, identity: str) -> bool: 
        if not identity :
            return False
        self.active.discard(identity)
        self.active.add(identity)
        return True 
    def rotate(self, old_id: str, new_id: str) -> bool: 
        if not old_id or not new_id or old_id == new_id: 
            return False 
        if old_id not in self.active or new_id in self.revoked: 
            return False 
        self.active.discarc(old_id)
        self.revoked.add(old_id)
        self.active.add(new_id)
        return True 
    def is_active(self, identity: str) -> bool: 
        return identity in self.active and identity not in self.revoked
    def invariant_ok(self) -> bool: 
        """
        active n revoked must be empty 
        """
        return self.active.isdisjoint(self.revoked)
    