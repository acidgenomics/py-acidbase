"""Tests for acidbase._path_string."""

import os

from acidbase import (
    add_to_path_end,
    add_to_path_start,
    collapse_to_path_string,
    remove_from_path,
    split_path_string,
    unique_path_string,
)

SEP = os.pathsep


class TestCollapseToPathString:
    """Tests for collapse_to_path_string."""

    def test_basic(self) -> None:
        """Joins paths with OS path separator."""
        result = collapse_to_path_string("/a", "/b", "/c")
        assert result == f"/a{SEP}/b{SEP}/c"


class TestSplitPathString:
    """Tests for split_path_string."""

    def test_basic(self) -> None:
        """Splits path string into list of paths."""
        result = split_path_string(f"/a{SEP}/b{SEP}/c")
        assert result == ["/a", "/b", "/c"]


class TestUniquePathString:
    """Tests for unique_path_string."""

    def test_dedup(self) -> None:
        """Duplicate paths are removed."""
        ps = f"/a{SEP}/b{SEP}/a{SEP}/c"
        result = unique_path_string(ps)
        assert result == f"/a{SEP}/b{SEP}/c"


class TestAddToPathEnd:
    """Tests for add_to_path_end."""

    def test_add(self) -> None:
        """Appends path to end of path string."""
        result = add_to_path_end(f"/a{SEP}/b", "/c")
        assert result.endswith(f"{SEP}/c")

    def test_already_present(self) -> None:
        """Already present path is not duplicated."""
        ps = f"/a{SEP}/b"
        result = add_to_path_end(ps, "/a")
        assert result == ps


class TestAddToPathStart:
    """Tests for add_to_path_start."""

    def test_add(self) -> None:
        """Prepends path to start of path string."""
        result = add_to_path_start(f"/a{SEP}/b", "/c")
        assert result.startswith(f"/c{SEP}")


class TestRemoveFromPath:
    """Tests for remove_from_path."""

    def test_remove(self) -> None:
        """Removes specified path from path string."""
        ps = f"/a{SEP}/b{SEP}/c"
        result = remove_from_path(ps, "/b")
        assert result == f"/a{SEP}/c"
