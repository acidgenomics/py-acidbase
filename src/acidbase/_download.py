"""Download / URL utilities."""

from __future__ import annotations

import os
import urllib.request
from pathlib import Path


def download(
    url: str,
    dest: str | Path | None = None,
) -> str:
    """Download a file from *url*.

    Parameters
    ----------
    url : str
    dest : str or Path, optional
        Destination path.  Defaults to the current directory using the
        URL basename.

    Returns
    -------
    str
        Absolute path to the downloaded file.
    """
    if dest is None:
        dest = Path.cwd() / os.path.basename(url)
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, str(dest))
    return str(dest.resolve())


def paste_url(*parts: str) -> str:
    """Join URL parts with ``/``.

    Parameters
    ----------
    *parts : str

    Returns
    -------
    str
    """
    return "/".join(p.strip("/") for p in parts)
