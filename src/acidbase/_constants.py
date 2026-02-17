"""Constants ported from AcidBase R package."""

import re

barcode_pattern: str = r"[ACGT]+"
"""Barcode pattern (e.g. multiplexed samples)."""

lane_pattern: str = r"L[0-9]+"
"""Column pattern matching expected lane identifiers."""

genome_metadata_names: tuple[str, ...] = (
    "genbankId",
    "genomeBuild",
    "id",
    "organism",
    "provider",
    "release",
    "taxonomyId",
)
"""Column names used in genome metadata tables."""

metadata_denylist: tuple[str, ...] = (
    "^description$",
    "^interestingGroups$",
    "^revcomp$",
    "^sampleId$",
    "^sampleName$",
)
"""Column name patterns that should be excluded from metadata."""

metrics_cols: tuple[str, ...] = (
    "nCount",
    "nFeature",
    "nCoding",
    "nMito",
    "log10FeaturesPerCount",
    "mitoRatio",
)
"""Column names commonly used for quality control metrics."""

update_message: str = "Run 'updateObject()' to update."
"""Standard message for outdated objects (kept for compatibility)."""

_ext_pattern: re.Pattern[str] = re.compile(
    r"(?:\."
    r"(?:7z|bam|bai|bed|counts|csv|gtf|gff|gff3|"
    r"hdf5|h5|h5ad|loom|mtx|rds|rda|tsv|txt|"
    r"fasta|fa|fastq|fq|sam|vcf|wiggle|xls|xlsx)"
    r")+$",
    re.IGNORECASE,
)
"""Pattern matching common bioinformatics/genomics file extensions."""

_compress_ext_pattern: re.Pattern[str] = re.compile(r"\.(?:bz2|gz|xz|zip)$", re.IGNORECASE)
"""Pattern matching compression extensions."""
