//! AIC reference client skeleton (Rust).
//! Pre-Covenant, under-claim, experimental. Not a production SDK.

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Decision {
    Allow,
    Deny,
    NeedHuman,
}

impl Decision {
    pub fn is_restrictive(self) -> bool {
        matches!(self, Decision::Deny | Decision::NeedHuman)
    }

    pub fn parse_fail_closed(s: &str) -> Self {
        match s {
            "Allow" => Decision::Allow,
            "NeedHuman" => Decision::NeedHuman,
            _ => Decision::Deny,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_unknown_is_deny() {
        assert_eq!(Decision::parse_fail_closed("nope"), Decision::Deny);
    }

    #[test]
    fn need_human_is_restrictive() {
        assert!(Decision::NeedHuman.is_restrictive());
    }
}