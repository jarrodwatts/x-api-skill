# Streams (Filtered Stream)

Docs entry points:
- `https://docs.x.com/x-api/posts/filtered-stream/introduction.md`
- `https://docs.x.com/x-api/posts/filtered-stream/quickstart.md`
- `https://docs.x.com/x-api/posts/filtered-stream/integrate/operators.md`

## Key Endpoints

- `GET /2/tweets/search/stream` (connect)
- `GET /2/tweets/search/stream/rules` (list rules)
- `POST /2/tweets/search/stream/rules` (add/delete rules)

## List Current Rules

```bash
curl -sS "https://api.x.com/2/tweets/search/stream/rules" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Add A Rule

```bash
curl -sS -X POST "https://api.x.com/2/tweets/search/stream/rules" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"add":[{"value":"cat has:images -is:retweet","tag":"cats"}]}'
```

## Delete A Rule

Rule deletions require rule IDs (from the list rules endpoint).

```bash
curl -sS -X POST "https://api.x.com/2/tweets/search/stream/rules" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"delete":{"ids":["1234567890"]}}'
```

## Connect To The Stream

The stream response is long-lived. Use:
- a low timeout
- reconnect logic
- backoff on failures

```bash
curl -sS "https://api.x.com/2/tweets/search/stream?tweet.fields=created_at" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

Operational guidance:
- Ensure the client can handle partial reads.
- If you see disconnects, reconnect with exponential backoff.
- Budget for continuous rate-limit and connection limits.

## Inventory

### Endpoints

- **GET /2/tweets/search/stream/rules/counts** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/get-stream-rule-counts.md`
- **GET /2/tweets/search/stream/rules** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/get-stream-rules.md`
- **GET /2/tweets/sample10/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-10-sampled-posts.md`
- **GET /2/likes/firehose/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-all-likes.md`
- **GET /2/tweets/firehose/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-all-posts.md`
- **GET /2/tweets/firehose/stream/lang/en** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-english-posts.md`
- **GET /2/tweets/search/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-filtered-posts.md`
- **GET /2/tweets/firehose/stream/lang/ja** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-japanese-posts.md`
- **GET /2/tweets/firehose/stream/lang/ko** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-korean-posts.md`
- **GET /2/likes/compliance/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-likes-compliance-data.md`
- **GET /2/tweets/firehose/stream/lang/pt** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-portuguese-posts.md`
- **GET /2/tweets/compliance/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-posts-compliance-data.md`
- **GET /2/likes/sample10/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-sampled-likes.md`
- **GET /2/tweets/sample/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-sampled-posts.md`
- **GET /2/users/compliance/stream** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/stream-users-compliance-data.md`
- **POST /2/tweets/search/stream/rules** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/stream/update-stream-rules.md`
