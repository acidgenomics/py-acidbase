"""Package cache directory management."""

from __future__ import annotations

import os
from pathlib import Path


def pkg_cache_dir(
    package: str = "acidbase",
    *,
    xdg: bool = True,
) -> str:
    """Return (and create) a package-specific cache directory.

    Follows the XDG Base Directory Specification by default.

    Parameters
    ----------
    package : str
    xdg : bool
        Use ``$XDG_CACHE_HOME`` (default ``True``).

    Returns
    -------
    str
    """
    if xdg:
        base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    else:
        base = Path.home() / ".cache"
    cache_dir = base / package
    cache_dir.mkdir(parents=True, exist_ok=True)
    return str(cache_dir)
