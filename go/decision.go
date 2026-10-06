// Package decision holds the AIC Decision vocabulary (reference sketch).
// Pre-Covenant, under-claim, experimental.
package decision

type Decision string

const (
	Allow     Decision = "Allow"
	Deny      Decision = "Deny"
	NeedHuman Decision = "NeedHuman"
)

func (d Decision) IsRestrictive() bool {
	return d == Deny || d == NeedHuman
}

// ParseFailClosed maps unknown strings to Deny.
func ParseFailClosed(s string) Decision {
	switch s {
	case string(Allow):
		return Allow
	case string(NeedHuman):
		return NeedHuman
	default:
		return Deny
	}
}
