"""Tests for acidbase._string."""

import pytest

from acidbase import (
    print_string,
    str_extract,
    str_extract_all,
    str_match,
    str_match_all,
    str_pad,
    str_remove_empty,
    str_replace_na,
    str_split,
    truncate_string,
)


class TestStrExtract:
    """Tests for str_extract."""

    def test_group_match(self) -> None:
        """Extracts first capture group match."""
        assert str_extract("abc123def", r"(\d+)") == "123"

    def test_no_group(self) -> None:
        """Extracts match without capture group."""
        assert str_extract("abc123def", r"\d+") == "123"

    def test_no_match(self) -> None:
        """Returns None when no match found."""
        assert str_extract("abcdef", r"\d+") is None


class TestStrExtractAll:
    """Tests for str_extract_all."""

    def test_multiple_matches(self) -> None:
        """Extracts all matches from string."""
        assert str_extract_all("a1b2c3", r"\d") == ["1", "2", "3"]

    def test_no_match(self) -> None:
        """Returns empty list when no match found."""
        assert str_extract_all("abc", r"\d") == []


class TestStrMatch:
    """Tests for str_match."""

    def test_match(self) -> None:
        """Returns match object for matching pattern."""
        m = str_match("hello world", r"world")
        assert m is not None
        assert m.group() == "world"

    def test_no_match(self) -> None:
        """Returns None when pattern does not match."""
        assert str_match("hello", r"xyz") is None


class TestStrMatchAll:
    """Tests for str_match_all."""

    def test_multiple(self) -> None:
        """Returns all non-overlapping matches."""
        matches = str_match_all("aabaa", r"a+")
        assert len(matches) == 2

    def test_empty(self) -> None:
        """Returns empty list when no matches found."""
        assert str_match_all("abc", r"\d+") == []


class TestStrPad:
    """Tests for str_pad."""

    def test_left(self) -> None:
        """Left padding adds spaces to the left."""
        assert str_pad("x", 5, side="left") == "    x"

    def test_right(self) -> None:
        """Right padding adds spaces to the right."""
        assert str_pad("x", 5, side="right") == "x    "

    def test_both(self) -> None:
        """Both-side padding centers the string."""
        result = str_pad("x", 5, side="both")
        assert len(result) == 5

    def test_custom_pad(self) -> None:
        """Custom pad character is used."""
        assert str_pad("1", 3, side="left", pad="0") == "001"

    def test_invalid_pad(self) -> None:
        """Multi-character pad raises ValueError."""
        with pytest.raises(ValueError):
            str_pad("x", 5, pad="ab")

    def test_invalid_side(self) -> None:
        """Invalid side argument raises ValueError."""
        with pytest.raises(ValueError):
            str_pad("x", 5, side="middle")


class TestStrRemoveEmpty:
    """Tests for str_remove_empty."""

    def test_removes_empty(self) -> None:
        """Empty strings and None values are removed."""
        assert str_remove_empty(["a", "", "b", None, "c"]) == ["a", "b", "c"]

    def test_all_empty(self) -> None:
        """All-empty input returns empty list."""
        assert str_remove_empty(["", None]) == []


class TestStrReplaceNa:
    """Tests for str_replace_na."""

    def test_basic(self) -> None:
        """None values are replaced with NA string."""
        assert str_replace_na(["a", None, "b"]) == ["a", "NA", "b"]

    def test_custom(self) -> None:
        """Custom replacement string is used."""
        assert str_replace_na([None], replace="?") == ["?"]


class TestStrSplit:
    """Tests for str_split."""

    def test_basic(self) -> None:
        """Splits string by regex pattern."""
        assert str_split("a-b-c", r"-") == ["a", "b", "c"]


class TestTruncateString:
    """Tests for truncate_string."""

    def test_short(self) -> None:
        """Short string is returned unchanged."""
        assert truncate_string("hi", 10) == "hi"

    def test_long(self) -> None:
        """Long string is truncated with ellipsis."""
        result = truncate_string("a" * 300, 200)
        assert len(result) == 203  # 200 + "..."
        assert result.endswith("...")


class TestPrintString:
    """Tests for print_string."""

    def test_list(self) -> None:
        """List is joined with comma separator."""
        assert print_string([1, 2, 3]) == "1, 2, 3"

    def test_scalar(self) -> None:
        """Scalar value is converted to string."""
        assert print_string(42) == "42"
