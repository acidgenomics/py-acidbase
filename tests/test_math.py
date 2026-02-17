"""Tests for acidbase._math."""

import numpy as np
import pandas as pd
import pytest

from acidbase import (
    euclidean,
    fold_change_to_log_ratio,
    geometric_mean,
    log_ratio_to_fold_change,
    ranked_matrix,
    sem,
    zscore,
)


class TestEuclidean:
    """Tests for euclidean."""

    def test_basic(self) -> None:
        """Euclidean distance of 3-4-5 triangle is 5."""
        assert euclidean([0, 0], [3, 4]) == pytest.approx(5.0)

    def test_same(self) -> None:
        """Same points have zero distance."""
        assert euclidean([1, 2], [1, 2]) == 0.0


class TestGeometricMean:
    """Tests for geometric_mean."""

    def test_basic(self) -> None:
        """Geometric mean of 2 and 8 is 4."""
        result = geometric_mean([2, 8])
        assert result == pytest.approx(4.0)

    def test_zero_propagate(self) -> None:
        """Zero propagation returns 0 when zeros present."""
        assert geometric_mean([0, 1, 2], zero_propagate=True) == 0.0

    def test_zero_excluded(self) -> None:
        """Zeros are excluded by default."""
        result = geometric_mean([0, 1, 2, 3])
        assert result > 0


class TestSem:
    """Tests for sem."""

    def test_basic(self) -> None:
        """Standard error of the mean matches expected value."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = sem(x)
        expected = np.std(x, ddof=1) / np.sqrt(5)
        assert result == pytest.approx(expected)


class TestZscore:
    """Tests for zscore."""

    def test_vector(self) -> None:
        """Z-scored values have mean of zero."""
        result = zscore([1, 2, 3, 4, 5])
        assert result.mean() == pytest.approx(0.0, abs=1e-10)


class TestFoldChangeLogRatio:
    """Tests for fold_change_to_log_ratio and log_ratio_to_fold_change."""

    def test_roundtrip(self) -> None:
        """Roundtrip conversion preserves original value."""
        fc = 4.0
        lr = fold_change_to_log_ratio(fc, base=2)
        assert lr == pytest.approx(2.0)
        back = log_ratio_to_fold_change(lr, base=2)
        assert back == pytest.approx(fc)


class TestRankedMatrix:
    """Tests for ranked_matrix."""

    def test_basic(self) -> None:
        """Returns ranked DataFrame with correct shape and values."""
        df = pd.DataFrame({"a": [3, 1, 2], "b": [10, 30, 20]})
        result = ranked_matrix(df)
        assert result.shape == df.shape
        assert list(result["a"]) == [3.0, 1.0, 2.0]
