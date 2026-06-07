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
    """Tests for geometric_mean.

    R equivalents verified via:
        geometricMean(c(1, 2, 8)) == exp((log(1)+log(2)+log(8))/3)
        geometricMean(c(0, 2, 8)) == exp((log(2)+log(8))/3)  # divides by 3 not 2
    """

    def test_basic(self) -> None:
        """Geometric mean of 2 and 8 is 4."""
        assert geometric_mean([2, 8]) == pytest.approx(4.0)

    def test_positive_sequence(self) -> None:
        """Geometric mean of 1..5 matches exp(mean(log(1:5))) in R."""
        expected = float(np.exp(np.mean(np.log([1, 2, 3, 4, 5]))))
        assert geometric_mean([1, 2, 3, 4, 5]) == pytest.approx(expected)

    def test_zero_excluded_divides_by_full_length(self) -> None:
        """Zeros excluded but full length is denominator (R semantics).

        R: geometricMean(c(0, 2, 8)) = exp(sum(log(c(2,8))) / 3)
        NOT exp(mean(log(c(2,8)))) which would divide by 2.
        """
        # R result: exp((log(2) + log(8)) / 3) = exp(log(16) / 3)
        expected = float(np.exp((np.log(2) + np.log(8)) / 3))
        result = geometric_mean([0, 2, 8])
        assert result == pytest.approx(expected)
        # Confirm it does NOT equal dividing by 2 (the buggy behavior)
        wrong = float(np.exp(np.mean(np.log([2, 8]))))
        assert result != pytest.approx(wrong)

    def test_zero_propagate(self) -> None:
        """Zero propagation returns 0 when zeros present."""
        assert geometric_mean([0, 1, 2], zero_propagate=True) == 0.0

    def test_negative_returns_nan(self) -> None:
        """Any negative element returns NaN (R semantics)."""
        result = geometric_mean([-1, 2, 4])
        assert np.isnan(result)

    def test_remove_na(self) -> None:
        """NaN values are removed by default."""
        result = geometric_mean([2.0, float("nan"), 8.0])
        assert result == pytest.approx(4.0)


class TestSem:
    """Tests for sem."""

    def test_basic(self) -> None:
        """Standard error of the mean matches expected value."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected = float(np.std(x, ddof=1) / np.sqrt(5))
        assert sem(x) == pytest.approx(expected)


class TestZscore:
    """Tests for zscore."""

    def test_vector(self) -> None:
        """Z-scored values have mean of zero."""
        result = zscore([1, 2, 3, 4, 5])
        assert result.mean() == pytest.approx(0.0, abs=1e-10)


class TestFoldChangeLogRatio:
    """Tests for fold_change_to_log_ratio and log_ratio_to_fold_change.

    R reference values from:
        foldChangeToLogRatio(c(-8, -4, -2, 1, 2, 4, 8))
        # [1] -3 -2 -1  0  1  2  3
        logRatioToFoldChange(seq(-3, 3, 1))
        # [1] -8 -4 -2  1  2  4  8
    """

    def test_positive_fc_to_lr(self) -> None:
        """Positive fold change: log2(4) == 2."""
        assert fold_change_to_log_ratio(4.0, base=2) == pytest.approx(2.0)

    def test_negative_fc_to_lr(self) -> None:
        """Negative fold change: -4 means 1/4x, so log2(1/4) == -2."""
        assert fold_change_to_log_ratio(-4.0, base=2) == pytest.approx(-2.0)

    def test_r_reference_vector(self) -> None:
        """Match R: foldChangeToLogRatio(c(-8,-4,-2,1,2,4,8)) == c(-3,-2,-1,0,1,2,3)."""
        fc = np.array([-8.0, -4.0, -2.0, 1.0, 2.0, 4.0, 8.0])
        expected = np.array([-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0])
        result = fold_change_to_log_ratio(fc, base=2)
        np.testing.assert_allclose(result, expected, atol=1e-10)

    def test_positive_lr_to_fc(self) -> None:
        """Positive log ratio: 2^2 == 4."""
        assert log_ratio_to_fold_change(2.0, base=2) == pytest.approx(4.0)

    def test_negative_lr_to_fc(self) -> None:
        """Negative log ratio: 2^-2 = 0.25 → -1/0.25 = -4 (R semantics)."""
        assert log_ratio_to_fold_change(-2.0, base=2) == pytest.approx(-4.0)

    def test_r_reference_vector_inverse(self) -> None:
        """Match R: logRatioToFoldChange(seq(-3,3,1)) == c(-8,-4,-2,1,2,4,8)."""
        lr = np.array([-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0])
        expected = np.array([-8.0, -4.0, -2.0, 1.0, 2.0, 4.0, 8.0])
        result = log_ratio_to_fold_change(lr, base=2)
        np.testing.assert_allclose(result, expected, atol=1e-10)

    def test_roundtrip(self) -> None:
        """Full roundtrip: fc → lr → fc recovers original value."""
        for fc in [-8.0, -4.0, -2.0, 1.0, 2.0, 4.0, 8.0]:
            lr = fold_change_to_log_ratio(fc, base=2)
            back = log_ratio_to_fold_change(lr, base=2)
            assert back == pytest.approx(fc, abs=1e-10), f"Roundtrip failed for fc={fc}"


class TestRankedMatrix:
    """Tests for ranked_matrix."""

    def test_basic_shape_and_values(self) -> None:
        """Returns ranked DataFrame with correct shape, index, and columns."""
        df = pd.DataFrame({"a": [3, 1, 2], "b": [10, 30, 20]})
        result = ranked_matrix(df)
        assert result.shape == df.shape
        assert list(result.columns) == list(df.columns)
        assert list(result.index) == list(df.index)
        assert list(result["a"]) == [3.0, 1.0, 2.0]
        assert list(result["b"]) == [1.0, 3.0, 2.0]

    def test_tied_ranks_averaged(self) -> None:
        """Tied values get averaged rank (method='average')."""
        df = pd.DataFrame({"x": [1, 1, 3]})
        result = ranked_matrix(df)
        # Ranks 1 and 2 are tied → both get 1.5
        assert list(result["x"]) == [1.5, 1.5, 3.0]

    def test_preserves_named_index(self) -> None:
        """Named index is preserved after ranking."""
        df = pd.DataFrame({"v": [5, 3, 1]}, index=["r1", "r2", "r3"])
        result = ranked_matrix(df)
        assert list(result.index) == ["r1", "r2", "r3"]
