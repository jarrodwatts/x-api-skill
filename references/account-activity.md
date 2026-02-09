# Account Activity API (Webhooks)

Docs entry points:
- `https://docs.x.com/x-api/account-activity/introduction.md`
- `https://docs.x.com/x-api/account-activity/create-subscription.md`
- `https://docs.x.com/x-api/account-activity/get-subscriptions.md`
- `https://docs.x.com/x-api/account-activity/create-replay-job.md`

## What This Is

The Account Activity API delivers real-time user account activity to your webhook (posts, DMs, follows, etc.).

Important detail:
- Some management endpoints are v1.1-style and use `https://api.x.com/1.1/account_activity/...`.

## Webhook Security

From the docs:
- CRC validation
- Signature header: `x-twitter-webhooks-signature`
- HTTPS-only webhook URLs

## Operational Guidance

- Build a replay strategy (see replay job docs).
- Make event processing idempotent.
- Store minimal required data, and apply compliance requirements.

This skill does not include a webhook server implementation; it focuses on correctly calling the management endpoints and understanding the event model.

## Inventory

### Endpoints

- **POST /2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/account-activity/create-replay-job.md`
- **POST /2/account_activity/webhooks/{webhook_id}/subscriptions/all** — Auth: `OAuth2UserToken [dm.read, dm.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/account-activity/create-subscription.md`
- **DELETE /2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/account-activity/delete-subscription.md`
- **GET /2/account_activity/subscriptions/count** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/account-activity/get-subscription-count.md`
- **GET /2/account_activity/webhooks/{webhook_id}/subscriptions/all/list** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/account-activity/get-subscriptions.md`
- **GET /2/account_activity/webhooks/{webhook_id}/subscriptions/all** — Auth: `OAuth2UserToken [dm.read, dm.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/account-activity/validate-subscription.md`

### Docs

- Account Activity API: `https://docs.x.com/x-api/account-activity/introduction.md`
- v2 Account Activity API Migration Guide: `https://docs.x.com/x-api/account-activity/migrate/overview.md`
