# Limitations

## 1. Not a production SDK

APIs will change. Dependency on these clients for critical systems is discouraged.

## 2. No cryptographic SSI

Bind / revoke / rotate are abstract state operations.  
They do not prove possession of keys or authenticity of credentials.

## 3. No consensus or networking stack

Clients do not implement peer discovery, consensus, or secure channels.

## 4. Mock success ≠ protocol completeness

Passing local tests shows the reference code behaves as written.  
It does not prove interop with every TestNet binary or future revision.

## 5. Pre-Covenant

Nothing here declares mainnet or Covenant readiness.

## 6. Entity ≠ immunity

Using these clients does not create special legal or operational status for any party.

## 7. Fail-closed is a posture, not a proof

Client-side checks help; they do not replace server-side enforcement or formal reasoning (see AIC-Formal).