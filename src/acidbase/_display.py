"""Display / pretty-print helpers."""

from __future__ import annotations


def show_slot_info(obj: object) -> str:
    """Return a formatted summary of an object's attributes.

    Parameters
    ----------
    obj : object

    Returns
    -------
    str
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
    width : int

    Returns
    -------
    str
    """
    return f"{'─' * 3} {text} {'─' * (width - len(text) - 5)}"


def simple_class(obj: object) -> str:
    """Return the simple class name (without module path).

    Parameters
    ----------
    obj : object

    Returns
    -------
    str
    """
    return type(obj).__name__
