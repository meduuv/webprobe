from webprobe import is_http_url, parse_url


def test_parse_url():
    assert is_http_url("https://example.com/a")
    assert parse_url("https://example.com/a?q=1")["host"] == "example.com"
