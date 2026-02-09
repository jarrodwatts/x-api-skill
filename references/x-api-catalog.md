# X API Catalog (Comprehensive)

This file enumerates every `x-api/*` page from `docs.x.com/llms.txt`.

- For OpenAPI pages, we extract `METHOD PATH`, security schemes/scopes, and generate a curl skeleton.
- For non-OpenAPI pages (integration guides, quickstarts, intros), we list the link under its group.

Use ripgrep to find anything quickly:
```bash
rg -n "/2/|OAuth2UserToken|BearerToken|tweet.write|dm.write|media" references/x-api-catalog.md
```

## posts

### Endpoints

### POST /2/tweets

- Doc: `https://docs.x.com/x-api/posts/create-post.md`
- Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/tweets/{id}

- Doc: `https://docs.x.com/x-api/posts/delete-post.md`
- Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/tweets/{id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/tweets/counts/all

- Doc: `https://docs.x.com/x-api/posts/get-count-of-all-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/counts/all" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/counts/recent

- Doc: `https://docs.x.com/x-api/posts/get-count-of-recent-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/counts/recent" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/{id}/liking_users

- Doc: `https://docs.x.com/x-api/posts/get-liking-users.md`
- Auth: `OAuth2UserToken [like.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/{id}/liking_users" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/tweets/analytics

- Doc: `https://docs.x.com/x-api/posts/get-post-analytics.md`
- Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/analytics" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/tweets/{id}

- Doc: `https://docs.x.com/x-api/posts/get-post-by-id.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets

- Doc: `https://docs.x.com/x-api/posts/get-posts-by-ids.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/{id}/quote_tweets

- Doc: `https://docs.x.com/x-api/posts/get-quoted-posts.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/{id}/quote_tweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/{id}/retweeted_by

- Doc: `https://docs.x.com/x-api/posts/get-reposted-by.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/{id}/retweeted_by" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/{id}/retweets

- Doc: `https://docs.x.com/x-api/posts/get-reposts.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/{id}/retweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### PUT /2/tweets/{tweet_id}/hidden

- Doc: `https://docs.x.com/x-api/posts/hide-reply.md`
- Auth: `OAuth2UserToken [tweet.moderate.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X PUT "https://api.x.com/2/tweets/{tweet_id}/hidden" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET /2/tweets/search/all

- Doc: `https://docs.x.com/x-api/posts/search-all-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/search/all" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/search/recent

- Doc: `https://docs.x.com/x-api/posts/search-recent-posts.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/tweets/search/recent" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### Docs

- Integration guide: `https://docs.x.com/x-api/posts/bookmarks/integrate.md`
- Bookmarks: `https://docs.x.com/x-api/posts/bookmarks/introduction.md`
- Bookmarks Lookup: `https://docs.x.com/x-api/posts/bookmarks/quickstart/bookmarks-lookup.md`
- Manage Bookmarks: `https://docs.x.com/x-api/posts/bookmarks/quickstart/manage-bookmarks.md`
- Build a query: `https://docs.x.com/x-api/posts/counts/integrate/build-a-query.md`
- Overview: `https://docs.x.com/x-api/posts/counts/integrate/overview.md`
- Post Counts: `https://docs.x.com/x-api/posts/counts/introduction.md`
- Full-Archive Post Counts: `https://docs.x.com/x-api/posts/counts/quickstart/full-archive-tweet-counts.md`
- Recent Post Counts: `https://docs.x.com/x-api/posts/counts/quickstart/recent-tweet-counts.md`
- Build a rule: `https://docs.x.com/x-api/posts/filtered-stream/integrate/build-a-rule.md`
- Matching Posts to Rules: `https://docs.x.com/x-api/posts/filtered-stream/integrate/matching-returned-tweets.md`
- Filtered Stream Operators: `https://docs.x.com/x-api/posts/filtered-stream/integrate/operators.md`
- Filtered Stream: `https://docs.x.com/x-api/posts/filtered-stream/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/filtered-stream/quickstart.md`
- Apps: `https://docs.x.com/x-api/posts/hide-replies/apps.md`
- Manage replies by topic: `https://docs.x.com/x-api/posts/hide-replies/integrate/manage-replies-by-topic.md`
- Manage replies by topic: `https://docs.x.com/x-api/posts/hide-replies/integrate/manage-replies-in-realtime.md`
- Hide Replies: `https://docs.x.com/x-api/posts/hide-replies/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/hide-replies/quickstart.md`
- Likes: `https://docs.x.com/x-api/posts/likes/introduction.md`
- Likes Lookup: `https://docs.x.com/x-api/posts/likes/quickstart/likes-lookup.md`
- Manage Likes: `https://docs.x.com/x-api/posts/likes/quickstart/manage-likes.md`
- Integration Guide: `https://docs.x.com/x-api/posts/lookup/integrate.md`
- Post Lookup: `https://docs.x.com/x-api/posts/lookup/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/lookup/quickstart.md`
- Integration guide: `https://docs.x.com/x-api/posts/manage-tweets/integrate.md`
- Manage Posts: `https://docs.x.com/x-api/posts/manage-tweets/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/manage-tweets/quickstart.md`
- Quote Posts: `https://docs.x.com/x-api/posts/quote-tweets/introduction.md`
- Quickstart: `https://docs.x.com/x-api/posts/quote-tweets/quickstart.md`
- Integration guide: `https://docs.x.com/x-api/posts/retweets/integrate.md`
- Retweets: `https://docs.x.com/x-api/posts/retweets/introduction.md`
- Manage Retweets: `https://docs.x.com/x-api/posts/retweets/quickstart/manage-retweets.md`
- Retweets Lookup: `https://docs.x.com/x-api/posts/retweets/quickstart/retweets-lookup.md`
- Retweets of Me: `https://docs.x.com/x-api/posts/retweets/quickstart/retweets-of-me.md`
- Build a query: `https://docs.x.com/x-api/posts/search/integrate/build-a-query.md`
- Search Operators: `https://docs.x.com/x-api/posts/search/integrate/operators.md`
- Integration Guide: `https://docs.x.com/x-api/posts/search/integrate/overview.md`
- Pagination: `https://docs.x.com/x-api/posts/search/integrate/paginate.md`
- Search Posts: `https://docs.x.com/x-api/posts/search/introduction.md`
- Full-Archive Search Quickstart: `https://docs.x.com/x-api/posts/search/quickstart/full-archive-search.md`
- Recent Search Quickstart: `https://docs.x.com/x-api/posts/search/quickstart/recent-search.md`
- Integration Guide: `https://docs.x.com/x-api/posts/timelines/integrate.md`
- Timelines: `https://docs.x.com/x-api/posts/timelines/introduction.md`
- Home Timeline Quickstart: `https://docs.x.com/x-api/posts/timelines/quickstart/reverse-chron-quickstart.md`
- User Mentions Timeline: `https://docs.x.com/x-api/posts/timelines/quickstart/user-mention-quickstart.md`
- Introduction: `https://docs.x.com/x-api/posts/volume-streams/introduction.md`

## users

### Endpoints

### POST /2/users/{id}/dm/block

- Doc: `https://docs.x.com/x-api/users/block-dms.md`
- Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/dm/block" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/users/{id}/bookmarks

- Doc: `https://docs.x.com/x-api/users/create-bookmark.md`
- Auth: `OAuth2UserToken [bookmark.write, tweet.read, users.read]`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/bookmarks" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/users/{id}/bookmarks/{tweet_id}

- Doc: `https://docs.x.com/x-api/users/delete-bookmark.md`
- Auth: `OAuth2UserToken [bookmark.write, tweet.read, users.read]`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{id}/bookmarks/{tweet_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### POST /2/users/{id}/followed_lists

- Doc: `https://docs.x.com/x-api/users/follow-list.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/followed_lists" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/users/{id}/following

- Doc: `https://docs.x.com/x-api/users/follow-user.md`
- Auth: `OAuth2UserToken [follows.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/following" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET /2/users/{id}/blocking

- Doc: `https://docs.x.com/x-api/users/get-blocking.md`
- Auth: `OAuth2UserToken [block.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/blocking" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/bookmarks/folders

- Doc: `https://docs.x.com/x-api/users/get-bookmark-folders.md`
- Auth: `OAuth2UserToken [bookmark.read, users.read]`

```bash
curl -sS "https://api.x.com/2/users/{id}/bookmarks/folders" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/bookmarks

- Doc: `https://docs.x.com/x-api/users/get-bookmarks.md`
- Auth: `OAuth2UserToken [bookmark.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/users/{id}/bookmarks" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/followed_lists

- Doc: `https://docs.x.com/x-api/users/get-followed-lists.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/followed_lists" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/{id}/followers

- Doc: `https://docs.x.com/x-api/users/get-followers.md`
- Auth: `BearerToken; OAuth2UserToken [follows.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/followers" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/{id}/following

- Doc: `https://docs.x.com/x-api/users/get-following.md`
- Auth: `BearerToken; OAuth2UserToken [follows.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/following" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/{id}/liked_tweets

- Doc: `https://docs.x.com/x-api/users/get-liked-posts.md`
- Auth: `OAuth2UserToken [like.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/liked_tweets" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/list_memberships

- Doc: `https://docs.x.com/x-api/users/get-list-memberships.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/list_memberships" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/{id}/mentions

- Doc: `https://docs.x.com/x-api/users/get-mentions.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/mentions" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/{id}/muting

- Doc: `https://docs.x.com/x-api/users/get-muting.md`
- Auth: `OAuth2UserToken [mute.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/muting" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/me

- Doc: `https://docs.x.com/x-api/users/get-my-user.md`
- Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/me" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/owned_lists

- Doc: `https://docs.x.com/x-api/users/get-owned-lists.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/owned_lists" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/{id}/pinned_lists

- Doc: `https://docs.x.com/x-api/users/get-pinned-lists.md`
- Auth: `OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/pinned_lists" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/tweets

- Doc: `https://docs.x.com/x-api/users/get-posts.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/tweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/reposts_of_me

- Doc: `https://docs.x.com/x-api/users/get-reposts-of-me.md`
- Auth: `OAuth2UserToken [timeline.read, tweet.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/reposts_of_me" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}/timelines/reverse_chronological

- Doc: `https://docs.x.com/x-api/users/get-timeline.md`
- Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}/timelines/reverse_chronological" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/users/{id}

- Doc: `https://docs.x.com/x-api/users/get-user-by-id.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/by/username/{username}

- Doc: `https://docs.x.com/x-api/users/get-user-by-username.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/by/username/{username}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users

- Doc: `https://docs.x.com/x-api/users/get-users-by-ids.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/by

- Doc: `https://docs.x.com/x-api/users/get-users-by-usernames.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/by" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### POST /2/users/{id}/likes

- Doc: `https://docs.x.com/x-api/users/like-post.md`
- Auth: `OAuth2UserToken [like.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/likes" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/users/{id}/muting

- Doc: `https://docs.x.com/x-api/users/mute-user.md`
- Auth: `OAuth2UserToken [mute.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/muting" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/users/{id}/pinned_lists

- Doc: `https://docs.x.com/x-api/users/pin-list.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/pinned_lists" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/users/{id}/retweets

- Doc: `https://docs.x.com/x-api/users/repost-post.md`
- Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/retweets" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET /2/users/search

- Doc: `https://docs.x.com/x-api/users/search-users.md`
- Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/search" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### POST /2/users/{id}/dm/unblock

- Doc: `https://docs.x.com/x-api/users/unblock-dms.md`
- Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/users/{id}/dm/unblock" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/users/{id}/followed_lists/{list_id}

- Doc: `https://docs.x.com/x-api/users/unfollow-list.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{id}/followed_lists/{list_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### DELETE /2/users/{source_user_id}/following/{target_user_id}

- Doc: `https://docs.x.com/x-api/users/unfollow-user.md`
- Auth: `OAuth2UserToken [follows.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{source_user_id}/following/{target_user_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### DELETE /2/users/{id}/likes/{tweet_id}

- Doc: `https://docs.x.com/x-api/users/unlike-post.md`
- Auth: `OAuth2UserToken [like.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{id}/likes/{tweet_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### DELETE /2/users/{source_user_id}/muting/{target_user_id}

- Doc: `https://docs.x.com/x-api/users/unmute-user.md`
- Auth: `OAuth2UserToken [mute.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{source_user_id}/muting/{target_user_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### DELETE /2/users/{id}/pinned_lists/{list_id}

- Doc: `https://docs.x.com/x-api/users/unpin-list.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{id}/pinned_lists/{list_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### DELETE /2/users/{id}/retweets/{source_tweet_id}

- Doc: `https://docs.x.com/x-api/users/unrepost-post.md`
- Auth: `OAuth2UserToken [tweet.read, tweet.write, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/users/{id}/retweets/{source_tweet_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

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

## lists

### Endpoints

### POST /2/lists/{id}/members

- Doc: `https://docs.x.com/x-api/lists/add-list-member.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/lists/{id}/members" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/lists

- Doc: `https://docs.x.com/x-api/lists/create-list.md`
- Auth: `OAuth2UserToken [list.read, list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/lists" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/lists/{id}

- Doc: `https://docs.x.com/x-api/lists/delete-list.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/lists/{id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/lists/{id}

- Doc: `https://docs.x.com/x-api/lists/get-list-by-id.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/lists/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/lists/{id}/followers

- Doc: `https://docs.x.com/x-api/lists/get-list-followers.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/lists/{id}/followers" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/lists/{id}/members

- Doc: `https://docs.x.com/x-api/lists/get-list-members.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/lists/{id}/members" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/lists/{id}/tweets

- Doc: `https://docs.x.com/x-api/lists/get-list-posts.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/lists/{id}/tweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### DELETE /2/lists/{id}/members/{user_id}

- Doc: `https://docs.x.com/x-api/lists/remove-list-member.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/lists/{id}/members/{user_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### PUT /2/lists/{id}

- Doc: `https://docs.x.com/x-api/lists/update-list.md`
- Auth: `OAuth2UserToken [list.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X PUT "https://api.x.com/2/lists/{id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

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

## fundamentals

### Docs

- API Consistency: `https://docs.x.com/x-api/fundamentals/consistency.md`
- Consuming streaming data: `https://docs.x.com/x-api/fundamentals/consuming-streaming-data.md`
- Conversation ID: `https://docs.x.com/x-api/fundamentals/conversation-id.md`
- Data Dictionary: `https://docs.x.com/x-api/fundamentals/data-dictionary.md`
- Edit Posts: `https://docs.x.com/x-api/fundamentals/edit-posts.md`
- Expansions: `https://docs.x.com/x-api/fundamentals/expansions.md`
- Fields: `https://docs.x.com/x-api/fundamentals/fields.md`
- Handling disconnections: `https://docs.x.com/x-api/fundamentals/handling-disconnections.md`
- Handling high-volume capacity: `https://docs.x.com/x-api/fundamentals/high-volume-capacity.md`
- Metrics: `https://docs.x.com/x-api/fundamentals/metrics.md`
- Pagination: `https://docs.x.com/x-api/fundamentals/pagination.md`
- Post Annotations: `https://docs.x.com/x-api/fundamentals/post-annotations.md`
- Usage and Billing: `https://docs.x.com/x-api/fundamentals/post-cap.md`
- X API Rate Limits: `https://docs.x.com/x-api/fundamentals/rate-limits.md`
- Recovery and redundancy: `https://docs.x.com/x-api/fundamentals/recovery-and-redundancy.md`
- Response Codes & Errors: `https://docs.x.com/x-api/fundamentals/response-codes-and-errors.md`
- Versioning: `https://docs.x.com/x-api/fundamentals/versioning.md`

## stream

### Endpoints

### GET /2/tweets/search/stream/rules/counts

- Doc: `https://docs.x.com/x-api/stream/get-stream-rule-counts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/search/stream/rules/counts" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/search/stream/rules

- Doc: `https://docs.x.com/x-api/stream/get-stream-rules.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/search/stream/rules" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/sample10/stream

- Doc: `https://docs.x.com/x-api/stream/stream-10-sampled-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/sample10/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/likes/firehose/stream

- Doc: `https://docs.x.com/x-api/stream/stream-all-likes.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/likes/firehose/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/firehose/stream

- Doc: `https://docs.x.com/x-api/stream/stream-all-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/firehose/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/firehose/stream/lang/en

- Doc: `https://docs.x.com/x-api/stream/stream-english-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/firehose/stream/lang/en" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/search/stream

- Doc: `https://docs.x.com/x-api/stream/stream-filtered-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/search/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/firehose/stream/lang/ja

- Doc: `https://docs.x.com/x-api/stream/stream-japanese-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/firehose/stream/lang/ja" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/firehose/stream/lang/ko

- Doc: `https://docs.x.com/x-api/stream/stream-korean-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/firehose/stream/lang/ko" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/likes/compliance/stream

- Doc: `https://docs.x.com/x-api/stream/stream-likes-compliance-data.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/likes/compliance/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/firehose/stream/lang/pt

- Doc: `https://docs.x.com/x-api/stream/stream-portuguese-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/firehose/stream/lang/pt" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/compliance/stream

- Doc: `https://docs.x.com/x-api/stream/stream-posts-compliance-data.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/compliance/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/likes/sample10/stream

- Doc: `https://docs.x.com/x-api/stream/stream-sampled-likes.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/likes/sample10/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/sample/stream

- Doc: `https://docs.x.com/x-api/stream/stream-sampled-posts.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/sample/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/users/compliance/stream

- Doc: `https://docs.x.com/x-api/stream/stream-users-compliance-data.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/users/compliance/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### POST /2/tweets/search/stream/rules

- Doc: `https://docs.x.com/x-api/stream/update-stream-rules.md`
- Auth: `BearerToken`

```bash
curl -sS -X POST "https://api.x.com/2/tweets/search/stream/rules" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

## direct-messages

### Endpoints

### POST /2/dm_conversations

- Doc: `https://docs.x.com/x-api/direct-messages/create-dm-conversation.md`
- Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/dm_conversations" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/dm_conversations/{dm_conversation_id}/messages

- Doc: `https://docs.x.com/x-api/direct-messages/create-dm-message-by-conversation-id.md`
- Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/dm_conversations/{dm_conversation_id}/messages" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/dm_conversations/with/{participant_id}/messages

- Doc: `https://docs.x.com/x-api/direct-messages/create-dm-message-by-participant-id.md`
- Auth: `OAuth2UserToken [dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/dm_conversations/with/{participant_id}/messages" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/dm_events/{event_id}

- Doc: `https://docs.x.com/x-api/direct-messages/delete-dm-event.md`
- Auth: `OAuth2UserToken [dm.read, dm.write]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/dm_events/{event_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/dm_events/{event_id}

- Doc: `https://docs.x.com/x-api/direct-messages/get-dm-event-by-id.md`
- Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/dm_events/{event_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/dm_conversations/{id}/dm_events

- Doc: `https://docs.x.com/x-api/direct-messages/get-dm-events-for-a-dm-conversation-1.md`
- Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/dm_conversations/{id}/dm_events" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/dm_conversations/with/{participant_id}/dm_events

- Doc: `https://docs.x.com/x-api/direct-messages/get-dm-events-for-a-dm-conversation.md`
- Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/dm_conversations/with/{participant_id}/dm_events" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/dm_events

- Doc: `https://docs.x.com/x-api/direct-messages/get-dm-events.md`
- Auth: `OAuth2UserToken [dm.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/dm_events" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### Docs

- Introduction: `https://docs.x.com/x-api/direct-messages/blocks/introduction.md`
- Integration Guide: `https://docs.x.com/x-api/direct-messages/lookup/integrate.md`
- Direct Messages Lookup: `https://docs.x.com/x-api/direct-messages/lookup/introduction.md`
- Quickstart: `https://docs.x.com/x-api/direct-messages/lookup/quickstart.md`
- Integration Guide: `https://docs.x.com/x-api/direct-messages/manage/integrate.md`
- Manage Direct Messages: `https://docs.x.com/x-api/direct-messages/manage/introduction.md`
- Quickstart: `https://docs.x.com/x-api/direct-messages/manage/quickstart.md`

## enterprise-gnip-2.0

### Docs

- Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/enterprise-gnip.md`
- Account Activity API: Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/account-activity.md`
- Data dictionary: Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/data-dictionary.md`
- Data enrichments: Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/data-enrichments.md`
- Decahose API: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/decahose-api.md`
- Edit Tweets: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/edit-tweets.md`
- Engagement API: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/engagement-api.md`
- Compliance Firehose API: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/firehouse.md`
- Gnip console: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/overview.md`
- Rate limits: Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/rate-limits.md`
- Rules and filtering: Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/rules-filtering.md`
- Search API: Enterprise: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/search-api.md`
- Usage API: `https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/usage.md`
- PowerTrack API: `https://docs.x.com/x-api/enterprise-gnip-2.0/powertrack-api.md`

## media

### Endpoints

### POST /2/media/upload/{id}/append

- Doc: `https://docs.x.com/x-api/media/append-media-upload.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/media/upload/{id}/append" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/media/metadata

- Doc: `https://docs.x.com/x-api/media/create-media-metadata.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/media/metadata" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/media/subtitles

- Doc: `https://docs.x.com/x-api/media/create-media-subtitles.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/media/subtitles" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/media/subtitles

- Doc: `https://docs.x.com/x-api/media/delete-media-subtitles.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/media/subtitles" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### POST /2/media/upload/{id}/finalize

- Doc: `https://docs.x.com/x-api/media/finalize-media-upload.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/media/upload/{id}/finalize" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET /2/media/analytics

- Doc: `https://docs.x.com/x-api/media/get-media-analytics.md`
- Auth: `OAuth2UserToken [tweet.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/media/analytics" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/media/upload

- Doc: `https://docs.x.com/x-api/media/get-media-upload-status.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS "https://api.x.com/2/media/upload" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### POST /2/media/upload/initialize

- Doc: `https://docs.x.com/x-api/media/initialize-media-upload.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/media/upload/initialize" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/media/upload

- Doc: `https://docs.x.com/x-api/media/upload-media.md`
- Auth: `OAuth2UserToken [media.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/media/upload" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Docs

- Introduction: `https://docs.x.com/x-api/media/introduction.md`
- Best practices: `https://docs.x.com/x-api/media/quickstart/best-practices.md`
- Chunked Media Upload: `https://docs.x.com/x-api/media/quickstart/media-upload-chunked.md`

## spaces

### Endpoints

### GET /2/spaces/{id}

- Doc: `https://docs.x.com/x-api/spaces/get-space-by-id.md`
- Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/spaces/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/spaces/{id}/tweets

- Doc: `https://docs.x.com/x-api/spaces/get-space-posts.md`
- Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/spaces/{id}/tweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/spaces/{id}/buyers

- Doc: `https://docs.x.com/x-api/spaces/get-space-ticket-buyers.md`
- Auth: `OAuth2UserToken [space.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/spaces/{id}/buyers" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/spaces/by/creator_ids

- Doc: `https://docs.x.com/x-api/spaces/get-spaces-by-creator-ids.md`
- Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/spaces/by/creator_ids" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/spaces

- Doc: `https://docs.x.com/x-api/spaces/get-spaces-by-ids.md`
- Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/spaces" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/spaces/search

- Doc: `https://docs.x.com/x-api/spaces/search-spaces.md`
- Auth: `BearerToken; OAuth2UserToken [space.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/spaces/search" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### Docs

- Introduction: `https://docs.x.com/x-api/spaces/introduction.md`
- Spaces Lookup: `https://docs.x.com/x-api/spaces/lookup/introduction.md`
- Quickstart: `https://docs.x.com/x-api/spaces/lookup/quickstart.md`
- Spaces Search: `https://docs.x.com/x-api/spaces/search/introduction.md`
- Quickstart: `https://docs.x.com/x-api/spaces/search/quickstart.md`

## webhooks

### Endpoints

### POST /2/webhooks/replay

- Doc: `https://docs.x.com/x-api/webhooks/create-replay-job-for-webhook.md`
- Auth: `BearerToken`

```bash
curl -sS -X POST "https://api.x.com/2/webhooks/replay" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/tweets/search/webhooks/{webhook_id}

- Doc: `https://docs.x.com/x-api/webhooks/create-stream-link.md`
- Auth: `BearerToken`

```bash
curl -sS -X POST "https://api.x.com/2/tweets/search/webhooks/{webhook_id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/webhooks

- Doc: `https://docs.x.com/x-api/webhooks/create-webhook.md`
- Auth: `BearerToken; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/webhooks" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/tweets/search/webhooks/{webhook_id}

- Doc: `https://docs.x.com/x-api/webhooks/delete-stream-link.md`
- Auth: `BearerToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/tweets/search/webhooks/{webhook_id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### DELETE /2/webhooks/{webhook_id}

- Doc: `https://docs.x.com/x-api/webhooks/delete-webhook.md`
- Auth: `BearerToken; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/webhooks/{webhook_id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/tweets/search/webhooks

- Doc: `https://docs.x.com/x-api/webhooks/get-stream-links.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/tweets/search/webhooks" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/webhooks

- Doc: `https://docs.x.com/x-api/webhooks/get-webhook.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/webhooks" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### PUT /2/webhooks/{webhook_id}

- Doc: `https://docs.x.com/x-api/webhooks/validate-webhook.md`
- Auth: `BearerToken; UserToken`

```bash
curl -sS -X PUT "https://api.x.com/2/webhooks/{webhook_id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Docs

- Webhooks: `https://docs.x.com/x-api/webhooks/introduction.md`
- Filtered Stream Webhooks API: `https://docs.x.com/x-api/webhooks/stream/introduction.md`
- Quickstart: `https://docs.x.com/x-api/webhooks/stream/quickstart.md`

## account-activity

### Endpoints

### POST /2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all

- Doc: `https://docs.x.com/x-api/account-activity/create-replay-job.md`
- Auth: `BearerToken`

```bash
curl -sS -X POST "https://api.x.com/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST /2/account_activity/webhooks/{webhook_id}/subscriptions/all

- Doc: `https://docs.x.com/x-api/account-activity/create-subscription.md`
- Auth: `OAuth2UserToken [dm.read, dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/account_activity/webhooks/{webhook_id}/subscriptions/all" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all

- Doc: `https://docs.x.com/x-api/account-activity/delete-subscription.md`
- Auth: `BearerToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/account_activity/subscriptions/count

- Doc: `https://docs.x.com/x-api/account-activity/get-subscription-count.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/account_activity/subscriptions/count" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/account_activity/webhooks/{webhook_id}/subscriptions/all/list

- Doc: `https://docs.x.com/x-api/account-activity/get-subscriptions.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/account_activity/webhooks/{webhook_id}/subscriptions/all

- Doc: `https://docs.x.com/x-api/account-activity/validate-subscription.md`
- Auth: `OAuth2UserToken [dm.read, dm.write, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/account_activity/webhooks/{webhook_id}/subscriptions/all" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### Docs

- Account Activity API: `https://docs.x.com/x-api/account-activity/introduction.md`
- v2 Account Activity API Migration Guide: `https://docs.x.com/x-api/account-activity/migrate/overview.md`

## activity

### Endpoints

### GET /2/activity/stream

- Doc: `https://docs.x.com/x-api/activity/activity-stream.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/activity/stream" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### POST /2/activity/subscriptions

- Doc: `https://docs.x.com/x-api/activity/create-x-activity-subscription.md`
- Auth: `BearerToken; OAuth2UserToken [dm.read, tweet.read]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/activity/subscriptions" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/activity/subscriptions/{subscription_id}

- Doc: `https://docs.x.com/x-api/activity/deletes-x-activity-subscription.md`
- Auth: `BearerToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/activity/subscriptions/{subscription_id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/activity/subscriptions

- Doc: `https://docs.x.com/x-api/activity/get-x-activity-subscriptions.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/activity/subscriptions" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### PUT /2/activity/subscriptions/{subscription_id}

- Doc: `https://docs.x.com/x-api/activity/update-x-activity-subscription.md`
- Auth: `BearerToken`

```bash
curl -sS -X PUT "https://api.x.com/2/activity/subscriptions/{subscription_id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Docs

- Introduction: `https://docs.x.com/x-api/activity/introduction.md`
- Quickstart: `https://docs.x.com/x-api/activity/quickstart.md`

## community-notes

### Endpoints

### POST /2/notes

- Doc: `https://docs.x.com/x-api/community-notes/create-a-community-note.md`
- Auth: `OAuth2UserToken [tweet.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/notes" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### DELETE /2/notes/{id}

- Doc: `https://docs.x.com/x-api/community-notes/delete-a-community-note.md`
- Auth: `OAuth2UserToken [tweet.write]; UserToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/notes/{id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### POST /2/evaluate_note

- Doc: `https://docs.x.com/x-api/community-notes/evaluate-a-community-note.md`
- Auth: `OAuth2UserToken [tweet.write]; UserToken`

```bash
curl -sS -X POST "https://api.x.com/2/evaluate_note" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET /2/notes/search/notes_written

- Doc: `https://docs.x.com/x-api/community-notes/search-for-community-notes-written.md`
- Auth: `OAuth2UserToken [tweet.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/notes/search/notes_written" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/notes/search/posts_eligible_for_notes

- Doc: `https://docs.x.com/x-api/community-notes/search-for-posts-eligible-for-community-notes.md`
- Auth: `OAuth2UserToken [tweet.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/notes/search/posts_eligible_for_notes" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### Docs

- Introduction: `https://docs.x.com/x-api/community-notes/introduction.md`
- Quickstart: `https://docs.x.com/x-api/community-notes/quickstart.md`

## compliance

### Endpoints

### POST /2/compliance/jobs

- Doc: `https://docs.x.com/x-api/compliance/create-compliance-job.md`
- Auth: `BearerToken`

```bash
curl -sS -X POST "https://api.x.com/2/compliance/jobs" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET /2/compliance/jobs/{id}

- Doc: `https://docs.x.com/x-api/compliance/get-compliance-job-by-id.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/compliance/jobs/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/compliance/jobs

- Doc: `https://docs.x.com/x-api/compliance/get-compliance-jobs.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/compliance/jobs" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### Docs

- Integration guide: `https://docs.x.com/x-api/compliance/batch-compliance/integrate.md`
- Batch Compliance: `https://docs.x.com/x-api/compliance/batch-compliance/introduction.md`
- Quickstart: `https://docs.x.com/x-api/compliance/batch-compliance/quickstart.md`
- Introduction: `https://docs.x.com/x-api/compliance/streams/introduction.md`

## getting-started

### Docs

- About the X API: `https://docs.x.com/x-api/getting-started/about-x-api.md`
- Getting Access: `https://docs.x.com/x-api/getting-started/getting-access.md`
- Important Resources: `https://docs.x.com/x-api/getting-started/important-resources.md`
- Make Your First Request: `https://docs.x.com/x-api/getting-started/make-your-first-request.md`
- Pricing: `https://docs.x.com/x-api/getting-started/pricing.md`
- X API: `https://docs.x.com/x-api/introduction.md`
- What to Build: `https://docs.x.com/x-api/what-to-build.md`

## communities

### Endpoints

### GET /2/communities/{id}

- Doc: `https://docs.x.com/x-api/communities/get-community-by-id.md`
- Auth: `BearerToken; OAuth2UserToken [list.read, tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/communities/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/communities/search

- Doc: `https://docs.x.com/x-api/communities/search-communities.md`
- Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/communities/search" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### Docs

- Communities Lookup: `https://docs.x.com/x-api/communities/lookup/introduction.md`
- Communities Search: `https://docs.x.com/x-api/communities/search/introduction.md`

## powerstream

### Docs

- Handling disconnections: `https://docs.x.com/x-api/powerstream/handling-disconnections.md`
- Introduction: `https://docs.x.com/x-api/powerstream/introduction.md`
- Powerstream Operators: `https://docs.x.com/x-api/powerstream/operators.md`
- Recovery and redundancy: `https://docs.x.com/x-api/powerstream/recovery-and-redundancy.md`

## trends

### Endpoints

### GET /2/users/personalized_trends

- Doc: `https://docs.x.com/x-api/trends/get-personalized-trends.md`
- Auth: `OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/users/personalized_trends" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

### GET /2/trends/by/woeid/{woeid}

- Doc: `https://docs.x.com/x-api/trends/get-trends-by-woeid.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/trends/by/woeid/{woeid}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### Docs

- Personalized Trends: `https://docs.x.com/x-api/trends/personalized-trends/introduction.md`
- Trends by WOEID: `https://docs.x.com/x-api/trends/trends-by-woeid/introduction.md`

## migrate

### Docs

- Data Formation Migration: `https://docs.x.com/x-api/migrate/data-format-migration.md`
- Overview: `https://docs.x.com/x-api/migrate/overview.md`
- X API endpoint map: `https://docs.x.com/x-api/migrate/x-api-endpoint-map.md`

## news

### Endpoints

### GET /2/news/{id}

- Doc: `https://docs.x.com/x-api/news/get-news-stories-by-id.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken`

```bash
curl -sS "https://api.x.com/2/news/{id}" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### GET /2/news/search

- Doc: `https://docs.x.com/x-api/news/search-news.md`
- Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/news/search" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### Docs

- Introduction: `https://docs.x.com/x-api/news/introduction.md`

## tools-and-libraries

### Docs

- Tools & Libraries: `https://docs.x.com/x-api/tools-and-libraries/overview.md`
- Official SDKs: `https://docs.x.com/x-api/tools-and-libraries/sdks.md`

## usage

### Endpoints

### GET /2/usage/tweets

- Doc: `https://docs.x.com/x-api/usage/get-usage.md`
- Auth: `BearerToken`

```bash
curl -sS "https://api.x.com/2/usage/tweets" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

### Docs

- Usage: `https://docs.x.com/x-api/usage/introduction.md`

## bookmarks

### Endpoints

### GET /2/users/{id}/bookmarks/folders/{folder_id}

- Doc: `https://docs.x.com/x-api/bookmarks/get-bookmarks-by-folder-id.md`
- Auth: `OAuth2UserToken [bookmark.read, tweet.read, users.read]`

```bash
curl -sS "https://api.x.com/2/users/{id}/bookmarks/folders/{folder_id}" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN"
```

## connections

### Endpoints

### DELETE /2/connections/all

- Doc: `https://docs.x.com/x-api/connections/terminate-all-connections.md`
- Auth: `BearerToken`

```bash
curl -sS -X DELETE "https://api.x.com/2/connections/all" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

