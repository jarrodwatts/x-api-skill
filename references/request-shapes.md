# Request Shapes: Fields, Expansions, Pagination

Source examples:
- `https://docs.x.com/x-api/getting-started/about-x-api.md`
- `https://docs.x.com/x-api/getting-started/make-your-first-request.md`

## Base URL

Most X API v2 endpoints are under:
- `https://api.x.com/2/...`

## Fields

By default, many endpoints return a small default set of fields. Use `*.fields` params to request more.

Common patterns:
- `tweet.fields=created_at,public_metrics,lang,conversation_id`
- `user.fields=created_at,description,public_metrics,verified,location,url`

Example:
```bash
curl -sS "https://api.x.com/2/tweets/123?tweet.fields=created_at,public_metrics" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Expansions

Use `expansions=` to include related objects in the response `includes` block.

Example: include author details while fetching a tweet:
```bash
curl -sS "https://api.x.com/2/tweets/123?tweet.fields=created_at&expansions=author_id&user.fields=username" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

Pragmatic rule:
- Start with no expansions.
- Add expansions only to eliminate follow-up calls.

## Pagination

Many endpoints return:
- `meta.next_token` (and sometimes `meta.previous_token`)

You pass:
- `pagination_token=<token>` or `next_token=<token>` depending on endpoint.

Workflow:
1. Request first page.
2. If response contains `meta.next_token`, request the next page with that token.
3. Stop when you have enough (cap pages).

## Common Query Parameters

- `max_results=<n>`: request more items per page.
- `pagination_token=<token>`: next page.
- `start_time`, `end_time`: time-bounded queries when supported.

## Output Requirements (For Agent Responses)

When the user asks for "fetch everything":
- specify a page cap or an explicit stop condition
- estimate call volume
- mention rate limits
