"""Dependency-free checks for the Training Heights GitHub Pages site."""

from html.parser import HTMLParser
from pathlib import Path
import sys


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_depth = 0
        self.title = ""
        self.has_viewport = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "title":
            self.title_depth += 1
        if tag == "meta" and attributes.get("name") == "viewport":
            self.has_viewport = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.title_depth = max(0, self.title_depth - 1)

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title += data


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


site = Path(__file__).resolve().parents[1]
index = site / "index.html"

if not index.is_file():
    fail("index.html is missing from the repository root")

html = index.read_text(encoding="utf-8")
if not html.lstrip().lower().startswith("<!doctype html>"):
    fail("index.html must start with an HTML5 doctype")

parser = SiteParser()
try:
    parser.feed(html)
    parser.close()
except Exception as exc:
    fail(f"index.html could not be parsed: {exc}")

if not parser.title.strip():
    fail("index.html must contain a non-empty <title>")
if not parser.has_viewport:
    fail("index.html must contain a viewport meta tag")

print(f"PASS: index.html is deployable (title: {parser.title.strip()})")

