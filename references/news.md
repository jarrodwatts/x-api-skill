# News

This page is for the X News API surface (story lookup/search). Most “what are people saying about X?” prompts should use `references/search.md` instead.

## Common prompts this helps with

- “Search X News for `<topic>`”
  - Use `GET /2/news/search` (Bearer token often works).
- “Get the full details for this news story id”
  - Use `GET /2/news/{id}`.

## Inventory

### Endpoints

- **GET /2/news/{id}** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]; UserToken` — Doc: `https://docs.x.com/x-api/news/get-news-stories-by-id.md`
- **GET /2/news/search** — Auth: `BearerToken; OAuth2UserToken [tweet.read, users.read]` — Doc: `https://docs.x.com/x-api/news/search-news.md`

### Docs

- Introduction: `https://docs.x.com/x-api/news/introduction.md`
