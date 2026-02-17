"""Tests for acidbase._system."""

from acidbase import cpus, random_string, shell


class TestCpus:
    """Tests for cpus."""

    def test_default(self) -> None:
        """Default returns at least 1 CPU."""
        assert cpus() >= 1

    def test_cap(self) -> None:
        """CPU count is capped at requested maximum."""
        assert cpus(2) <= 2

    def test_all(self) -> None:
        """Zero requests all available CPUs."""
        assert cpus(0) >= 1


class TestRandomString:
    """Tests for random_string."""

    def test_length(self) -> None:
        """Generated string has requested length."""
        assert len(random_string(16)) == 16

    def test_unique(self) -> None:
        """Successive calls produce unique strings."""
        assert random_string() != random_string()

    def test_alphanumeric(self) -> None:
        """Generated string is alphanumeric."""
        s = random_string(100)
        assert s.isalnum()


class TestShell:
    """Tests for shell."""

    def test_echo(self) -> None:
        """Captures stdout from shell command."""
        result = shell("echo hello")
        assert result.stdout.strip() == "hello"

    def test_exit_code(self) -> None:
        """Successful command returns exit code 0."""
        result = shell("true")
        assert result.returncode == 0
