"""Tests for acidbase._constants."""

import re

from acidbase import (
    barcode_pattern,
    genome_metadata_names,
    lane_pattern,
    metadata_denylist,
    metrics_cols,
    update_message,
)


class TestBarcodePattern:
    """Tests for barcode_pattern."""

    def test_matches(self) -> None:
        """Matches valid barcode sequence."""
        assert re.search(barcode_pattern, "ACGT") is not None

    def test_no_match(self) -> None:
        """Does not match non-barcode string."""
        assert re.search(barcode_pattern, "1234") is None


class TestLanePattern:
    """Tests for lane_pattern."""

    def test_matches(self) -> None:
        """Matches valid lane identifier."""
        assert re.search(lane_pattern, "L001") is not None


class TestGenomeMetadataNames:
    """Tests for genome_metadata_names."""

    def test_is_tuple(self) -> None:
        """Constant is a tuple."""
        assert isinstance(genome_metadata_names, tuple)

    def test_contains(self) -> None:
        """Contains expected organism key."""
        assert "organism" in genome_metadata_names


class TestMetadataDenylist:
    """Tests for metadata_denylist."""

    def test_is_tuple(self) -> None:
        """Constant is a tuple."""
        assert isinstance(metadata_denylist, tuple)


class TestMetricsCols:
    """Tests for metrics_cols."""

    def test_contains(self) -> None:
        """Contains expected nCount column."""
        assert "nCount" in metrics_cols


class TestUpdateMessage:
    """Tests for update_message."""

    def test_is_str(self) -> None:
        """Constant is a string."""
        assert isinstance(update_message, str)
