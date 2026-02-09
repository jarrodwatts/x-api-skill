# Apps & Credentials (Developer Console)

This guide is written for an **autonomous agent** setup (OpenClaw / Clawdbot-style): you create an app once, generate credentials once, store them as secrets, and then your agent can post/search/DM on your behalf.

It also maps the Developer Console credentials to the environment variables this skill expects.

## Create an app

1. Go to [console.x.com](https://console.x.com/) and sign in.
2. Create an app (name, description, use case).
3. Generate the credentials you need.
4. Store credentials securely (they may only be shown once).

## Autonomous agent credential paths (choose one)

Pick based on what you want the agent to do:

### Option A: Read-only agent (no posting / no DMs)

Use this if your agent only needs public reads (lookups, public search, etc.).

1. In the app’s credentials, generate a **Bearer Token**.
2. Store it as `X_BEARER_TOKEN`.

That’s it—no callback URL and no user authorization step needed.

### Option B: Agent that performs user actions (post / reply / delete / bookmark / DM / follow)

Use this if your agent needs to act *as a user*.

1. Configure **OAuth 2.0** for your app (choose an app type that matches where the agent runs).
2. Add a **callback URL** (redirect URI) that your agent setup will use.
3. Run a **one-time authorization** (you will be asked to open an authorize URL, approve the app, then paste/return a code).
4. Store the resulting **user access token** as `X_USER_ACCESS_TOKEN`.
   - If the token exchange also returns a **refresh token**, store that too (your agent host may manage refresh automatically; otherwise you’ll re-authorize when tokens expire).

Tip: prefer **OAuth 2.0** for new projects because it supports fine-grained scopes and is required for many v2 user-context endpoints.

## Credential types (Console → what it’s for)

- **API Key & Secret**
  - OAuth 1.0a (signing requests / legacy flows)
- **Access Token & Secret**
  - OAuth 1.0a “user context” for your own account
- **Client ID & Secret**
  - OAuth 2.0 authorization code flow (server-side app types)
- **Bearer Token**
  - App-only auth for public data endpoints

## Map Console credentials to env vars (this skill)

- `X_BEARER_TOKEN` → **Bearer Token**
- `X_CLIENT_ID` → **Client ID** (OAuth 2.0)
- `X_CLIENT_SECRET` → **Client Secret** (OAuth 2.0, only if your app type has one)
- `X_USER_ACCESS_TOKEN` → **OAuth 2.0 user access token** (after the one-time authorization)

Security note: never commit or paste tokens into chats. Use environment variables or a secrets manager. See `references/fundamentals-security.md`.

## OAuth 2.0 app type (important)

When configuring OAuth 2.0, choose the app type that matches where your agent runs:

- **Automated App / Bot** (confidential)
  - Best default for autonomous agents running on a server (gets a Client Secret).
- **Web App** (confidential)
  - Server-side web apps (gets a Client Secret).
- **Native App** (public)
  - Mobile/desktop apps (no Client Secret; PKCE only).
- **Single Page App** (public)
  - Browser JS apps (no Client Secret; PKCE only).

## Callback URLs (redirect URIs)

For OAuth flows, you must allowlist callback URLs in the Developer Console. This is the most common place people get stuck.

Rules to remember:
- Must match exactly (including trailing slashes).
- Up to 10 callback URLs per app.
- Use `https://` in production.
- For local dev, prefer `http://127.0.0.1` (not `localhost`).

If you see “Callback URL not approved”, your callback URL likely doesn’t match exactly what’s allowlisted.

Practical guidance for autonomous agents:
- If your agent host provides a callback URL, **use that exact URL**.
- If you’re doing a local “one-time setup” flow, use a loopback callback like `http://127.0.0.1:<port>/callback` and have your setup tool capture the authorization code.

## Permissions/scopes

- OAuth 1.0a uses permission levels (read, read+write, read+write+DMs).
- OAuth 2.0 uses **scopes**.

If you change permissions/scopes, users usually must re-authorize the app to obtain tokens with the updated access.

For autonomous agents, the safest default is:
- Request only scopes you need for the tasks you intend to automate.
- Keep “write” scopes out of a read-only agent.

## Where to go next

- Auth mode decisioning and flows: `references/fundamentals-auth.md`
- Security/storage guidance: `references/fundamentals-security.md`
- Common tasks and endpoints: `references/workflows.md`, `references/docs-map.md`

