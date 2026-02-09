# Bookmarks

Docs entry points:
- `https://docs.x.com/x-api/posts/bookmarks/introduction.md`
- `https://docs.x.com/x-api/posts/bookmarks/quickstart/bookmarks-lookup.md`
- `https://docs.x.com/x-api/posts/bookmarks/quickstart/manage-bookmarks.md`
- `https://docs.x.com/x-api/users/get-bookmarks.md`
- `https://docs.x.com/x-api/users/create-bookmark.md`
- `https://docs.x.com/x-api/users/delete-bookmark.md`

Bookmarks are user-scoped and require user context.

## Key Endpoints

- `GET /2/users/:id/bookmarks` (list bookmarks)
- `POST /2/users/:id/bookmarks` (add bookmark)
- `DELETE /2/users/:id/bookmarks/:tweet_id` (remove bookmark)

Scopes (from the OpenAPI docs):
- read: `bookmark.read` (plus `tweet.read`, `users.read`)
- write: `bookmark.write` (plus `tweet.read`, `users.read`)

The `:id` must match the authenticated user.

## Get My User ID (Recommended)

In autonomous-agent setups, the user usually won’t know their numeric user id.
Fetch it from the user token:

```bash
curl -sS "https://api.x.com/2/users/me" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

Then use `data.id` as `USER_ID` for the bookmark endpoints.

## Lookup Bookmarks

```bash
USER_ID="..."

curl -sS "https://api.x.com/2/users/$USER_ID/bookmarks?max_results=10" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## Add Bookmark

```bash
USER_ID="..."
TWEET_ID="..."

curl -sS -X POST "https://api.x.com/2/users/$USER_ID/bookmarks" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"tweet_id\":\"$TWEET_ID\"}"
```

## Remove Bookmark

```bash
USER_ID="..."
TWEET_ID="..."

curl -sS -X DELETE "https://api.x.com/2/users/$USER_ID/bookmarks/$TWEET_ID" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## Inventory

### Endpoints

- **GET /2/users/{id}/bookmarks/folders/{folder_id}** — Auth: `OAuth2UserToken [bookmark.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/bookmarks/get-bookmarks-by-folder-id.md`
