# Webhooks

This page is for webhook-style delivery (push, not pull). Most users asking “notify me when … happens” want one of these:

- **Account Activity webhooks** (posts/DMs/follows/etc. delivered to your server): see `references/account-activity.md`
- **Filtered stream** (long-lived connection for matching posts): see `references/streams.md`

## Common prompts this helps with

- “Notify my bot when new posts match `<query>`”
  - Prefer Filtered Stream (`references/streams.md`) unless you need webhook delivery.
- “Replay missed webhook events”
  - Use the replay job endpoint(s) below.

## Inventory

### Endpoints

- **POST /2/webhooks/replay** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/webhooks/create-replay-job-for-webhook.md`
- **POST /2/tweets/search/webhooks/{webhook_id}** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/webhooks/create-stream-link.md`
- **POST /2/webhooks** — Auth: `BearerToken; UserToken` — Doc: `https://docs.x.com/x-api/webhooks/create-webhook.md`
- **DELETE /2/tweets/search/webhooks/{webhook_id}** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/webhooks/delete-stream-link.md`
- **DELETE /2/webhooks/{webhook_id}** — Auth: `BearerToken; UserToken` — Doc: `https://docs.x.com/x-api/webhooks/delete-webhook.md`
- **GET /2/tweets/search/webhooks** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/webhooks/get-stream-links.md`
- **GET /2/webhooks** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/webhooks/get-webhook.md`
- **PUT /2/webhooks/{webhook_id}** — Auth: `BearerToken; UserToken` — Doc: `https://docs.x.com/x-api/webhooks/validate-webhook.md`

### Docs

- Webhooks: `https://docs.x.com/x-api/webhooks/introduction.md`
- Filtered Stream Webhooks API: `https://docs.x.com/x-api/webhooks/stream/introduction.md`
- Quickstart: `https://docs.x.com/x-api/webhooks/stream/quickstart.md`
