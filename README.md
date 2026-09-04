# py-acidbase

[![Install with Bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg)](https://bioconda.github.io/recipes/acidbase/README.html) ![Lifecycle: maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg)

Base functions for [Acid Genomics](https://acidgenomics.com) packages.

## Installation

### [uv][] method

This is a [Python][] package hosted on [PyPI][] as `acidgenomics-acidbase`.
The import name is unchanged: `acidbase`.
We recommend using [uv][] to install.

```sh
uv add acidgenomics-acidbase
```

Or with [pip][]:

```sh
pip install acidgenomics-acidbase
```

### [Conda][] method

Configure [Conda][] to use the [Bioconda][] channels.

```sh
# Don't install recipe into base environment.
name='acidbase'
conda create --name="$name" "$name"
conda activate "$name"
python -c 'import acidbase'
```

## Links

- [GitHub](https://github.com/acidgenomics/py-acidbase)


## License

Apache-2.0 — Copyright 2026 Acid Genomics LLC — see [LICENSE](LICENSE).

[bioconda]: https://bioconda.github.io/
[conda]: https://docs.conda.io/
[pip]: https://pip.pypa.io/
[pypi]: https://pypi.org/project/acidgenomics-acidbase/
[python]: https://www.python.org/
[uv]: https://docs.astral.sh/uv/
