"""AcidBase -- Base functions for Acid Genomics packages."""

# ── Constants ────────────────────────────────────────────────────────
# ── Cache ────────────────────────────────────────────────────────────
from acidbase._cache import pkg_cache_dir

# ── Compression ──────────────────────────────────────────────────────
from acidbase._compress import compress, decompress
from acidbase._constants import (
    barcode_pattern,
    genome_metadata_names,
    lane_pattern,
    metadata_denylist,
    metrics_cols,
    update_message,
)

# ── Data manipulation ────────────────────────────────────────────────
from acidbase._data import (
    dupes,
    headtail,
    intersect_all,
    intersection_matrix,
    keep_only_atomic_cols,
    match_all,
    match_nested,
    not_dupes,
)

# ── Display helpers ──────────────────────────────────────────────────
from acidbase._display import show_header, show_slot_info, simple_class

# ── Download / URL ───────────────────────────────────────────────────
from acidbase._download import download, paste_url

# ── File utilities ───────────────────────────────────────────────────
from acidbase._file import (
    basename_sans_ext,
    file_depth,
    file_ext,
    init_dir,
    parent_dir,
    parent_directory,
    realpath,
    tempdir2,
    unlink2,
)

# ── Math / statistics ────────────────────────────────────────────────
from acidbase._math import (
    euclidean,
    fold_change_to_log_ratio,
    geometric_mean,
    log_ratio_to_fold_change,
    ranked_matrix,
    sem,
    zscore,
)

# ── PATH-string manipulation ─────────────────────────────────────────
from acidbase._path_string import (
    add_to_path_end,
    add_to_path_start,
    collapse_to_path_string,
    remove_from_path,
    split_path_string,
    unique_path_string,
)

# ── String utilities ─────────────────────────────────────────────────
from acidbase._string import (
    print_string,
    str_extract,
    str_extract_all,
    str_match,
    str_match_all,
    str_pad,
    str_remove_empty,
    str_replace_na,
    str_split,
    truncate_string,
)

# ── System utilities ─────────────────────────────────────────────────
from acidbase._system import (
    cpus,
    git_current_branch,
    git_default_branch,
    quietly,
    ram,
    random_string,
    shell,
)

# ── Version utilities ────────────────────────────────────────────────
from acidbase._version import (
    major_minor_version,
    major_version,
    minor_version,
    sanitize_version,
)

__all__ = [
    # path string
    "add_to_path_end",
    "add_to_path_start",
    # constants
    "barcode_pattern",
    # file
    "basename_sans_ext",
    "collapse_to_path_string",
    # compression
    "compress",
    # system
    "cpus",
    "decompress",
    # download
    "download",
    # data
    "dupes",
    # math
    "euclidean",
    "file_depth",
    "file_ext",
    "fold_change_to_log_ratio",
    "genome_metadata_names",
    "geometric_mean",
    "git_current_branch",
    "git_default_branch",
    "headtail",
    "init_dir",
    "intersect_all",
    "intersection_matrix",
    "keep_only_atomic_cols",
    "lane_pattern",
    "log_ratio_to_fold_change",
    # version
    "major_minor_version",
    "major_version",
    "match_all",
    "match_nested",
    "metadata_denylist",
    "metrics_cols",
    "minor_version",
    "not_dupes",
    "parent_dir",
    "parent_directory",
    "paste_url",
    # cache
    "pkg_cache_dir",
    # string
    "print_string",
    "quietly",
    "ram",
    "random_string",
    "ranked_matrix",
    "realpath",
    "remove_from_path",
    "sanitize_version",
    "sem",
    "shell",
    # display
    "show_header",
    "show_slot_info",
    "simple_class",
    "split_path_string",
    "str_extract",
    "str_extract_all",
    "str_match",
    "str_match_all",
    "str_pad",
    "str_remove_empty",
    "str_replace_na",
    "str_split",
    "tempdir2",
    "truncate_string",
    "unique_path_string",
    "unlink2",
    "update_message",
    "zscore",
]
