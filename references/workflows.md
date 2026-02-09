# Common Workflows

This file is the “what should my agent do?” guide.

## Common non-technical prompts → what the agent should do

- “Tweet this: `...`”
  - Use `POST /2/tweets` (requires OAuth user context: `X_USER_ACCESS_TOKEN` + `tweet.write`).
- “Reply to this post: `https://x.com/.../status/123` with `...`”
  - Extract the post id from the URL, then `POST /2/tweets` with `reply.in_reply_to_tweet_id`.
- “What are people saying about `X` on Twitter?”
  - Use `GET /2/tweets/search/recent`, cap results/pages, and include author info via `expansions=author_id`.
- “What are my bookmarks?”
  - First call `GET /2/users/me` to get the authenticated user id, then call `GET /2/users/:id/bookmarks`.
- “Send a DM to `@username` saying `...`”
  - Use `GET /2/users/by/username/:username` to get the participant id, then `POST /2/dm_conversations/with/:participant_id/messages`.
- “What are my likes / who do I follow / who follows me?”
  - First call `GET /2/users/me`, then call the appropriate `GET /2/users/:id/...` endpoint (likes/followers/following).

## Fetch A Post With Author Details

Use:
- `GET /2/tweets/:id`

Pattern:
- add `tweet.fields=` for the Post fields you actually need
- add `expansions=author_id`
- add `user.fields=` to get author fields

Example:
```bash
POST_ID="..."

curl -sS "https://api.x.com/2/tweets/$POST_ID?tweet.fields=created_at,public_metrics&expansions=author_id&user.fields=username" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Search For Posts

Choose:
- recent: `GET /2/tweets/search/recent`
- full archive: `GET /2/tweets/search/all` (plan dependent)

Rules of thumb:
- Use curl `-G` and `--data-urlencode` for the `query=` parameter.
- Start with a small `max_results` while iterating.
- Paginate with `next_token` only when you have to.

## Stream Matching Posts

Choose filtered stream when you need near real-time delivery.

Flow:
1. `GET /2/tweets/search/stream/rules` to inspect current rules.
2. `POST /2/tweets/search/stream/rules` to add/delete.
3. `GET /2/tweets/search/stream` to connect.

Operational notes:
- Treat streams as long-lived connections.
- Implement reconnect with backoff.

## Create Or Delete A Post

Create:
- `POST /2/tweets` (OAuth 2.0 user context, `tweet.write`)

Delete:
- `DELETE /2/tweets/:id` (OAuth 2.0 user context, `tweet.write`)

Always state the side effect and confirm the target ID.

Tip: users often paste X links. The post id is the digits after `/status/` (treat it as a string).

## Send A Direct Message

Flow:
1. Resolve the recipient:
   - `GET /2/users/by/username/:username` → `data.id` = `PARTICIPANT_ID`
2. Send message:
   - `POST /2/dm_conversations/with/:participant_id/messages`

DM calls require OAuth 2.0 user context and `dm.write`.

## Manage Bookmarks

Flow:
1. List: `GET /2/users/:id/bookmarks` (`bookmark.read`)
2. Add: `POST /2/users/:id/bookmarks` (`bookmark.write`)
3. Remove: `DELETE /2/users/:id/bookmarks/:tweet_id` (`bookmark.write`)

The `:id` must match the authenticated user.

## Build Compliance Into Your Storage

Compliance is how you keep stored data accurate over time.

Common pattern:
1. Create a job: `POST /2/compliance/jobs`
2. Upload the input set if required by the job type.
3. Poll the job: `GET /2/compliance/jobs/:id`
4. Download results and apply mutations to your datastore.

Important:
- Treat compliance processing as part of your ingestion pipeline, not an afterthought.
- Keep job ids and status transitions observable.

## Account Activity Webhooks (High Level)

Flow:
1. Register webhook.
2. Subscribe users.
3. Receive events at your webhook.

Security notes:
- Verify CRC and request signatures.
- Make event processing idempotent.

Use this skill's `account-activity.md` for the event model and doc links.
