#!/usr/bin/env python3
"""Extract a curl skeleton from an X docs OpenAPI markdown page.

Usage:
  python3 x_openapi_curl.py <docs-url-or-path>

This is intentionally dependency-free (no PyYAML).
It uses simple heuristics based on the docs' fenced OpenAPI YAML blocks.
"""

from __future__ import annotations

import os
import re
import sys
import urllib.request
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class OpenApiExtract:
    method: str
    path: str
    server_url: Optional[str]
    security_block_lines: List[str]


def _read_text(url_or_path: str) -> str:
    if re.match(r"^https?://", url_or_path):
        req = urllib.request.Request(
            url_or_path,
            headers={
                "User-Agent": "x-api-skill-openapi-extractor/1.0",
                "Accept": "text/markdown,text/plain,*/*",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")

    with open(url_or_path, "r", encoding="utf-8") as f:
        return f.read()


def _extract_openapi_yaml_block(md: str) -> Tuple[str, str, str]:
    """Return (fence_header_line, yaml_text, fence)

    Docs use a 4-backtick fence like:
      ````yaml get /2/tweets/{id}
      ...
      ````
    """

    # Find the first 4-backtick yaml fence.
    m = re.search(r"(?m)^(`{4})yaml\s+([^\n]+)\n", md)
    if not m:
        raise ValueError("Could not find an OpenAPI YAML fence (expected a line starting with ````yaml ...)")

    fence = m.group(1)
    header = m.group(0).rstrip("\n")
    start = m.end()

    end_pat = rf"(?m)^{re.escape(fence)}\s*$"
    m_end = re.search(end_pat, md[start:])
    if not m_end:
        raise ValueError("Could not find closing OpenAPI YAML fence")

    yaml_text = md[start : start + m_end.start()]
    return header, yaml_text, fence


def _parse_method_path_from_header(header_line: str) -> Tuple[str, str]:
    # header is like: ````yaml get /2/tweets/{id}
    m = re.match(r"^`{4}yaml\s+(\w+)\s+([^\s]+)\s*$", header_line)
    if not m:
        raise ValueError(f"Unexpected OpenAPI fence header: {header_line!r}")
    return m.group(1).upper(), m.group(2)


def _find_server_url(yaml_lines: List[str]) -> Optional[str]:
    # Heuristic: look for the first "servers:" block then the first "url:" under it.
    for i, line in enumerate(yaml_lines):
        if re.match(r"^\s*servers:\s*$", line):
            for j in range(i + 1, min(i + 80, len(yaml_lines))):
                m = re.match(r"^\s*url:\s*(https?://\S+)\s*$", yaml_lines[j])
                if m:
                    return m.group(1)
    return None


def _leading_spaces(s: str) -> int:
    return len(s) - len(s.lstrip(" "))


def _extract_security_block(yaml_lines: List[str]) -> List[str]:
    """Return the first operation-level security block (as raw YAML lines).

    We skip top-level `security: []` and take the first `security:` that is followed by list entries.
    """
    for i, line in enumerate(yaml_lines):
        if re.match(r"^\s*security:\s*\[\s*\]\s*$", line):
            continue
        if not re.match(r"^\s*security:\s*$", line):
            continue

        indent = _leading_spaces(line)
        collected: List[str] = []

        for j in range(i + 1, len(yaml_lines)):
            nxt = yaml_lines[j]
            if nxt.strip() == "":
                continue
            if _leading_spaces(nxt) <= indent:
                break
            collected.append(nxt.rstrip("\n"))

        # Only accept a block that looks list-y.
        if any(re.match(r"^\s*-\s+", x) for x in collected):
            return collected

    return []


def _pick_auth_env(security_block_lines: List[str]) -> str:
    joined = "\n".join(security_block_lines)
    if "BearerToken" in joined:
        return "$X_BEARER_TOKEN"
    if "OAuth2UserToken" in joined or "UserToken" in joined:
        return "$X_USER_ACCESS_TOKEN"
    return "$X_BEARER_TOKEN"


def _render_curl(ex: OpenApiExtract) -> str:
    base = ex.server_url or "https://api.x.com"
    url = f"{base}{ex.path}"

    auth_token = _pick_auth_env(ex.security_block_lines)
    method_flag = "" if ex.method == "GET" else f"-X {ex.method} "

    parts: List[str] = [f"curl -sS {method_flag}\"{url}\""]
    parts.append(f"  -H \"Authorization: Bearer {auth_token}\"")

    if ex.method in {"POST", "PUT", "PATCH"}:
        parts.append("  -H \"Content-Type: application/json\"")
        parts.append("  -d '{}'")

    # Join as a single shell command with line continuations.
    return " \\\n".join(parts)


def extract(url_or_path: str) -> OpenApiExtract:
    md = _read_text(url_or_path)
    header, yaml_text, _fence = _extract_openapi_yaml_block(md)

    method, path = _parse_method_path_from_header(header)
    yaml_lines = yaml_text.splitlines()

    server_url = _find_server_url(yaml_lines)
    security_lines = _extract_security_block(yaml_lines)

    return OpenApiExtract(method=method, path=path, server_url=server_url, security_block_lines=security_lines)


def main(argv: List[str]) -> int:
    if len(argv) != 2 or argv[1] in {"-h", "--help"}:
        print(__doc__.strip())
        return 2

    src = argv[1]

    try:
        ex = extract(src)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    base = ex.server_url or "https://api.x.com"
    print(f"endpoint: {ex.method} {base}{ex.path}")

    if ex.security_block_lines:
        print("auth:")
        for line in ex.security_block_lines:
            print(f"  {line}")
    else:
        print("auth: (not found; check docs page)")

    print("curl:")
    print(_render_curl(ex))

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
