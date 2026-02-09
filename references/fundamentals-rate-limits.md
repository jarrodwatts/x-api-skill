# Fundamentals: Rate Limits

Authoritative docs:
- `https://docs.x.com/fundamentals/rate-limits.md`

## What To Capture On Every Response

Rate limit headers are per-endpoint and (in practice) the easiest reliable signal:
- `x-rate-limit-limit`: allowed requests per window
- `x-rate-limit-remaining`: remaining requests in window
- `x-rate-limit-reset`: unix epoch seconds when the window resets

When debugging, always log these alongside request URL and status code.

## Handling 429

If you receive `429 Too Many Requests`:
1. Read `x-rate-limit-reset`.
2. Sleep until reset (add jitter) and retry.
3. Reduce concurrency.

Do not busy-loop. Avoid retry storms.

## Backoff Guidance

- Prefer "retry after reset" semantics when the reset header exists.
- Otherwise: exponential backoff with jitter.

## Pagination + Rate Limits

Pagination can multiply call volume quickly.

Rule of thumb:
- Cap pages.
- Stop when you have enough.
- Cache aggressively for read workflows.

## Agent Output Requirements

When drafting a solution for a user, include:
- Expected call count (rough estimate).
- Where pagination happens.
- What the failure mode is if rate limited.
