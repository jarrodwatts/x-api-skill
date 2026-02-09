# Direct Messages

Docs entry points:
- `https://docs.x.com/x-api/direct-messages/lookup/introduction.md`
- `https://docs.x.com/x-api/direct-messages/manage/introduction.md`
- `https://docs.x.com/x-api/direct-messages/get-dm-events.md`
- `https://docs.x.com/x-api/direct-messages/create-dm-conversation.md`
- `https://docs.x.com/x-api/direct-messages/create-dm-message-by-conversation-id.md`
- `https://docs.x.com/x-api/direct-messages/create-dm-message-by-participant-id.md`
- `https://docs.x.com/x-api/direct-messages/get-dm-event-by-id.md`
- `https://docs.x.com/x-api/direct-messages/delete-dm-event.md`

## Key Endpoints (Common)

- `GET /2/dm_events` (recent DM events)
- `GET /2/dm_events/:event_id` (event by ID)
- `DELETE /2/dm_events/:event_id` (delete event)
- `POST /2/dm_conversations` (create conversation)
- `POST /2/dm_conversations/:dm_conversation_id/messages` (send message to a conversation)
- `POST /2/dm_conversations/with/:participant_id/messages` (send message to a participant)
- `GET /2/dm_conversations/with/:participant_id/dm_events` (events for a conversation with a participant)

DM endpoints require user context (OAuth 2.0 user token). Typical scopes:
- read: `dm.read` (plus `tweet.read`, `users.read` used by the docs)
- write: `dm.write` (plus `tweet.read`, `users.read`)

## Get Recent DM Events

```bash
curl -sS "https://api.x.com/2/dm_events" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## Get DM Events With A Participant

```bash
PARTICIPANT_ID="..."

curl -sS "https://api.x.com/2/dm_conversations/with/$PARTICIPANT_ID/dm_events" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## Send A DM Message (By Conversation)

```bash
CONV_ID="..."

curl -sS -X POST "https://api.x.com/2/dm_conversations/$CONV_ID/messages" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello"}'
```

## Send A DM Message (By Participant)

```bash
PARTICIPANT_ID="..."

curl -sS -X POST "https://api.x.com/2/dm_conversations/with/$PARTICIPANT_ID/messages" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello"}'
```

Write notes:
- Sending messages has user-visible side effects.
- Validate conversation and participant IDs before sending.

## Inventory

### Endpoints

- **POST /2/dm_conversations** — Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/create-dm-conversation.md`
- **POST /2/dm_conversations/{dm_conversation_id}/messages** — Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/create-dm-message-by-conversation-id.md`
- **POST /2/dm_conversations/with/{participant_id}/messages** — Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/create-dm-message-by-participant-id.md`
- **DELETE /2/dm_events/{event_id}** — Auth: `OAuth2UserToken [dm.read, dm.write]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/delete-dm-event.md`
- **GET /2/dm_events/{event_id}** — Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/get-dm-event-by-id.md`
- **GET /2/dm_conversations/{id}/dm_events** — Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/get-dm-events-for-a-dm-conversation-1.md`
- **GET /2/dm_conversations/with/{participant_id}/dm_events** — Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/get-dm-events-for-a-dm-conversation.md`
- **GET /2/dm_events** — Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/direct-messages/get-dm-events.md`

### Docs

- Introduction: `https://docs.x.com/x-api/direct-messages/blocks/introduction.md`
- Integration Guide: `https://docs.x.com/x-api/direct-messages/lookup/integrate.md`
- Direct Messages Lookup: `https://docs.x.com/x-api/direct-messages/lookup/introduction.md`
- Quickstart: `https://docs.x.com/x-api/direct-messages/lookup/quickstart.md`
- Integration Guide: `https://docs.x.com/x-api/direct-messages/manage/integrate.md`
- Manage Direct Messages: `https://docs.x.com/x-api/direct-messages/manage/introduction.md`
- Quickstart: `https://docs.x.com/x-api/direct-messages/manage/quickstart.md`
