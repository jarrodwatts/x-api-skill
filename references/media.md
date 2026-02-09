# Media

Media upload is a multi-step flow. For a great end-user experience in an autonomous agent, treat “tweet this image/video” as a two-phase plan:

1. **Upload media** (get a media id)
2. **Create the post** referencing that media id

## Common prompts this helps with

- “Tweet this image with caption `...`”
- “Tweet this video”

## Practical notes for autonomous agents

- Media endpoints require OAuth 2.0 user context and typically `media.write`.
- Upload flows are easy to get wrong; prefer following the official docs step-by-step.
- If the user provides a local file, the agent will need a host/runtime that can read the file and upload bytes (not just draft curl).

## Inventory

### Endpoints

- **POST /2/media/upload/{id}/append** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/append-media-upload.md`
- **POST /2/media/metadata** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/create-media-metadata.md`
- **POST /2/media/subtitles** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/create-media-subtitles.md`
- **DELETE /2/media/subtitles** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/delete-media-subtitles.md`
- **POST /2/media/upload/{id}/finalize** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/finalize-media-upload.md`
- **GET /2/media/analytics** — Auth: `OAuth2UserToken [tweet.read]; UserToken` — Doc: `https://docs.x.com/x-api/media/get-media-analytics.md`
- **GET /2/media/upload** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/get-media-upload-status.md`
- **POST /2/media/upload/initialize** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/initialize-media-upload.md`
- **POST /2/media/upload** — Auth: `OAuth2UserToken [media.write]; UserToken` — Doc: `https://docs.x.com/x-api/media/upload-media.md`

### Docs

- Introduction: `https://docs.x.com/x-api/media/introduction.md`
- Best practices: `https://docs.x.com/x-api/media/quickstart/best-practices.md`
- Chunked Media Upload: `https://docs.x.com/x-api/media/quickstart/media-upload-chunked.md`
