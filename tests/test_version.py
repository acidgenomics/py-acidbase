"""Tests for acidbase._version."""

from acidbase import major_minor_version, major_version, sanitize_version


class TestMajorVersion:
    """Tests for major_version."""

    def test_basic(self) -> None:
        """Extracts major version component."""
        assert major_version("3.6.1") == "3"


class TestMajorMinorVersion:
    """Tests for major_minor_version."""

    def test_basic(self) -> None:
        """Extracts major.minor version components."""
        assert major_minor_version("3.6.1") == "3.6"


class TestSanitizeVersion:
    """Tests for sanitize_version."""

    def test_basic(self) -> None:
        """Valid version string is unchanged."""
        result = sanitize_version("1.2.3")
        assert result == "1.2.3"

    def test_normalise(self) -> None:
        """Leading zeros are normalized."""
        result = sanitize_version("1.02.003")
        assert result == "1.2.3"
