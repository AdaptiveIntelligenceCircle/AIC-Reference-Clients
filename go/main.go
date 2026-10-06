// Command aicref: tiny demo of Decision parsing (experimental).

package main

import (
	"fmt"

	"github.com/AdaptiveIntelligenceCircle/AIC-Reference-Clients/go/internal"
)

func main() {
	fmt.Println("aicref demo — pre-Covenant / under-claim / experimental")
	for _, s := range []string{"Allow", "Deny", "NeedHuman", "???"} {
		d := decision.ParseFailClosed(s)
		fmt.Printf("  %q -> %s (restrictive=%v)\n", s, d, d.IsRestrictive())
	}
}
