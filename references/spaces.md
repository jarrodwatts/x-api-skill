# Spaces

Docs entry points:
- `https://docs.x.com/x-api/spaces/introduction.md`
- `https://docs.x.com/x-api/spaces/lookup/introduction.md`
- `https://docs.x.com/x-api/spaces/search/introduction.md`
- `https://docs.x.com/x-api/spaces/get-space-by-id.md`
- `https://docs.x.com/x-api/spaces/get-spaces-by-ids.md`
- `https://docs.x.com/x-api/spaces/search-spaces.md`
- `https://docs.x.com/x-api/spaces/get-space-posts.md`

## Key Endpoints (Common)

- `GET /2/spaces/:id`
- `GET /2/spaces` (lookup by ids)
- `GET /2/spaces/by/creator_ids` (lookup by creator)
- `GET /2/spaces/search` (search)
- `GET /2/spaces/:id/tweets` (posts in a space)

Auth notes (from the OpenAPI docs):
- Many Space endpoints allow Bearer token, and also allow OAuth 2.0 user context with `space.read`, `tweet.read`, `users.read`.

## Get Space By ID

```bash
SPACE_ID="..."

curl -sS "https://api.x.com/2/spaces/$SPACE_ID" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Get Spaces By IDs

```bash
curl -sS -G "https://api.x.com/2/spaces" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  --data 'ids=1SLjjRYNejbKM,1YqKDqWqdPLsV'
```

## Get Space Posts

```bash
SPACE_ID="..."

curl -sS "https://api.x.com/2/spaces/$SPACE_ID/tweets?max_results=10" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Search Spaces

```bash
curl -sS -G "https://api.x.com/2/spaces/search" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  --data-urlencode 'query=ai'
```

## Inventory

### Endpoints

- **GET /2/spaces/{id}** — Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/spaces/get-space-by-id.md`
- **GET /2/spaces/{id}/tweets** — Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/spaces/get-space-posts.md`
- **GET /2/spaces/{id}/buyers** — Auth: `OAuth2UserToken [space.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/spaces/get-space-ticket-buyers.md`
- **GET /2/spaces/by/creator_ids** — Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/spaces/get-spaces-by-creator-ids.md`
- **GET /2/spaces** — Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/spaces/get-spaces-by-ids.md`
- **GET /2/spaces/search** — Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/spaces/search-spaces.md`

### Docs

- Introduction: `https://docs.x.com/x-api/spaces/introduction.md`
- Spaces Lookup: `https://docs.x.com/x-api/spaces/lookup/introduction.md`
- Quickstart: `https://docs.x.com/x-api/spaces/lookup/quickstart.md`
- Spaces Search: `https://docs.x.com/x-api/spaces/search/introduction.md`
- Quickstart: `https://docs.x.com/x-api/spaces/search/quickstart.md`
