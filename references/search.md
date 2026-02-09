# Search

Docs entry points:
- `https://docs.x.com/x-api/posts/search/introduction.md`
- `https://docs.x.com/x-api/posts/search/integrate/build-a-query.md`
- `https://docs.x.com/x-api/posts/search/integrate/operators.md`

## Key Endpoints

- `GET /2/tweets/search/recent` (last 7 days)
- `GET /2/tweets/search/all` (full archive, plan dependent)

## Recent Search (cURL)

Example: english posts containing python, excluding retweets.

Use curl's `-G` + `--data-urlencode` to avoid manual URL encoding:
```bash
curl -sS -G "https://api.x.com/2/tweets/search/recent" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  --data-urlencode 'query=python lang:en -is:retweet' \
  --data 'max_results=10' \
  --data 'tweet.fields=created_at'
```

## “What are people saying about X?”

For non-technical prompts like “what are people saying about `<topic>`”, default to **recent search**, cap results, and include author info so you can attribute quotes:

```bash
curl -sS -G "https://api.x.com/2/tweets/search/recent" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  --data-urlencode 'query=<topic> -is:retweet' \
  --data 'max_results=20' \
  --data 'tweet.fields=created_at,lang,public_metrics' \
  --data 'expansions=author_id' \
  --data 'user.fields=username,verified'
```

Pagination guidance:
- If you need “a quick read of the room”, don’t fetch everything—cap pages (for example 1–3) and summarize.
- If the user asks for exhaustive coverage, state the call volume and rate-limit implications up front.

## Full-Archive Search

Same structure as recent search, but the path is `/2/tweets/search/all` and access is plan dependent.

## Pagination

The search response can include `meta.next_token`.
Request the next page with `next_token=<token>`.

Example:
```bash
curl -sS -G "https://api.x.com/2/tweets/search/recent" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  --data-urlencode 'query=python' \
  --data 'max_results=10' \
  --data 'next_token=...'
```

## Output Requirements

When drafting search requests, always specify:
- the exact query string
- whether recent vs full-archive is required
- max results and pagination plan
