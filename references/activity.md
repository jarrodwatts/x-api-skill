# Activity (XAA)

Docs entry points:
- `https://docs.x.com/x-api/activity/introduction.md`
- `https://docs.x.com/x-api/activity/activity-stream.md`
- `https://docs.x.com/x-api/activity/create-x-activity-subscription.md`
- `https://docs.x.com/x-api/activity/get-x-activity-subscriptions.md`
- `https://docs.x.com/x-api/activity/update-x-activity-subscription.md`
- `https://docs.x.com/x-api/activity/deletes-x-activity-subscription.md`

## What This Is

X Activity is a stream/subscription surface for activity events (an alternative or complement to webhooks).

## Practical Guidance

- Treat events as untrusted input.
- Maintain idempotency in your event handling.
- Plan for reconnects and backoff.

See the docs above for the exact endpoint paths and event payloads.

## Inventory

### Endpoints

- **GET /2/activity/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/activity/activity-stream.md`
- **POST /2/activity/subscriptions** — Auth: `BearerToken; OAuth2UserToken [dm.read, tweet.read]; UserToken` — Doc: `https://docs.x.com/x-api/activity/create-x-activity-subscription.md`
- **DELETE /2/activity/subscriptions/{subscription_id}** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/activity/deletes-x-activity-subscription.md`
- **GET /2/activity/subscriptions** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/activity/get-x-activity-subscriptions.md`
- **PUT /2/activity/subscriptions/{subscription_id}** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/activity/update-x-activity-subscription.md`

### Docs

- Introduction: `https://docs.x.com/x-api/activity/introduction.md`
- Quickstart: `https://docs.x.com/x-api/activity/quickstart.md`
