# Fundamentals: Authentication

Authoritative docs:
- `https://docs.x.com/fundamentals/authentication/overview.md`
- `https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping.md`
- `https://docs.x.com/fundamentals/authentication/oauth-2-0/bearer-tokens.md`
- `https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md`
- `https://docs.x.com/fundamentals/authentication/oauth-1-0a/authorizing-a-request.md`
- `https://docs.x.com/fundamentals/authentication/oauth-1-0a/creating-a-signature.md`

## Pick The Right Auth Mode

Use this as the default decision rule:

- `Authorization: Bearer ...` (app-only):
  - Read public data.
  - Best for server-to-server jobs.

- OAuth 2.0 user context (Authorization Code + PKCE):
  - Any action on behalf of a user (create/delete Post, bookmarks, DMs, follow/unfollow, etc.).
  - Best default for most user-context integrations.

- OAuth 1.0a user context:
  - Use when the endpoint requires OAuth 1.0a (some legacy surfaces).
  - More complex signing; avoid unless required by the auth mapping.

When in doubt, consult the v2 auth mapping doc for the specific endpoint.

Pragmatic shortcut:
- If you have the docs OpenAPI page URL for an endpoint, run:
  - `python3 /Users/jarrod/x-api-skill/scripts/x_openapi_curl.py <url>`
  - This prints the endpoint path plus the `security:` block (schemes/scopes) and a curl skeleton.

## Bearer Token (App-Only)

Headers:
- `Authorization: Bearer $X_BEARER_TOKEN`

Example:
```bash
curl -sS "https://api.x.com/2/users/by/username/xdevelopers" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## OAuth 2.0 Authorization Code Flow With PKCE (User Context)

This skill is curl-first, so it describes the HTTP pieces rather than a full interactive flow.

Typical shape:
1. Create PKCE verifier/challenge.
2. Send user to the authorization URL (`/2/oauth2/authorize`) with:
   - `client_id`, `redirect_uri`
   - `response_type=code`
   - `scope=...`
   - PKCE: `code_challenge`, `code_challenge_method=S256`
   - `state`
3. Exchange `code` for tokens at `/2/oauth2/token`.
4. Call API endpoints with `Authorization: Bearer $X_USER_ACCESS_TOKEN`.

Doc:
- `https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code.md`

## OAuth 1.0a User Context (Signed Requests)

OAuth 1.0a requires constructing an `Authorization: OAuth ...` header with a signature.

Doc set:
- `https://docs.x.com/fundamentals/authentication/oauth-1-0a/authorizing-a-request.md`
- `https://docs.x.com/fundamentals/authentication/oauth-1-0a/creating-a-signature.md`

Pragmatic rule:
- If an endpoint supports OAuth 2.0 user token, prefer OAuth 2.0.
- If you must use OAuth 1.0a, implement signing in a small script and keep curl examples focused on the request itself.

## Common Failure Modes

- `401 Unauthorized`:
  - Wrong token type (Bearer vs user-context).
  - Missing scopes (OAuth 2.0).
  - Token expired/revoked.

- `403 Forbidden`:
  - App plan/entitlement does not allow the endpoint.
  - Scope missing or action not permitted.

- `429 Too Many Requests`:
  - Rate limit exceeded; see `fundamentals-rate-limits.md`.
