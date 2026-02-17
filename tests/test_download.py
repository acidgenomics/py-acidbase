"""Tests for acidbase._download."""

from acidbase import paste_url


class TestPasteUrl:
    """Tests for paste_url."""

    def test_basic(self) -> None:
        """Joins URL components with slashes."""
        assert (
            paste_url("https://example.com", "path", "file.txt")
            == "https://example.com/path/file.txt"
        )

    def test_strips_slashes(self) -> None:
        """Extra slashes are stripped from components."""
        assert (
            paste_url("https://example.com/", "/path/", "/file") == "https://example.com/path/file"
        )
