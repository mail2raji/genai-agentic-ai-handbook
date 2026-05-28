"""build-export.py

Walk the mkdocs.yml nav, concatenate every leaf markdown file into one big
markdown document, fix relative links, and write it to `_export/book.md`.

The output is then fed to pandoc by the GitHub Actions workflow to produce
`book.docx` and `book.pdf`.

Idempotent. Safe to run locally:
    python tools/build-export.py
"""
from __future__ import annotations

import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"
DOCS_DIR = REPO_ROOT / "docs"
OUT_DIR = REPO_ROOT / "_export"
OUT_MD = OUT_DIR / "book.md"


# MkDocs uses !!python/name: tags that PyYAML won't load by default.
# Strip them out — we only need the `nav` block, not the plugin internals.
class _SafeLoader(yaml.SafeLoader):
    pass


def _ignore_python_name(loader, tag_suffix, node):  # noqa: ARG001
    return None


_SafeLoader.add_multi_constructor("tag:yaml.org,2002:python/name:", _ignore_python_name)
_SafeLoader.add_multi_constructor("!!python/name:", _ignore_python_name)


def load_nav() -> list:
    text = MKDOCS_YML.read_text(encoding="utf-8")
    data = yaml.load(text, Loader=_SafeLoader)
    return data.get("nav", []) or []


def walk_nav(nav, parents=None):
    """Yield (heading_path, md_path) tuples in nav order."""
    parents = parents or []
    if isinstance(nav, list):
        for item in nav:
            yield from walk_nav(item, parents)
        return
    if isinstance(nav, dict):
        for title, value in nav.items():
            new_parents = parents + [str(title)]
            if isinstance(value, str):
                yield (new_parents, value)
            else:
                yield from walk_nav(value, new_parents)


_FENCE_RE = re.compile(r"^(`{3,}|~{3,})", re.MULTILINE)
_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def fix_relative_links(text: str, md_path: Path) -> str:
    """Convert relative .md links to anchor refs inside the combined book.

    Strategy: every md file becomes one section with an explicit anchor like
    `<a id="anchor-slug"></a>`. Relative links within the book get rewritten
    to those anchors. External URLs are left alone.
    """

    def _repl(match: re.Match) -> str:
        label = match.group(1)
        target = match.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        # Resolve target relative to current file
        try:
            abs_target = (md_path.parent / target).resolve()
        except OSError:
            return match.group(0)
        try:
            rel_to_docs = abs_target.relative_to(DOCS_DIR)
        except ValueError:
            return match.group(0)
        anchor = slug_for(rel_to_docs)
        return f"[{label}](#{anchor})"

    # Don't touch links inside fenced code blocks
    parts = []
    pos = 0
    in_fence = False
    fence_marker = None
    for m in _FENCE_RE.finditer(text):
        chunk = text[pos:m.start()]
        if not in_fence:
            chunk = _LINK_RE.sub(_repl, chunk)
        parts.append(chunk)
        parts.append(m.group(0))
        if not in_fence:
            in_fence = True
            fence_marker = m.group(1)[0]  # ` or ~
        else:
            in_fence = False
            fence_marker = None
        pos = m.end()
    tail = text[pos:]
    if not in_fence:
        tail = _LINK_RE.sub(_repl, tail)
    parts.append(tail)
    return "".join(parts)


def slug_for(rel: Path) -> str:
    s = str(rel.with_suffix("")).replace("\\", "/").replace("/", "-").replace(" ", "-")
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", s).strip("-").lower()


def main() -> int:
    if not MKDOCS_YML.exists():
        print(f"mkdocs.yml not found at {MKDOCS_YML}", file=sys.stderr)
        return 1

    nav = load_nav()
    if not nav:
        print("Nav is empty.", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(exist_ok=True)
    out = []
    # Front matter for pandoc
    out.append("---")
    out.append("title: \"GenAI & Agentic AI Handbook\"")
    out.append("subtitle: \"Beginner-to-Advanced — concept curriculum + 18 hands-on phases\"")
    out.append("author: \"mail2raji\"")
    out.append("lang: en")
    out.append("toc: true")
    out.append("toc-depth: 3")
    out.append("---")
    out.append("")

    count = 0
    missing = []

    for heading_path, md_rel in walk_nav(nav):
        md_file = DOCS_DIR / md_rel
        if not md_file.exists():
            missing.append(md_rel)
            continue
        count += 1
        depth = max(1, min(6, len(heading_path)))
        anchor = slug_for(Path(md_rel))
        out.append(f"<a id=\"{anchor}\"></a>")
        out.append("")
        out.append(f"{'#' * depth} {heading_path[-1]}")
        out.append("")
        raw = md_file.read_text(encoding="utf-8")
        # Strip an existing top-level H1 to avoid duplicate titles
        raw = re.sub(r"\A\s*#\s[^\n]*\n+", "", raw)
        # Demote remaining # headings by depth-1 levels so they nest correctly
        if depth > 1:
            def _demote(match: re.Match, d=depth) -> str:
                hashes = match.group(1)
                rest = match.group(2)
                new_level = min(6, len(hashes) + (d - 1))
                return f"{'#' * new_level} {rest}"
            raw = re.sub(r"^(#{1,6})\s+(.*)$", _demote, raw, flags=re.MULTILINE)
        raw = fix_relative_links(raw, md_file)
        out.append(raw)
        out.append("")
        out.append("---")
        out.append("")

    OUT_MD.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT_MD} ({count} sections)")
    if missing:
        print(f"WARNING: {len(missing)} nav entries point to missing files:")
        for m in missing[:20]:
            print(f"  - {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
