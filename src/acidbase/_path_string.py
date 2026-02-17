"""PATH-string manipulation utilities.

Operates on colon-separated (``:``) path strings such as ``$PATH``.
"""

from __future__ import annotations

import os


def collapse_to_path_string(*paths: str) -> str:
    """Join paths into a single colon-separated string.

    Parameters
    ----------
    *paths : str

    Returns
    -------
    str
    """
    return os.pathsep.join(paths)


def split_path_string(path_string: str) -> list[str]:
    """Split a colon-separated path string.

    Parameters
    ----------
    path_string : str

    Returns
    -------
    list[str]
    """
    return path_string.split(os.pathsep)


def unique_path_string(path_string: str) -> str:
    """Remove duplicate entries from a path string.

    Parameters
    ----------
    path_string : str

    Returns
    -------
    str
    """
    seen: set[str] = set()
    unique: list[str] = []
    for p in split_path_string(path_string):
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return collapse_to_path_string(*unique)


def add_to_path_end(path_string: str, new_path: str) -> str:
    """Append *new_path* to the end of a path string (if not present).

    Parameters
    ----------
    path_string : str
    new_path : str

    Returns
    -------
    str
    """
    parts = split_path_string(path_string)
    if new_path not in parts:
        parts.append(new_path)
    return collapse_to_path_string(*parts)


def add_to_path_start(path_string: str, new_path: str) -> str:
    """Prepend *new_path* to the start of a path string (if not present).

    Parameters
    ----------
    path_string : str
    new_path : str

    Returns
    -------
    str
    """
    parts = split_path_string(path_string)
    if new_path in parts:
        parts.remove(new_path)
    parts.insert(0, new_path)
    return collapse_to_path_string(*parts)


def remove_from_path(path_string: str, target: str) -> str:
    """Remove *target* from a path string.

    Parameters
    ----------
    path_string : str
    target : str

    Returns
    -------
    str
    """
    parts = [p for p in split_path_string(path_string) if p != target]
    return collapse_to_path_string(*parts)
