# Fundamentals: X IDs

Authoritative docs:
- `https://docs.x.com/fundamentals/x-ids.md`

## What Matters For API Calls

- IDs are strings in JSON responses even if they look numeric.
- Do not assume they fit in 32-bit (or even 53-bit JS number) integer types.
- Preserve IDs as strings end-to-end.

## Common Places IDs Show Up

- `data.id` for a resource
- `includes.users[].id` and similar when using expansions
- path params like `/2/tweets/{id}` or `/2/users/{id}`

## Extract IDs From X Links (Common User Input)

Non-technical users often paste links instead of IDs. Common patterns:

- Post URL:
  - `https://x.com/<handle>/status/<post_id>`
  - Extract `<post_id>` (digits after `/status/`).
- Communities/other URLs may include IDs in the path as well; if in doubt, ask the user for the exact link and extract the obvious numeric segment.

Always keep extracted IDs as strings.

## Agent Output Requirements

If the user is using JavaScript/TypeScript, explicitly warn not to parse IDs as `number`.
