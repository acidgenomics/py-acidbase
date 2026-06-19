"""Mathematical / statistical helper functions."""

import numpy as np
import pandas as pd


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
    remove_na: bool = True,
    zero_propagate: bool = False,
) -> float:
    """Compute the geometric mean.

    Parameters
    ----------
    x : array-like
        Numeric vector.
    remove_na : bool
        If ``True`` (default), ``NA``/``NaN`` values are removed before
        computing.
    zero_propagate : bool
        If ``True``, return ``0`` when any element is zero.
        If ``False`` (default), zeros are excluded before computing, but the
        full length of ``x`` (including zeros) is used as the denominator —
        matching R's ``geometricMean`` default.

    Returns
    -------
    float

    Notes
    -----
    Returns ``NaN`` when any element is negative (R semantics).
    """
    x = np.asarray(x, dtype=float)
    if remove_na:
        x = x[~np.isnan(x)]
    if len(x) == 0:
        return float("nan")
    # Any negative value → NaN (matches R)
    if np.any(x < 0):
        return float("nan")
    if zero_propagate:
        if np.any(x == 0):
            return 0.0
        return float(np.exp(np.mean(np.log(x))))
    # Divide by FULL length (including excluded zeros), not len(positives)
    n = len(x)
    log_sum = np.sum(np.log(x[x > 0]))
    return float(np.exp(log_sum / n))


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
        Fold-change values. Negative values are treated as reciprocal
        fold changes: ``-4`` means ``1/4``.
    base : int
        Logarithm base (default ``2``).

    Returns
    -------
    float or numpy.ndarray

    Notes
    -----
    Matches R's ``foldChangeToLogRatio`` semantics: negative fold changes are
    first transformed to ``1 / -x`` before taking the logarithm, so the result
    is negative (down-regulation) as expected.
    """
    x = np.asarray(x, dtype=float)
    # Negative fold change → reciprocal (R: object <- ifelse(object < 0, 1/-object, object))
    transformed = np.where(x < 0, 1.0 / (-x), x)
    result = np.log(transformed) / np.log(base)
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

    Notes
    -----
    Matches R's ``logRatioToFoldChange`` semantics: after exponentiation, any
    result ``< 1`` is replaced by ``-1 / result`` to give a negative fold
    change representing down-regulation.
    """
    x = np.asarray(x, dtype=float)
    fc = np.float_power(base, x)
    # Where result < 1 → -1/fc  (R: ifelse(object < 1, -1/object, object))
    result = np.where(fc < 1.0, -1.0 / fc, fc)
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
        Data frame of the same shape containing ranks, preserving
        index and column names.
    """
    return x.rank(method="average")
