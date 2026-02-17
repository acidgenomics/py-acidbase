"""File-path utility functions."""

from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path

from acidbase._constants import _compress_ext_pattern, _ext_pattern


def basename_sans_ext(path: str | Path) -> str:
    """Return the file basename without extension(s).

    Strips recognised bioinformatics extensions *and* compression
    suffixes so that ``"sample.fastq.gz"`` becomes ``"sample"``.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    str
    """
    name = Path(path).name
    name = _compress_ext_pattern.sub("", name)
    name = _ext_pattern.sub("", name)
    if name == Path(path).name:
        return Path(path).stem
    return name


def file_ext(path: str | Path) -> str:
    """Return the file extension(s) including compression suffix.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    str
        Extension string *with* leading dot, e.g. ``".fastq.gz"``.
        Empty string when there is no extension.
    """
    name = Path(path).name
    base = basename_sans_ext(path)
    if base == name:
        return ""
    return name[len(base) :]


def file_depth(path: str | Path) -> int:
    """Return the directory depth of *path*.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    int
    """
    return len(Path(path).parts) - 1


def realpath(path: str | Path) -> str:
    """Resolve *path* to an absolute real path.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    str

    Raises
    ------
    FileNotFoundError
        If the resolved path does not exist.
    """
    resolved = str(Path(path).resolve())
    if not os.path.exists(resolved):
        raise FileNotFoundError(resolved)
    return resolved


def init_dir(path: str | Path) -> str:
    """Create a directory (and parents) if it does not exist.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    str
        The absolute path of the created directory.
    """
    p = Path(path).resolve()
    p.mkdir(parents=True, exist_ok=True)
    return str(p)


def tempdir2(*, prefix: str | None = None) -> str:
    """Create a unique temporary directory.

    Unlike :func:`tempfile.mkdtemp`, the directory name is more
    human-readable when *prefix* is supplied.

    Parameters
    ----------
    prefix : str, optional

    Returns
    -------
    str
        Absolute path to the new temporary directory.
    """
    return tempfile.mkdtemp(prefix=prefix)


def unlink2(path: str | Path) -> bool:
    """Delete a file or directory tree.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    bool
        ``True`` if something was deleted.
    """
    p = Path(path)
    if p.is_dir():
        shutil.rmtree(p)
        return True
    if p.exists():
        p.unlink()
        return True
    return False


def parent_directory(path: str | Path, n: int = 1) -> str:
    """Return the *n*-th parent directory of *path*.

    Parameters
    ----------
    path : str or Path
    n : int
        Number of levels to go up (default ``1``).

    Returns
    -------
    str
    """
    p = Path(path).resolve()
    for _ in range(n):
        p = p.parent
    return str(p)


parent_dir = parent_directory
