# x-api-skill

Codex skill for turning plain-English requests into correct X API (Twitter API v2) request(s): endpoint selection, auth mode (bearer vs user-context), scopes, params (`fields`, `expansions`), pagination, and write-action safety.

## Install (via skills CLI)

List skills in a repo (sanity check):

```bash
npx skills add <owner>/<repo> --list
```

Install this skill from GitHub:

```bash
npx skills add <owner>/x-api-skill
```

If you have a multi-skill repo, select a specific skill:

```bash
npx skills add <owner>/<repo> --skill x-api-skill
```

## Repo requirements for `npx skills add`

- `SKILL.md` exists (root for a single-skill repo, or in each skill directory for a multi-skill repo).
- `SKILL.md` has YAML frontmatter with `name` and `description`.
- Any referenced files (like `references/...` or `scripts/...`) are repo-relative paths that exist.

