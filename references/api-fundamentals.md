# Api Fundamentals

This page is for “how does the X API behave?” questions. Most non-technical users won’t ask for this directly, but it’s what an autonomous agent should consult when something is confusing (pagination, fields, disconnections, errors).

## Common prompts this helps with

- “Why is my response missing fields?”
  - Use `*.fields` and `expansions` to request exactly what you need. See `references/request-shapes.md`.
- “Why did I get rate limited?”
  - Read `x-rate-limit-*` headers and back off. See `references/fundamentals-rate-limits.md`.
- “Why did the request fail?”
  - Use status code + response body; don’t blindly retry `401/403/404`. See `references/fundamentals-errors.md`.
- “My stream disconnected”
  - Streams are long-lived; reconnect with backoff. See `references/streams.md`.

If you’re just trying to post/search/bookmarks/DMs, start with `references/workflows.md`.

## Inventory

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
