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
