"""Version-string utilities."""

import warnings

from packaging.version import Version


def major_version(version: str) -> str:
    """Return the major component of a version string.

    Parameters
    ----------
    version : str
        Version string to parse.

    Returns
    -------
    str
        Major version component.
    """
    v = Version(version)
    return str(v.major)


def major_minor_version(version: str) -> str:
    """Return ``major.minor`` from a version string.

    Parameters
    ----------
    version : str
        Version string to parse.

    Returns
    -------
    str
        ``"major.minor"`` component.
    """
    v = Version(version)
    return f"{v.major}.{v.minor}"


def minor_version(version: str) -> str:
    """Return ``major.minor`` from a version string.

    Parameters
    ----------
    version : str
        Version string to parse.

    Returns
    -------
    str
        ``"major.minor"`` component.

    .. deprecated::
        Use :func:`major_minor_version` instead. This function is
        preserved for R API parity only.
    """
    warnings.warn(
        "minor_version() is deprecated; use major_minor_version() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return major_minor_version(version)


def sanitize_version(version: str) -> str:
    """Normalise a version string using PEP 440.

    Parameters
    ----------
    version : str
        Version string to normalize.

    Returns
    -------
    str
        PEP 440-normalized version string.
    """
    return str(Version(version))
