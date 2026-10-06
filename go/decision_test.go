package decision

import "testing"

func TestParseUnknownIsDeny(t *testing.T) {
	if ParseFailClosed("nope") != Deny {
		t.Fatalf("expected Deny")
	}
}

func TestNeedHumanRestrictive(t *testing.T) {
	if !NeedHuman.IsRestrictive() {
		t.Fatalf("NeedHuman should be restrictive")
	}
}
