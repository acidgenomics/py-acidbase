"""Data manipulation utilities."""

from __future__ import annotations

from collections.abc import Hashable, Sequence
from functools import reduce
from typing import Any

import numpy as np
import pandas as pd


def dupes(x: Sequence[Hashable]) -> list:
    """Return duplicated elements.

    Parameters
    ----------
    x : sequence

    Returns
    -------
    list
        Sorted list of values appearing more than once.
    """
    seen: dict[Hashable, int] = {}
    for item in x:
        seen[item] = seen.get(item, 0) + 1
    return sorted((k for k, v in seen.items() if v > 1), key=str)


def not_dupes(x: Sequence[Hashable]) -> list:
    """Return elements that appear exactly once.

    Parameters
    ----------
    x : sequence

    Returns
    -------
    list
    """
    seen: dict[Hashable, int] = {}
    for item in x:
        seen[item] = seen.get(item, 0) + 1
    return sorted((k for k, v in seen.items() if v == 1), key=str)


def intersect_all(*args: Sequence) -> list:
    """Return the intersection of multiple sequences.

    Parameters
    ----------
    *args : sequence

    Returns
    -------
    list
    """
    if not args:
        return []
    sets = [set(a) for a in args]
    result = reduce(lambda a, b: a & b, sets)
    return sorted(result, key=str)


def intersection_matrix(*args: Sequence, names: Sequence[str] | None = None) -> pd.DataFrame:
    """Build a Boolean intersection matrix.

    Parameters
    ----------
    *args : sequence
        Collections to compare.
    names : sequence of str, optional
        Labels for each collection.

    Returns
    -------
    pandas.DataFrame
    """
    if names is None:
        names = [f"set{i + 1}" for i in range(len(args))]
    all_items = sorted(set().union(*args))
    data = {
        name: [item in set(s) for item in all_items] for name, s in zip(names, args, strict=False)
    }
    return pd.DataFrame(data, index=all_items)


def keep_only_atomic_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only columns that contain scalar (atomic) values.

    Drops columns whose elements are lists, dicts, or other
    non-scalar types.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """
    atomic_cols = []
    for col in df.columns:
        sample = df[col].dropna()
        if len(sample) == 0:
            atomic_cols.append(col)
            continue
        first = sample.iloc[0]
        if not isinstance(first, (list, dict, set, np.ndarray)):
            atomic_cols.append(col)
    return df.loc[:, atomic_cols]


def match_all(x: Sequence, table: Sequence) -> list[int]:
    """Return indices of all matches of *x* in *table*.

    Like R's ``match()`` but returns *all* positions, not just the
    first.

    Parameters
    ----------
    x : sequence
        Values to look up.
    table : sequence
        Reference table.

    Returns
    -------
    list[int]
        0-based indices into *table*.

    Raises
    ------
    KeyError
        If any element in *x* is not found in *table*.
    """
    lookup: dict[Any, list[int]] = {}
    for i, val in enumerate(table):
        lookup.setdefault(val, []).append(i)
    result: list[int] = []
    for val in x:
        if val not in lookup:
            raise KeyError(f"{val!r} not found in table")
        result.extend(lookup[val])
    return result


def match_nested(
    x: Hashable,
    table: dict | list,
) -> Hashable | None:
    """Recursively search for *x* in a nested dict/list structure.

    Parameters
    ----------
    x : object
        Value to search for.
    table : dict or list
        Nested structure.

    Returns
    -------
    object or None
        The matched value, or ``None`` if not found.
    """
    if isinstance(table, dict):
        for key, value in table.items():
            if key == x:
                return value
            found = match_nested(x, value)
            if found is not None:
                return found
    elif isinstance(table, (list, tuple)):
        for item in table:
            if item == x:
                return item
            found = match_nested(x, item)
            if found is not None:
                return found
    return None


def headtail(x: pd.DataFrame | list | np.ndarray, n: int = 2) -> None:
    """Print the first and last *n* elements / rows.

    Parameters
    ----------
    x : DataFrame, list, or array
    n : int
    """
    if isinstance(x, pd.DataFrame):
        print(x.head(n))
        print("---")
        print(x.tail(n))
    elif isinstance(x, np.ndarray):
        print(x[:n])
        print("...")
        print(x[-n:])
    else:
        seq = list(x)
        head = seq[:n]
        tail = seq[-n:]
        print(head)
        print("...")
        print(tail)
