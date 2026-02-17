"""Tests for acidbase._data."""

import pandas as pd
import pytest

from acidbase import (
    dupes,
    headtail,
    intersect_all,
    intersection_matrix,
    keep_only_atomic_cols,
    match_all,
    match_nested,
    not_dupes,
)


class TestDupes:
    """Tests for dupes."""

    def test_basic(self) -> None:
        """Returns duplicated values."""
        assert dupes([1, 2, 2, 3, 3, 3]) == [2, 3]

    def test_no_dupes(self) -> None:
        """Returns empty list when no duplicates."""
        assert dupes([1, 2, 3]) == []


class TestNotDupes:
    """Tests for not_dupes."""

    def test_basic(self) -> None:
        """Returns non-duplicated values."""
        assert not_dupes([1, 2, 2, 3]) == [1, 3]


class TestIntersectAll:
    """Tests for intersect_all."""

    def test_basic(self) -> None:
        """Returns elements common to all inputs."""
        result = intersect_all([1, 2, 3], [2, 3, 4], [3, 4, 5])
        assert result == [3]

    def test_empty(self) -> None:
        """No arguments returns empty list."""
        assert intersect_all() == []


class TestIntersectionMatrix:
    """Tests for intersection_matrix."""

    def test_basic(self) -> None:
        """Returns DataFrame with boolean membership."""
        result = intersection_matrix([1, 2, 3], [2, 3, 4], names=["a", "b"])
        assert isinstance(result, pd.DataFrame)
        assert result.loc[2, "a"] is True or result.loc[2, "a"]
        assert result.loc[4, "a"] is False or not result.loc[4, "a"]


class TestKeepOnlyAtomicCols:
    """Tests for keep_only_atomic_cols."""

    def test_basic(self) -> None:
        """Removes columns with non-atomic values."""
        df = pd.DataFrame(
            {
                "a": [1, 2, 3],
                "b": ["x", "y", "z"],
                "c": [[1], [2], [3]],
            }
        )
        result = keep_only_atomic_cols(df)
        assert "a" in result.columns
        assert "b" in result.columns
        assert "c" not in result.columns


class TestMatchAll:
    """Tests for match_all."""

    def test_basic(self) -> None:
        """Returns indices of matched elements."""
        result = match_all(["b", "a"], ["a", "b", "c"])
        assert result == [1, 0]

    def test_missing(self) -> None:
        """Missing element raises KeyError."""
        with pytest.raises(KeyError):
            match_all(["z"], ["a", "b"])


class TestMatchNested:
    """Tests for match_nested."""

    def test_dict(self) -> None:
        """Finds value in nested dictionary."""
        data = {"a": {"b": {"c": 42}}}
        assert match_nested("c", data) == 42

    def test_not_found(self) -> None:
        """Returns None when key not found."""
        assert match_nested("z", {"a": 1}) is None


class TestHeadtail:
    """Tests for headtail."""

    def test_list(self, capsys: pytest.CaptureFixture) -> None:
        """Prints head and tail of list."""
        headtail([1, 2, 3, 4, 5], n=2)
        captured = capsys.readouterr()
        assert "1" in captured.out
        assert "5" in captured.out
