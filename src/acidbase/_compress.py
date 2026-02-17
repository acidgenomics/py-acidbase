"""File compression / decompression utilities."""

from __future__ import annotations

import bz2
import gzip
import lzma
import shutil
import zipfile
from pathlib import Path


def compress(
    path: str | Path,
    method: str = "gz",
    *,
    remove: bool = True,
) -> str:
    """Compress a file.

    Parameters
    ----------
    path : str or Path
        File to compress.
    method : str
        One of ``'gz'``, ``'bz2'``, ``'xz'``, ``'zip'``.
    remove : bool
        Delete the original file after compression (default ``True``).

    Returns
    -------
    str
        Path to the compressed file.
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(str(path))

    openers = {
        "gz": (gzip.open, f"{path}.gz"),
        "bz2": (bz2.open, f"{path}.bz2"),
        "xz": (lzma.open, f"{path}.xz"),
    }

    if method in openers:
        opener, out_path = openers[method]
        with open(path, "rb") as f_in, opener(out_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    elif method == "zip":
        out_path = f"{path}.zip"
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(path, path.name)
    else:
        raise ValueError(f"Unsupported method {method!r}. Use 'gz', 'bz2', 'xz', or 'zip'.")

    if remove:
        path.unlink()
    return str(out_path)


def decompress(
    path: str | Path,
    *,
    remove: bool = True,
) -> str:
    """Decompress a file.

    Parameters
    ----------
    path : str or Path
        Compressed file (``.gz``, ``.bz2``, ``.xz``, or ``.zip``).
    remove : bool
        Delete the compressed file after extraction (default ``True``).

    Returns
    -------
    str
        Path to the decompressed file.
    """
    path = Path(path)
    suffix = path.suffix.lower()
    out_path = str(path.with_suffix(""))

    openers = {
        ".gz": gzip.open,
        ".bz2": bz2.open,
        ".xz": lzma.open,
    }

    if suffix in openers:
        with openers[suffix](path, "rb") as f_in, open(out_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    elif suffix == ".zip":
        with zipfile.ZipFile(path, "r") as zf:
            names = zf.namelist()
            if len(names) == 1:
                out_path = str(path.parent / names[0])
            zf.extractall(path.parent)
    else:
        raise ValueError(f"Unsupported suffix {suffix!r}.")

    if remove:
        path.unlink()
    return out_path
