"""String manipulation utilities."""

from __future__ import annotations

import re


def str_extract(string: str, pattern: str) -> str | None:
    """Extract first match of *pattern* from *string*.

    Parameters
    ----------
    string : str
        Input string.
    pattern : str
        Regular-expression pattern (should contain a group).

    Returns
    -------
    str or None
        First captured group, or None when no match.
    """
    m = re.search(pattern, string)
    if m is None:
        return None
    return m.group(1) if m.lastindex else m.group(0)


def str_extract_all(string: str, pattern: str) -> list[str]:
    """Return all matches of *pattern* in *string*.

    Parameters
    ----------
    string : str
        Input string.
    pattern : str
        Regular-expression pattern.

    Returns
    -------
    list[str]
        All matches of ``pattern`` in ``string``.
    """
    return re.findall(pattern, string)


def str_match(string: str, pattern: str) -> re.Match[str] | None:
    """Return the first regex match object of *pattern* in *string*.

    Parameters
    ----------
    string : str
        Input string.
    pattern : str
        Regular-expression pattern.

    Returns
    -------
    re.Match or None
        First match object, or None when no match.
    """
    return re.search(pattern, string)


def str_match_all(string: str, pattern: str) -> list[re.Match[str]]:
    """Return all regex match objects for *pattern* in *string*.

    Parameters
    ----------
    string : str
        Input string.
    pattern : str
        Regular-expression pattern.

    Returns
    -------
    list[re.Match]
        All match objects for ``pattern`` in ``string``.
    """
    return list(re.finditer(pattern, string))


def str_pad(
    string: str,
    width: int,
    side: str = "left",
    pad: str = " ",
) -> str:
    """Pad a string to a minimum *width*.

    Parameters
    ----------
    string : str
        Input string.
    width : int
        Desired minimum width of the output.
    side : str
        One of 'left', 'right', or 'both'.
    pad : str
        Single character used for padding.

    Returns
    -------
    str
        Padded string.
    """
    if len(pad) != 1:
        raise ValueError("'pad' must be a single character.")
    if side == "left":
        return string.rjust(width, pad)
    if side == "right":
        return string.ljust(width, pad)
    if side == "both":
        return string.center(width, pad)
    raise ValueError("'side' must be 'left', 'right', or 'both'.")


def str_remove_empty(x: list[str]) -> list[str]:
    """Remove empty strings and None values from a list.

    Parameters
    ----------
    x : list[str]
        Input list, possibly containing ``None`` or empty strings.

    Returns
    -------
    list[str]
        ``x`` with ``None`` and empty-string elements removed.
    """
    return [s for s in x if s is not None and s != ""]


def str_replace_na(x: list[str | None], replace: str = "NA") -> list[str]:
    """Replace None values with a placeholder string.

    Parameters
    ----------
    x : list[str | None]
        Input list, possibly containing ``None``.
    replace : str
        Placeholder used in place of ``None``.

    Returns
    -------
    list[str]
        ``x`` with every ``None`` replaced by ``replace``.
    """
    return [replace if v is None else v for v in x]


def str_split(string: str, pattern: str) -> list[str]:
    """Split *string* by a regex *pattern*.

    Parameters
    ----------
    string : str
        Input string.
    pattern : str
        Regular-expression pattern to split on.

    Returns
    -------
    list[str]
        Substrings between matches of ``pattern``.
    """
    return re.split(pattern, string)


def truncate_string(string: str, n: int = 200) -> str:
    """Truncate *string* to *n* characters, appending '...' if needed.

    Parameters
    ----------
    string : str
        Input string.
    n : int
        Maximum length before truncation.

    Returns
    -------
    str
        ``string`` unchanged if within ``n`` characters, otherwise truncated
        with an appended ``"..."``.
    """
    if len(string) <= n:
        return string
    return string[:n] + "..."


def print_string(x: object) -> str:
    """Coerce an object to a human-friendly print string.

    Parameters
    ----------
    x : object
        Value to render. Lists, tuples, and sets are joined with ``", "``.

    Returns
    -------
    str
        Human-readable string representation of ``x``.
    """
    if isinstance(x, (list, tuple, set)):
        return ", ".join(str(i) for i in x)
    return str(x)
