"""AcidBase -- Base functions for Acid Genomics packages."""

__version__ = "0.7.5"

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
    ram,
    random_string,
    shell,
)

# ── Version utilities ────────────────────────────────────────────────
from acidbase._version import (
    major_minor_version,
    major_version,
    sanitize_version,
)

__all__ = [
    # constants
    "barcode_pattern",
    "genome_metadata_names",
    "lane_pattern",
    "metadata_denylist",
    "metrics_cols",
    "update_message",
    # string
    "print_string",
    "str_extract",
    "str_extract_all",
    "str_match",
    "str_match_all",
    "str_pad",
    "str_remove_empty",
    "str_replace_na",
    "str_split",
    "truncate_string",
    # file
    "basename_sans_ext",
    "file_depth",
    "file_ext",
    "init_dir",
    "parent_dir",
    "parent_directory",
    "realpath",
    "tempdir2",
    "unlink2",
    # math
    "euclidean",
    "fold_change_to_log_ratio",
    "geometric_mean",
    "log_ratio_to_fold_change",
    "ranked_matrix",
    "sem",
    "zscore",
    # data
    "dupes",
    "headtail",
    "intersect_all",
    "intersection_matrix",
    "keep_only_atomic_cols",
    "match_all",
    "match_nested",
    "not_dupes",
    # path string
    "add_to_path_end",
    "add_to_path_start",
    "collapse_to_path_string",
    "remove_from_path",
    "split_path_string",
    "unique_path_string",
    # system
    "cpus",
    "git_current_branch",
    "git_default_branch",
    "ram",
    "random_string",
    "shell",
    # version
    "major_minor_version",
    "major_version",
    "sanitize_version",
    # compression
    "compress",
    "decompress",
    # download
    "download",
    "paste_url",
    # display
    "show_header",
    "show_slot_info",
    "simple_class",
    # cache
    "pkg_cache_dir",
]
