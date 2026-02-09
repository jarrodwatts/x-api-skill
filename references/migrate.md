# Migrate

This page is for migration guidance (for example, moving from older Twitter API surfaces to X API v2).

## Common prompts this helps with

- “I used to call v1.1 `statuses/user_timeline` — what’s the v2 equivalent?”
  - Use the endpoint map docs below, then confirm auth/scopes using `references/fundamentals-auth.md`.
- “Why did my old auth stop working?”
  - Prefer OAuth 2.0 user context for v2 user actions; see `references/apps-and-credentials.md`.

## Inventory

### Docs

- Data Formation Migration: `https://docs.x.com/x-api/migrate/data-format-migration.md`
- Overview: `https://docs.x.com/x-api/migrate/overview.md`
- X API endpoint map: `https://docs.x.com/x-api/migrate/x-api-endpoint-map.md`
