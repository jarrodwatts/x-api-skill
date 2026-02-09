# X API Skill

Let your AI agent use X (Twitter) on your behalf: post, reply, search, send DMs, bookmark, and follow and more - anything that is possible via the new [X API](https://console.x.com/).

[![License](https://img.shields.io/github/license/jarrodwatts/x-api-skill)](LICENSE)
[![Stars](https://img.shields.io/github/stars/jarrodwatts/x-api-skill)](https://github.com/jarrodwatts/x-api-skill/stargazers)

## Install

Inside a Claude Code instance, run:

**Step 1: Install the skill**

```
npx skills add jarrodwatts/x-api-skill
```

**Step 2: Set your tokens**

Ask your agent how to set up the necessary tokens you need to use the X API, with a prompt such as:

```
Using /x-api-skill - help me set up the necessary tokens to use the X API. 
```

Or see [references/apps-and-credentials.md](references/apps-and-credentials.md) for a more detailed guide.

**Step 3: Start using it**

Just ask Claude what you want to do:

- "Search recent posts about `topic`"
- "Reply to this post with: `...`"
- "Send a DM to `@username` saying `...`"
- "Bookmark post `https://x.com/.../status/123`"
- "Follow `@username`"

Done! The skill handles endpoint selection, auth, pagination, and rate limits automatically.

---

## What It Does

The skill teaches your agent how to use the X API correctly so you don't have to.

| Capability | What Happens |
|------------|--------------|
| **Endpoint selection** | Picks the right method + path for your request |
| **Auth handling** | Bearer for reads, user-context for writes — automatically |
| **Request shaping** | Adds `fields`/`expansions` to minimize API calls |
| **Pagination** | Handles multi-page results with clear stop conditions |
| **Rate limits** | Backs off on `429` using response headers |
| **Error guidance** | Interprets `401/403/429/5xx` with fix-vs-retry advice |
| **Safety** | States side effects and confirms before any write action |

---

## How It Works

The skill is a set of curated guidelines and reference docs that get loaded into your agent's context. When you ask it to do something on X, it:

1. Identifies the right X API v2 endpoint
2. Picks the correct auth mode and scopes
3. Builds the request (using env vars — never inline tokens)
4. For write actions: tells you exactly what it will do and asks for confirmation
5. Executes and handles pagination/errors

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| **401 Unauthorized** | Token missing, invalid, or expired. Regenerate in the [Developer Console](https://console.x.com/). |
| **403 Forbidden** | Missing scopes or insufficient app access level for the endpoint. |
| **429 Too Many Requests** | Rate limited — the agent will back off automatically. Reduce request volume if persistent. |

---

## License

MIT — see [LICENSE](LICENSE)
