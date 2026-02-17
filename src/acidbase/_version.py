"""Version-string utilities."""

from __future__ import annotations

from packaging.version import Version


def major_version(version: str) -> str:
    """Return the major component of a version string.

    Parameters
    ----------
    version : str

    Returns
    -------
    str
    """
    v = Version(version)
    return str(v.major)


def major_minor_version(version: str) -> str:
    """Return ``major.minor`` from a version string.

    Parameters
    ----------
    version : str

    Returns
    -------
    str
    """
    v = Version(version)
    return f"{v.major}.{v.minor}"


def sanitize_version(version: str) -> str:
    """Normalise a version string using PEP 440.

    Parameters
    ----------
    version : str

    Returns
    -------
    str
    """
    return str(Version(version))
