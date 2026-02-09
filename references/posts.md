# Posts (Tweets)

Docs entry points:
- `https://docs.x.com/x-api/posts/lookup/introduction.md`
- `https://docs.x.com/x-api/posts/get-post-by-id.md`
- `https://docs.x.com/x-api/posts/get-posts-by-ids.md`
- `https://docs.x.com/x-api/posts/create-post.md`
- `https://docs.x.com/x-api/posts/delete-post.md`

## Key Endpoints

- `GET /2/tweets/:id` (single Post)
- `GET /2/tweets` (multiple Posts by id list)
- `POST /2/tweets` (create or edit)
- `DELETE /2/tweets/:id` (delete)

## Get Post By ID

Typical auth:
- Bearer token OR OAuth 2.0 user token (depends on access and the target).

Example (request fields and author expansion):
```bash
POST_ID="1460323737035677698"

curl -sS "https://api.x.com/2/tweets/$POST_ID?tweet.fields=created_at,public_metrics&expansions=author_id&user.fields=username" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Get Posts By IDs

Example:
```bash
IDS="1460323737035677698,1460323737035677699"

curl -sS "https://api.x.com/2/tweets?ids=$IDS&tweet.fields=created_at,public_metrics" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Create Post

Requires user context.

Example (simple text post):
```bash
curl -sS "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello from the X API"}'
```

## Reply To A Post

If the user gives a link like `https://x.com/<handle>/status/<id>`, the post id is the digits after `/status/`.

```bash
IN_REPLY_TO_TWEET_ID="..."

curl -sS "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"reply text\",\"reply\":{\"in_reply_to_tweet_id\":\"$IN_REPLY_TO_TWEET_ID\"}}"
```

## Quote A Post

```bash
QUOTE_TWEET_ID="..."

curl -sS "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"your commentary\",\"quote_tweet_id\":\"$QUOTE_TWEET_ID\"}"
```

Notes:
- The create payload supports more than `text` (reply, quote, media, edit options, etc.). See the OpenAPI schema in the docs.
 - If a post fails validation, treat the error response as authoritative. See `fundamentals-counting-characters.md`.

## Delete Post

Requires user context and ownership.

Example:
```bash
POST_ID="1460323737035677698"

curl -sS -X DELETE "https://api.x.com/2/tweets/$POST_ID" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## Common Gotchas

- IDs are strings. Do not parse as numbers.
- Prefer `tweet.fields` and `expansions` up front to avoid N+1 calls.
- For write calls: state the side effect.

## Inventory

### Endpoints

- **POST /2/tweets** — Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/create-post.md`
- **DELETE /2/tweets/{id}** — Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/delete-post.md`
- **GET /2/tweets/counts/all** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/posts/get-count-of-all-posts.md`
- **GET /2/tweets/counts/recent** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/posts/get-count-of-recent-posts.md`
- **GET /2/tweets/{id}/liking_users** — Auth: `OAuth2UserToken [like.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-liking-users.md`
- **GET /2/tweets/analytics** — Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-post-analytics.md`
- **GET /2/tweets/{id}** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-post-by-id.md`
- **GET /2/tweets** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-posts-by-ids.md`
- **GET /2/tweets/{id}/quote_tweets** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-quoted-posts.md`
- **GET /2/tweets/{id}/retweeted_by** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-reposted-by.md`
- **GET /2/tweets/{id}/retweets** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/get-reposts.md`
- **PUT /2/tweets/{tweet_id}/hidden** — Auth: `OAuth2UserToken [tweet.moderate.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/hide-reply.md`
- **GET /2/tweets/search/all** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/posts/search-all-posts.md`
- **GET /2/tweets/search/recent** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/posts/search-recent-posts.md`

### Docs

- Integration guide: `https://docs.x.com/x-api/posts/bookmarks/integrate.md`
- Bookmarks: `https://docs.x.com/x-api/posts/bookmarks/introduction.md`
- Bookmarks Lookup: `https://docs.x.com/x-api/posts/bookmarks/quickstart/bookmarks-lookup.md`
- Manage Bookmarks: `https://docs.x.com/x-api/posts/bookmarks/quickstart/manage-bookmarks.md`
- Build a query: `https://docs.x.com/x-api/posts/counts/integrate/build-a-query.md`
- Overview: `https://docs.x.com/x-api/posts/counts/integrate/overview.md`
- Post Counts: `https://docs.x.com/x-api/posts/counts/introduction.md`
- Full-Archive Post Counts: `https://docs.x.com/x-api/posts/counts/quickstart/full-archive-tweet-counts.md`
- Recent Post Counts: `https://docs.x.com/x-api/posts/counts/quickstart/recent-tweet-counts.md`
- Build a rule: `https://docs.x.com/x-api/posts/filtered-stream/integrate/build-a-rule.md`
- Matching Posts to Rules: `https://docs.x.com/x-api/posts/filtered-stream/integrate/matching-returned-tweets.md`
- Filtered Stream Operators: `https://docs.x.com/x-api/posts/filtered-stream/integrate/operators.md`
- Filtered Stream: `https://docs.x.com/x-api/posts/filtered-stream/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/filtered-stream/quickstart.md`
- Apps: `https://docs.x.com/x-api/posts/hide-replies/apps.md`
- Manage replies by topic: `https://docs.x.com/x-api/posts/hide-replies/integrate/manage-replies-by-topic.md`
- Manage replies by topic: `https://docs.x.com/x-api/posts/hide-replies/integrate/manage-replies-in-realtime.md`
- Hide Replies: `https://docs.x.com/x-api/posts/hide-replies/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/hide-replies/quickstart.md`
- Likes: `https://docs.x.com/x-api/posts/likes/introduction.md`
- (and 27 more; see `autogen/posts.md`)
