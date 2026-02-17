"""Tests for acidbase._compress."""

import os
import tempfile

import pytest

from acidbase import compress, decompress


def _make_tmp_file(content: bytes = b"hello world\n") -> str:
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, "wb") as f:
        f.write(content)
    return path


class TestCompress:
    """Tests for compress and decompress."""

    @pytest.mark.parametrize("method", ["gz", "bz2", "xz", "zip"])
    def test_roundtrip(self, method: str) -> None:
        """Roundtrip compress/decompress preserves content."""
        original = _make_tmp_file()
        with open(original, "rb") as f:
            expected = f.read()
        compressed = compress(original, method=method, remove=True)
        assert os.path.isfile(compressed)
        assert not os.path.exists(original)
        decompressed = decompress(compressed, remove=True)
        assert os.path.isfile(decompressed)
        with open(decompressed, "rb") as f:
            assert f.read() == expected
        os.unlink(decompressed)

    def test_keep_original(self) -> None:
        """Original file is kept when remove=False."""
        original = _make_tmp_file()
        compressed = compress(original, method="gz", remove=False)
        assert os.path.exists(original)
        os.unlink(original)
        os.unlink(compressed)

    def test_invalid_method(self) -> None:
        """Invalid method raises ValueError."""
        original = _make_tmp_file()
        with pytest.raises(ValueError):
            compress(original, method="rar")
        os.unlink(original)
