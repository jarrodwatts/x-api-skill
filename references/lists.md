# Lists

Docs entry points:
- `https://docs.x.com/x-api/lists/list-lookup/introduction.md`
- `https://docs.x.com/x-api/lists/manage-lists/introduction.md`
- `https://docs.x.com/x-api/lists/get-list-by-id.md`
- `https://docs.x.com/x-api/lists/get-list-posts.md`
- `https://docs.x.com/x-api/lists/create-list.md`
- `https://docs.x.com/x-api/lists/update-list.md`
- `https://docs.x.com/x-api/lists/delete-list.md`

## Key Endpoints (Common)

- `GET /2/lists/:id`
- `POST /2/lists` (create)
- `PUT /2/lists/:id` (update)
- `DELETE /2/lists/:id` (delete)
- `GET /2/lists/:id/tweets` (list timeline)

See the full list of list endpoints in the docs index (`docs-map.md`).

## Get List By ID

```bash
LIST_ID="..."

curl -sS "https://api.x.com/2/lists/$LIST_ID" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Get List Posts

```bash
LIST_ID="..."

curl -sS "https://api.x.com/2/lists/$LIST_ID/tweets?max_results=10" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Create List

```bash
curl -sS -X POST "https://api.x.com/2/lists" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"my list","private":true}'
```

## Update List

```bash
LIST_ID="..."

curl -sS -X PUT "https://api.x.com/2/lists/$LIST_ID" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"description":"updated description"}'
```

## Delete List

```bash
LIST_ID="..."

curl -sS -X DELETE "https://api.x.com/2/lists/$LIST_ID" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## Write Notes

Creating/updating/deleting Lists requires user context (OAuth 2.0 user token).

Typical scopes (from the OpenAPI docs):
- create: `list.write`, `list.read`, `tweet.read`, `users.read`
- update/delete: `list.write`, `tweet.read`, `users.read`

List reads can allow Bearer token, but some list read endpoints may require `list.read` depending on access and the target list.
When drafting write calls, state the side effect and required scopes.

## Inventory

### Endpoints

- **POST /2/lists/{id}/members** — Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/add-list-member.md`
- **POST /2/lists** — Auth: `OAuth2UserToken [list.read, list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/create-list.md`
- **DELETE /2/lists/{id}** — Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/delete-list.md`
- **GET /2/lists/{id}** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/get-list-by-id.md`
- **GET /2/lists/{id}/followers** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/get-list-followers.md`
- **GET /2/lists/{id}/members** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/get-list-members.md`
- **GET /2/lists/{id}/tweets** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/get-list-posts.md`
- **DELETE /2/lists/{id}/members/{user_id}** — Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/remove-list-member.md`
- **PUT /2/lists/{id}** — Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/lists/update-list.md`

### Docs

- Integration Guide: `https://docs.x.com/x-api/lists/list-lookup/integrate.md`
- List Lookup: `https://docs.x.com/x-api/lists/list-lookup/introduction.md`
- Quickstart: `https://docs.x.com/x-api/lists/list-lookup/quickstart.md`
- Integration guide: `https://docs.x.com/x-api/lists/list-members/integrate.md`
- List Members: `https://docs.x.com/x-api/lists/list-members/introduction.md`
- List Members Lookup: `https://docs.x.com/x-api/lists/list-members/quickstart/list-members-lookup.md`
- Manage List Members: `https://docs.x.com/x-api/lists/list-members/quickstart/manage-list-members.md`
- List Members Overview: `https://docs.x.com/x-api/lists/list-members/quickstart/overview.md`
- Integration guide: `https://docs.x.com/x-api/lists/list-tweets/integrate.md`
- List Posts: `https://docs.x.com/x-api/lists/list-tweets/introduction.md`
- Quickstart: `https://docs.x.com/x-api/lists/list-tweets/quickstart.md`
- Integration guide: `https://docs.x.com/x-api/lists/manage-lists/integrate.md`
- Manage Lists: `https://docs.x.com/x-api/lists/manage-lists/introduction.md`
- Quickstart: `https://docs.x.com/x-api/lists/manage-lists/quickstart.md`
- Integration guide: `https://docs.x.com/x-api/lists/pinned-lists/integrate.md`
- Pinned Lists: `https://docs.x.com/x-api/lists/pinned-lists/introduction.md`
- Manage Pinned Lists: `https://docs.x.com/x-api/lists/pinned-lists/quickstart/manage-pinned-lists.md`
- Pinned Lists Overview: `https://docs.x.com/x-api/lists/pinned-lists/quickstart/overview.md`
- Pinned Lists Lookup: `https://docs.x.com/x-api/lists/pinned-lists/quickstart/pinned-list-lookup.md`
