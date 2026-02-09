# Trends

Docs entry points:
- `https://docs.x.com/x-api/trends/trends-by-woeid/introduction.md`
- `https://docs.x.com/x-api/trends/personalized-trends/introduction.md`
- `https://docs.x.com/x-api/trends/get-trends-by-woeid.md`
- `https://docs.x.com/x-api/trends/get-personalized-trends.md`

## Key Endpoints

- `GET /2/trends/by/woeid/:woeid`
- `GET /2/users/personalized_trends` (user-context)

## Trends By WOEID

```bash
WOEID="1"

curl -sS "https://api.x.com/2/trends/by/woeid/$WOEID" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Personalized Trends

Personalized trends are per-user and require user context.

```bash
curl -sS "https://api.x.com/2/users/personalized_trends" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

Typical scopes (from the OpenAPI docs): `tweet.read`, `users.read`.

## Inventory

### Endpoints

- **GET /2/users/personalized_trends** — Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/trends/get-personalized-trends.md`
- **GET /2/trends/by/woeid/{woeid}** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/trends/get-trends-by-woeid.md`

### Docs

- Personalized Trends: `https://docs.x.com/x-api/trends/personalized-trends/introduction.md`
- Trends by WOEID: `https://docs.x.com/x-api/trends/trends-by-woeid/introduction.md`
