# Fundamentals: Counting Characters

Authoritative docs:
- `https://docs.x.com/fundamentals/counting-characters.md`

## Why This Matters

- Post length validation is not just raw Unicode codepoint count.
- URLs and certain characters can be counted differently.

When drafting create/edit Post requests, treat server validation errors as authoritative.
If you need exact client-side validation, implement it per the Counting Characters doc.
