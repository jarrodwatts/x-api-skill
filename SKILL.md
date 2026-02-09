---
name: x-api-skill
description: "Let your AI agent use X (Twitter) on your behalf: post, reply, search, send DMs, bookmark, and follow. The agent will ask before doing anything that changes your account."
---

# X API Skill (v2)

This skill helps an agent do one thing well: **take what you want to do on X and do it safely and correctly**, including asking for missing details and confirming before any action that changes your account.

Compatibility: requires `curl` and `python3`; expects network access to `docs.x.com` and `api.x.com`.

If you say “tweet this”, the agent should:
- Draft the exact API call(s) needed.
- Tell you what token type/scopes you need.
- Ask for any missing IDs (user id, post id) or derive them safely.
- Confirm any write action before executing.

## What you can ask (copy/paste)

- “Post this text: `...`”
- “Reply to this post id `...` with: `...`”
- “Quote-post `...` and say: `...`”
- “Delete my post id `...`”
- “Search recent posts for `query` and return the top 20 results”
- “Set up a filtered stream rule for `query` and show me how to read results”
- “Send a DM to `@username` saying `...`”
- “Bookmark post id `...`”
- “Follow `@username`”

## What this skill needs from you (tokens)

This skill never asks you to paste secrets. It expects tokens via environment variables:
- **Read public data**: `X_BEARER_TOKEN` (app-only bearer token)
- **Do anything as a user** (post/reply/delete, bookmarks, DMs, follow/unfollow, etc.): `X_USER_ACCESS_TOKEN` (OAuth user context)

If an endpoint requires OAuth 1.0a (some legacy surfaces), the agent should call that out explicitly and avoid recommending it unless required.

## Setup: create an app (onboarding)

If you haven’t created an app/credentials yet, start in the [Developer Console](https://console.x.com/):
- Create an app
- Generate credentials (Bearer Token for read-only; OAuth 2.0 Client ID/Secret for user actions)
- Allowlist callback URLs for OAuth (exact match; local dev should use `http://127.0.0.1`)

Reference: `references/apps-and-credentials.md`

## Documentation index (for this skill’s sources)

To discover official X docs pages quickly, the agent can start from:
- `https://docs.x.com/llms.txt`

## What the agent should output

When answering, prefer a small, concrete plan and then the exact request(s):
- **Endpoint(s)** (method + path)
- **Auth mode** (bearer vs user context) and required **scopes** when known
- **curl** command(s) using env vars (never inline tokens)
- **Request shaping**: `fields` / `expansions` only when needed
- **Pagination**: a stop condition (page cap, result cap, time bounds)
- **Rate limits**: how to behave on `429` using response headers
- **Errors**: how to interpret `401/403/429/5xx` and what to fix vs retry

## Important behavior rules

- **Default to least-privileged**: use bearer only for read-only public data; use user context for writes.
- **Be explicit about side effects**: for write actions, state what will happen and confirm before executing.
- **Avoid bulk actions by default**: if a user asks for bulk deletes/DMs/follows, require a cap and mention rate limits + compliance considerations.
- **Use stable identifiers**: treat IDs as strings (do not parse as numbers).
- **Minimize follow-up calls**: use `expansions` + `*.fields` to avoid N+1 patterns when it meaningfully reduces requests.

## Deeper references (optional)

If you need the detailed docs map or topic guides:
- `references/getting-started.md`
- `references/docs-map.md`
- `references/workflows.md`
- `references/request-shapes.md`
- `references/fundamentals-auth.md`
- `references/apps-and-credentials.md`
