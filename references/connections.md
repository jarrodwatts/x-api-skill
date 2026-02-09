# Connections

Docs entry points:
- `https://docs.x.com/x-api/connections/terminate-all-connections.md`

## Key Endpoint

- `DELETE /2/connections/all` (terminate all active streaming connections for the app)

## Terminate All Connections

```bash
curl -sS -X DELETE "https://api.x.com/2/connections/all" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

Use this if your stream clients are stuck or you need to reset streaming sessions.

## Inventory

### Endpoints

- **DELETE /2/connections/all** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/connections/terminate-all-connections.md`
