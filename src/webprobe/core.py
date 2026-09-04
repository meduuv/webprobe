"""Read-only URL parsing helpers."""

from urllib.parse import urlparse


def parse_url(url: str) -> dict[str, str]:
    """Return the useful components of a URL."""
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "host": parsed.hostname or "",
        "port": str(parsed.port or ""),
        "path": parsed.path,
        "query": parsed.query,
    }


def is_http_url(url: str) -> bool:
    """Return whether a URL uses HTTP or HTTPS."""
    return urlparse(url).scheme.casefold() in {"http", "https"}
