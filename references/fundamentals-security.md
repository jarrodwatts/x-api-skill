# Fundamentals: Security

Authoritative docs:
- `https://docs.x.com/fundamentals/security.md`

## Defaults

- Use HTTPS endpoints only.
- Do not commit secrets.
- Store tokens in environment variables or a secrets manager.
- Rotate and revoke credentials if they leak.

## Logging

Never log:
- bearer tokens
- refresh tokens
- OAuth 1.0a signing keys

If you must log request headers for debugging, redact `Authorization`.

## Least Privilege

- Request only the OAuth scopes needed.
- Use separate apps/keys for environments.

## Webhooks / Account Activity

- Verify webhook signatures if provided by the product.
- Treat inbound webhook payloads as untrusted input.
