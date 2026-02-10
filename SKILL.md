---
name: x-api-skill
description: "X (Twitter) API usage and safe automation guidelines. This skill should be used when interacting with X (Twitter), including creating posts, reading the timeline, sending messages, or any other X (Twitter) capabilities that can be executed via API requests (post/reply/search, DMs, bookmarks, follows, auth, DMs, spaces, etc.)."
---

# X API Skill

This skill is a set of guidelines and tools for interacting with X (Twitter) via the X API (https://console.x.com/) and docs (https://docs.x.com/overview). Use the suite of `.md` files in `/references` for more detailed information and examples.

Compatibility: requires `curl` and `python3`; expects network access to `docs.x.com` and `api.x.com`.

## When to Apply

Reference these guidelines when:

- Performing any action on X (Twitter) that can be executed via API requests (post/reply/search, DMs, bookmarks, follows, auth, DMs, spaces, etc.)
- Understanding how to use the X (Twitter) API
- Setting up X (Twitter) API credentials (https://console.x.com/)
- Understanding the X (Twitter) API documentation (https://docs.x.com/overview)

## Example prompts of when to apply this skill

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

## Automation & spam compliance

All usage must follow X's Automation Rules (https://help.x.com/en/rules-and-policies/x-automation) and Developer Agreement (https://developer.x.com/en/developer-terms/agreement-and-policy). Key rules:

- **Consent before outreach**: never send automated replies or DMs without explicit opt-in from the recipient.
- **Honor opt-outs immediately**: if someone asks to stop being contacted, stop.
- **No bulk/aggressive actions**: no mass following, unfollowing, liking, or DMing. Always cap and pace automated actions.
- **No duplicate content**: never post identical or substantially similar content across multiple accounts.
- **Bot disclosure**: if operating a bot account, the profile bio must clearly state it is a bot and who is responsible for it.
- **No trend manipulation**: do not automatically post about trending topics or attempt to manipulate trends.
- **No keyword-only replies**: sending automated replies based on keyword searches alone (without prior opt-in) is prohibited.

## Deeper references (optional)

If you need the detailed docs map or topic guides:
- `references/getting-started.md`
- `references/docs-map.md`
- `references/workflows.md`
- `references/request-shapes.md`
- `references/fundamentals-auth.md`
- `references/apps-and-credentials.md`
