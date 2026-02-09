# Communities

Docs entry points:
- `https://docs.x.com/x-api/communities/lookup/introduction.md`
- `https://docs.x.com/x-api/communities/get-community-by-id.md`
- `https://docs.x.com/x-api/communities/search/introduction.md`
- `https://docs.x.com/x-api/communities/search-communities.md`

## Key Endpoints

- `GET /2/communities/:id`
- Search endpoints, see docs (keyword-based)

## Get Community By ID

```bash
COMMUNITY_ID="..."

curl -sS "https://api.x.com/2/communities/$COMMUNITY_ID" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

Community membership and visibility can affect what you can see. Prefer user context if the docs indicate it.

## Inventory

### Endpoints

- **GET /2/communities/{id}** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/communities/get-community-by-id.md`
- **GET /2/communities/search** — Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/communities/search-communities.md`

### Docs

- Communities Lookup: `https://docs.x.com/x-api/communities/lookup/introduction.md`
- Communities Search: `https://docs.x.com/x-api/communities/search/introduction.md`
