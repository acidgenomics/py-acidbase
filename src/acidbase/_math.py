"""Mathematical / statistical helper functions."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import rankdata


def euclidean(a: np.ndarray, b: np.ndarray) -> float:
    """Compute the Euclidean distance between two vectors.

    Parameters
    ----------
    a, b : array-like

    Returns
    -------
    float
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return float(np.sqrt(np.sum((a - b) ** 2)))


def geometric_mean(
    x: np.ndarray,
    *,
    zero_propagate: bool = False,
) -> float:
    """Compute the geometric mean.

    Parameters
    ----------
    x : array-like
        Numeric vector.
    zero_propagate : bool
        If ``True``, return ``0`` when any element is zero.
        If ``False`` (default), zeros are excluded before computing.

    Returns
    -------
    float
    """
    x = np.asarray(x, dtype=float)
    if zero_propagate:
        if np.any(x == 0):
            return 0.0
    else:
        x = x[x > 0]
    if len(x) == 0:
        return float("nan")
    return float(np.exp(np.mean(np.log(x))))


def sem(x: np.ndarray) -> float:
    """Compute the standard error of the mean.

    Parameters
    ----------
    x : array-like

    Returns
    -------
    float
    """
    x = np.asarray(x, dtype=float)
    return float(np.std(x, ddof=1) / np.sqrt(len(x)))


def zscore(x: np.ndarray) -> np.ndarray:
    """Compute Z-scores (column-wise for matrices).

    Parameters
    ----------
    x : array-like
        Numeric vector or 2-D array.

    Returns
    -------
    numpy.ndarray
    """
    x = np.asarray(x, dtype=float)
    if x.ndim == 1:
        return (x - np.mean(x)) / np.std(x, ddof=1)
    return (x - x.mean(axis=0)) / x.std(axis=0, ddof=1)


def fold_change_to_log_ratio(x: float | np.ndarray, base: int = 2) -> float | np.ndarray:
    """Convert fold change to log ratio.

    Parameters
    ----------
    x : float or array-like
        Fold-change values.
    base : int
        Logarithm base (default ``2``).

    Returns
    -------
    float or numpy.ndarray
    """
    x = np.asarray(x, dtype=float)
    result = np.where(x >= 0, np.log(x), -np.log(np.abs(x))) / np.log(base)
    return float(result) if result.ndim == 0 else result


def log_ratio_to_fold_change(x: float | np.ndarray, base: int = 2) -> float | np.ndarray:
    """Convert log ratio to fold change.

    Parameters
    ----------
    x : float or array-like
        Log-ratio values.
    base : int
        Logarithm base (default ``2``).

    Returns
    -------
    float or numpy.ndarray
    """
    x = np.asarray(x, dtype=float)
    result = np.where(x >= 0, base**x, -(base ** np.abs(x)))
    return float(result) if result.ndim == 0 else result


def ranked_matrix(
    x: pd.DataFrame,
) -> pd.DataFrame:
    """Rank values within each column, with ties averaged.

    Parameters
    ----------
    x : pandas.DataFrame
        Numeric data frame.

    Returns
    -------
    pandas.DataFrame
        Data frame of the same shape containing ranks.
    """
    ranked = x.apply(lambda col: rankdata(col, method="average"))
    return ranked
