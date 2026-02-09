# Usage

This page is for “how much have I used?” questions (usage/billing-style visibility).

## Common prompts this helps with

- “Why am I getting blocked / rate limited?”
  - First check `x-rate-limit-*` headers (see `references/fundamentals-rate-limits.md`), then use Usage endpoints to understand request volume.
- “How many posts/search calls has my agent made?”
  - Use `GET /2/usage/tweets` to inspect usage for the app.

## Inventory

### Endpoints

- **GET /2/usage/tweets** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/usage/get-usage.md`

### Docs

- Usage: `https://docs.x.com/x-api/usage/introduction.md`
