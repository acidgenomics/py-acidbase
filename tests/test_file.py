"""Tests for acidbase._file."""

import os
import tempfile

import pytest

from acidbase import (
    basename_sans_ext,
    file_depth,
    file_ext,
    init_dir,
    parent_dir,
    parent_directory,
    realpath,
    tempdir2,
    unlink2,
)


class TestBasenameSansExt:
    """Tests for basename_sans_ext."""

    def test_simple(self) -> None:
        """Simple file extension is removed."""
        assert basename_sans_ext("file.txt") == "file"

    def test_fastq_gz(self) -> None:
        """Compound extension (.fastq.gz) is removed."""
        assert basename_sans_ext("sample.fastq.gz") == "sample"

    def test_bam(self) -> None:
        """BAM extension is removed."""
        assert basename_sans_ext("reads.bam") == "reads"

    def test_no_ext(self) -> None:
        """File without extension returns unchanged."""
        assert basename_sans_ext("Makefile") == "Makefile"

    def test_path(self) -> None:
        """Directory path is stripped along with extension."""
        assert basename_sans_ext("/path/to/file.csv") == "file"


class TestFileExt:
    """Tests for file_ext."""

    def test_simple(self) -> None:
        """Simple extension is returned."""
        assert file_ext("file.txt") == ".txt"

    def test_fastq_gz(self) -> None:
        """Compound extension is returned."""
        assert file_ext("sample.fastq.gz") == ".fastq.gz"

    def test_no_ext(self) -> None:
        """File without extension returns empty string."""
        assert file_ext("Makefile") == ""


class TestFileDepth:
    """Tests for file_depth."""

    def test_root(self) -> None:
        """File at root has depth 1."""
        assert file_depth("/file.txt") == 1

    def test_nested(self) -> None:
        """Nested file returns correct depth."""
        assert file_depth("/a/b/c.txt") == 3


class TestRealpath:
    """Tests for realpath."""

    def test_existing(self) -> None:
        """Existing file returns absolute path."""
        with tempfile.NamedTemporaryFile() as f:
            result = realpath(f.name)
            assert os.path.isabs(result)

    def test_nonexistent(self) -> None:
        """Nonexistent path raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            realpath("/nonexistent/path/abc123")


class TestInitDir:
    """Tests for init_dir."""

    def test_creates(self) -> None:
        """Creates nested directory structure."""
        with tempfile.TemporaryDirectory() as d:
            new = os.path.join(d, "sub", "dir")
            result = init_dir(new)
            assert os.path.isdir(result)


class TestTempdir2:
    """Tests for tempdir2."""

    def test_creates(self) -> None:
        """Creates a temporary directory."""
        d = tempdir2(prefix="test_")
        assert os.path.isdir(d)
        os.rmdir(d)


class TestUnlink2:
    """Tests for unlink2."""

    def test_file(self) -> None:
        """Removes a file and returns True."""
        with tempfile.NamedTemporaryFile(delete=False) as f:
            path = f.name
        assert unlink2(path) is True
        assert not os.path.exists(path)

    def test_dir(self) -> None:
        """Removes a directory and returns True."""
        d = tempfile.mkdtemp()
        assert unlink2(d) is True
        assert not os.path.exists(d)

    def test_nonexistent(self) -> None:
        """Returns False for nonexistent path."""
        assert unlink2("/nonexistent/abc123") is False


class TestParentDirectory:
    """Tests for parent_directory."""

    def test_one_level(self) -> None:
        """Returns immediate parent directory."""
        result = parent_directory("/a/b/c")
        assert result.endswith("/b") or result.endswith("\\b")

    def test_two_levels(self) -> None:
        """Returns grandparent directory with n=2."""
        result = parent_directory("/a/b/c", n=2)
        assert result.endswith("/a") or result.endswith("\\a")

    def test_alias(self) -> None:
        """parent_dir is an alias for parent_directory."""
        assert parent_dir is parent_directory
