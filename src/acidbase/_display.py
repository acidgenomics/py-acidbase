"""Display / pretty-print helpers."""

from __future__ import annotations


def show_slot_info(obj: object) -> str:
    """Return a formatted summary of an object's attributes.

    Parameters
    ----------
    obj : object
        Object whose ``__dict__`` attributes are summarized.

    Returns
    -------
    str
        One ``"  name (Type)"`` line per attribute, sorted by name.
    """
    lines: list[str] = []
    attrs = vars(obj) if hasattr(obj, "__dict__") else {}
    for name, value in sorted(attrs.items()):
        cls = type(value).__name__
        lines.append(f"  {name} ({cls})")
    return "\n".join(lines)


def show_header(text: str, width: int = 72) -> str:
    """Return a formatted header line.

    Parameters
    ----------
    text : str
        Header text.
    width : int
        Total width of the rendered line.

    Returns
    -------
    str
        A single line: three dashes, ``text``, then dashes padding to
        ``width``.
    """
    return f"{'─' * 3} {text} {'─' * (width - len(text) - 5)}"


def simple_class(obj: object) -> str:
    """Return the simple class name (without module path).

    Parameters
    ----------
    obj : object
        Object to inspect.

    Returns
    -------
    str
        ``type(obj).__name__``.
    """
    return type(obj).__name__
