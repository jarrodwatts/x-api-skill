# Fundamentals: Response Codes and Errors

Authoritative docs:
- `https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md`

## High-Signal Status Codes

- `200/201/202`: success
- `400`: invalid request (bad params/body)
- `401`: missing/invalid auth
- `403`: forbidden (scopes/entitlement/policy)
- `404`: wrong id or resource not accessible
- `409`: conflict (state mismatch)
- `422`: well-formed, semantically invalid (often validation)
- `429`: rate limit
- `5xx`: server-side error (retry with backoff)

## Debugging Checklist

When an endpoint call fails, gather:
- full URL (including query string)
- request method
- auth mode (Bearer vs user token vs OAuth 1.0a)
- status code
- response body
- `x-rate-limit-*` headers

## Retry Policy

- Do not retry `400/401/403/404` blindly.
- Consider retry for:
  - `429` (sleep until reset)
  - `5xx` (backoff + jitter)

## Agent Output Requirements

When responding to a user with a failing request, return:
- the corrected curl command
- what was wrong
- how to confirm the fix (example expected response shape)
