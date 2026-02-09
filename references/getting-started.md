# Getting Started

## First-time setup (autonomous agent)

If you just installed this skill into an autonomous agent, do this once:

1. Create an app in the [Developer Console](https://console.x.com/).
2. Decide what you need:
   - **Read-only** (public data): generate a **Bearer Token**
   - **User actions** (post/reply/delete, bookmarks, DMs, follow/unfollow): configure **OAuth 2.0**
3. If using OAuth 2.0, add an allowlisted **callback URL** (exact match; local dev should use `http://127.0.0.1`).
4. Complete the one-time OAuth authorization to obtain a user access token (and refresh token if provided).
5. Store credentials securely and set environment variables (never commit them).

Common env vars:
```bash
export X_BEARER_TOKEN="..."
export X_USER_ACCESS_TOKEN="..."
export X_CLIENT_ID="..."
export X_CLIENT_SECRET="..." # only if your OAuth 2.0 app type has one
```

Next:
- Console setup + credential mapping: `references/apps-and-credentials.md`
- How to pick auth + scopes for an endpoint: `references/fundamentals-auth.md`

## Inventory

### Docs

- About the X API: `https://docs.x.com/x-api/getting-started/about-x-api.md`
- Getting Access: `https://docs.x.com/x-api/getting-started/getting-access.md`
- Important Resources: `https://docs.x.com/x-api/getting-started/important-resources.md`
- Make Your First Request: `https://docs.x.com/x-api/getting-started/make-your-first-request.md`
- Pricing: `https://docs.x.com/x-api/getting-started/pricing.md`
- X API: `https://docs.x.com/x-api/introduction.md`
- What to Build: `https://docs.x.com/x-api/what-to-build.md`
