# acidbase

Base functions for [Acid Genomics](https://acidgenomics.com) packages.

A grab-bag of small, dependency-light utilities shared across the Acid Genomics
Python packages: math/statistics, string handling, file and PATH-string
manipulation, system/shell helpers, and version parsing.

## Installation

### uv method

This package is hosted on [PyPI](https://pypi.org/project/acidgenomics-acidbase/)
as `acidgenomics-acidbase`. The import name is unchanged: `acidbase`.
We recommend using [uv](https://docs.astral.sh/uv/) to install.

```sh
uv add acidgenomics-acidbase
```

Or with [pip](https://pip.pypa.io/):

```sh
pip install acidgenomics-acidbase
```

### Conda method

Configure [Conda](https://docs.conda.io/) to use the
[Bioconda](https://bioconda.github.io/) channels.

```sh
# Don't install recipe into base environment.
name='acidbase'
conda create --name="$name" "$name"
conda activate "$name"
python -c 'import acidbase'
```

## Math and statistics

```pycon
>>> from acidbase import euclidean, geometric_mean, headtail
>>> euclidean([0, 0], [3, 4])
5.0
>>> geometric_mean([1, 2, 4, 8])
2.82842712474619
```

`headtail` prints and returns the first and last *n* elements of a list, array, or
DataFrame:

```pycon
>>> result = headtail(list(range(10)), n=2)
[0, 1, 8, 9]
>>> result
[0, 1, 8, 9]
```

Also included: `fold_change_to_log_ratio`/`log_ratio_to_fold_change`, `zscore`,
`sem`, `ranked_matrix`, `intersect_all`, and `intersection_matrix`.

## Data manipulation

```pycon
>>> from acidbase import dupes, not_dupes
>>> dupes(["a", "b", "a", "c", "b"])
['a', 'b']
>>> not_dupes(["a", "b", "a", "c", "b"])
['c']
```

`match_all` returns every matching index instead of just the first (unlike Python's
built-in lookup semantics); `match_nested` recursively searches a nested dict/list
structure; `keep_only_atomic_cols` drops list/dict-valued DataFrame columns.

## String utilities

```pycon
>>> from acidbase import str_pad, truncate_string
>>> str_pad("5", 3, pad="0")
'005'
>>> truncate_string("a very long string indeed", 10)
'a very lon...'
```

The `str_extract`/`str_extract_all`/`str_match`/`str_match_all`/`str_split` family
wraps `re` with a consistent argument order (subject string first, pattern second).

## File and PATH-string utilities

`basename_sans_ext`/`file_ext` understand compound bioinformatics extensions like
`.fastq.gz`; `compress`/`decompress` handle gz/bz2/xz/zip; `init_dir`, `realpath`,
`tempdir2`, and `unlink2` round out common filesystem operations.

The path-string family (`split_path_string`, `add_to_path_start`,
`add_to_path_end`, `remove_from_path`, `unique_path_string`,
`collapse_to_path_string`) operates on colon-separated strings like `$PATH`.

## System, version, and download utilities

`shell` runs a command and returns a `subprocess.CompletedProcess`;
`git_current_branch`/`git_default_branch` inspect the current repo; `cpus`/`ram`
report system resources; `quietly` is a context manager that suppresses stdout,
stderr, and warnings within a block.

`major_version`/`major_minor_version`/`sanitize_version` parse and normalize PEP
440 version strings. `download` fetches a URL to disk; `paste_url` joins URL path
segments.

```{toctree}
:maxdepth: 1
:caption: Contents
:hidden:

reference/index
changelog
```
