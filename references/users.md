# Users

Docs entry points:
- `https://docs.x.com/x-api/users/get-user-by-id.md`
- `https://docs.x.com/x-api/users/get-users-by-ids.md`
- `https://docs.x.com/x-api/users/get-user-by-username.md`
- `https://docs.x.com/x-api/users/get-users-by-usernames.md`

## Key Endpoints

- `GET /2/users/:id`
- `GET /2/users` (by `ids=`)
- `GET /2/users/by/username/:username`
- `GET /2/users/by` (by `usernames=`)
- `GET /2/users/me` (the authenticated user)

## Get My User (Autonomous Agents)

When a user asks “my bookmarks”, “my likes”, “my follows”, etc., an autonomous agent usually needs the authenticated user id.

Use:
- `GET /2/users/me`

```bash
curl -sS "https://api.x.com/2/users/me" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

This requires OAuth 2.0 user context. It’s the simplest way to get the correct `USER_ID` for user-scoped endpoints.

## Get User By Username

```bash
curl -sS "https://api.x.com/2/users/by/username/xdevelopers?user.fields=created_at,description,public_metrics" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Get User By ID

```bash
USER_ID="2244994945"

curl -sS "https://api.x.com/2/users/$USER_ID?user.fields=created_at,description,public_metrics" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Multiple Users

```bash
curl -sS "https://api.x.com/2/users?ids=2244994945,6253282&user.fields=username,created_at" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Common Gotchas

- Preserve IDs as strings.
- Add `user.fields` explicitly when you need non-default attributes.

## Inventory

### Endpoints

- **POST /2/users/{id}/dm/block** — Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/block-dms.md`
- **POST /2/users/{id}/bookmarks** — Auth: `OAuth2UserToken [bookmark.write, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/users/create-bookmark.md`
- **DELETE /2/users/{id}/bookmarks/{tweet_id}** — Auth: `OAuth2UserToken [bookmark.write, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/users/delete-bookmark.md`
- **POST /2/users/{id}/followed_lists** — Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/follow-list.md`
- **POST /2/users/{id}/following** — Auth: `OAuth2UserToken [follows.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/follow-user.md`
- **GET /2/users/{id}/blocking** — Auth: `OAuth2UserToken [block.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-blocking.md`
- **GET /2/users/{id}/bookmarks/folders** — Auth: `OAuth2UserToken [bookmark.read, users.read]` — Doc: `https://docs.x.com/x-api/users/get-bookmark-folders.md`
- **GET /2/users/{id}/bookmarks** — Auth: `OAuth2UserToken [bookmark.read, tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/users/get-bookmarks.md`
- **GET /2/users/{id}/followed_lists** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-followed-lists.md`
- **GET /2/users/{id}/followers** — Auth: `BearerToken; OAuth2UserToken [follows.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-followers.md`
- **GET /2/users/{id}/following** — Auth: `BearerToken; OAuth2UserToken [follows.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-following.md`
- **GET /2/users/{id}/liked_tweets** — Auth: `OAuth2UserToken [like.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-liked-posts.md`
- **GET /2/users/{id}/list_memberships** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-list-memberships.md`
- **GET /2/users/{id}/mentions** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-mentions.md`
- **GET /2/users/{id}/muting** — Auth: `OAuth2UserToken [mute.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-muting.md`
- **GET /2/users/me** — Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-my-user.md`
- **GET /2/users/{id}/owned_lists** — Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-owned-lists.md`
- **GET /2/users/{id}/pinned_lists** — Auth: `OAuth2UserToken [list.read, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-pinned-lists.md`
- **GET /2/users/{id}/tweets** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-posts.md`
- **GET /2/users/reposts_of_me** — Auth: `OAuth2UserToken [timeline.read, tweet.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-reposts-of-me.md`
- **GET /2/users/{id}/timelines/reverse_chronological** — Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-timeline.md`
- **GET /2/users/{id}** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-user-by-id.md`
- **GET /2/users/by/username/{username}** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-user-by-username.md`
- **GET /2/users** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-users-by-ids.md`
- **GET /2/users/by** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/get-users-by-usernames.md`
- **POST /2/users/{id}/likes** — Auth: `OAuth2UserToken [like.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/like-post.md`
- **POST /2/users/{id}/muting** — Auth: `OAuth2UserToken [mute.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/mute-user.md`
- **POST /2/users/{id}/pinned_lists** — Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/pin-list.md`
- **POST /2/users/{id}/retweets** — Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/repost-post.md`
- **GET /2/users/search** — Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/users/search-users.md`
- (and 7 more endpoints; see `references/x-api-catalog.md`)

### Docs

- Integration Guide: `https://docs.x.com/x-api/users/blocks/integrate.md`
- Blocks: `https://docs.x.com/x-api/users/blocks/introduction.md`
- Quickstart: `https://docs.x.com/x-api/users/blocks/quickstart.md`
- Follows: `https://docs.x.com/x-api/users/follows/introduction.md`
- Quickstart: `https://docs.x.com/x-api/users/follows/quickstart.md`
- Integration Guide: `https://docs.x.com/x-api/users/lookup/integrate.md`
- User Lookup: `https://docs.x.com/x-api/users/lookup/introduction.md`
- Authenticated User Quickstart: `https://docs.x.com/x-api/users/lookup/quickstart/authenticated-lookup.md`
- User Lookup Quickstart: `https://docs.x.com/x-api/users/lookup/quickstart/user-lookup.md`
- Integration Guide: `https://docs.x.com/x-api/users/mutes/integrate.md`
- Mutes: `https://docs.x.com/x-api/users/mutes/introduction.md`
- Manage Mutes: `https://docs.x.com/x-api/users/mutes/quickstart/manage-mutes-quickstart.md`
- Mutes Lookup: `https://docs.x.com/x-api/users/mutes/quickstart/mutes-lookup.md`
- User Search: `https://docs.x.com/x-api/users/search/introduction.md`
