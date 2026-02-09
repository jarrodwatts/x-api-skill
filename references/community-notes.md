# Community Notes

Docs entry points:
- `https://docs.x.com/x-api/community-notes/introduction.md`
- `https://docs.x.com/x-api/community-notes/quickstart.md`
- `https://docs.x.com/x-api/community-notes/create-a-community-note.md`
- `https://docs.x.com/x-api/community-notes/delete-a-community-note.md`
- `https://docs.x.com/x-api/community-notes/evaluate-a-community-note.md`
- `https://docs.x.com/x-api/community-notes/search-for-community-notes-written.md`
- `https://docs.x.com/x-api/community-notes/search-for-posts-eligible-for-community-notes.md`

## Key Endpoints

- `POST /2/notes` (create note)

Other endpoints vary by operation; use the docs above as the source of truth.

## Create A Note

Requires user context.

Minimal shape (see schema in docs for full `info` object):
- `info.text` must include at least one URL (per the OpenAPI pattern).
- `info` requires `text`, `classification`, `misleading_tags`, `trustworthy_sources`.

```bash
curl -sS -X POST "https://api.x.com/2/notes" \
  -H "Authorization: Bearer $X_USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "test_mode": true,
    "post_id": "...",
    "info": {
      "text": "Summary with at least one source link: https://example.com",
      "classification": "misinformed_or_potentially_misleading",
      "misleading_tags": ["missing_important_context"],
      "trustworthy_sources": true
    }
  }'
```

Notes:
- `test_mode=true` is for testing and should not publish.
- Treat this as a write action with user-visible side effects when `test_mode=false`.

## Inventory

### Endpoints

- **POST /2/notes** — Auth: `OAuth2UserToken [tweet.write]; UserToken` — Doc: `https://docs.x.com/x-api/community-notes/create-a-community-note.md`
- **DELETE /2/notes/{id}** — Auth: `OAuth2UserToken [tweet.write]; UserToken` — Doc: `https://docs.x.com/x-api/community-notes/delete-a-community-note.md`
- **POST /2/evaluate_note** — Auth: `OAuth2UserToken [tweet.write]; UserToken` — Doc: `https://docs.x.com/x-api/community-notes/evaluate-a-community-note.md`
- **GET /2/notes/search/notes_written** — Auth: `OAuth2UserToken [tweet.read]; UserToken` — Doc: `https://docs.x.com/x-api/community-notes/search-for-community-notes-written.md`
- **GET /2/notes/search/posts_eligible_for_notes** — Auth: `OAuth2UserToken [tweet.read]; UserToken` — Doc: `https://docs.x.com/x-api/community-notes/search-for-posts-eligible-for-community-notes.md`

### Docs

- Introduction: `https://docs.x.com/x-api/community-notes/introduction.md`
- Quickstart: `https://docs.x.com/x-api/community-notes/quickstart.md`
