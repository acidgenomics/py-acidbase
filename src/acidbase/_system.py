"""System / shell utility functions."""

from __future__ import annotations

import multiprocessing
import secrets
import string
import subprocess

import psutil


def cpus(n: int = 1) -> int:
    """Return available CPU count, capped at *n* if requested.

    Parameters
    ----------
    n : int
        Maximum CPUs to return.  Use ``0`` to return all available.

    Returns
    -------
    int
    """
    available = multiprocessing.cpu_count()
    if n <= 0:
        return available
    return min(n, available)


def ram() -> float:
    """Return total system RAM in gibibytes (GiB).

    Requires the ``psutil`` package.

    Returns
    -------
    float

    Raises
    ------
    ImportError
        When ``psutil`` is not installed.
    """
    return psutil.virtual_memory().total / (1024**3)


def random_string(n: int = 8) -> str:
    """Generate a random alphanumeric string of length *n*.

    Parameters
    ----------
    n : int

    Returns
    -------
    str
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(n))


def shell(
    command: str,
    *,
    check: bool = True,
    capture_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    """Run a shell command.

    Parameters
    ----------
    command : str
    check : bool
        Raise on non-zero exit code (default ``True``).
    capture_output : bool

    Returns
    -------
    subprocess.CompletedProcess
    """
    return subprocess.run(
        command,
        shell=True,
        check=check,
        capture_output=capture_output,
        text=True,
    )


def git_current_branch() -> str | None:
    """Return the name of the current Git branch.

    Returns
    -------
    str or None
        ``None`` if not inside a Git repository.
    """
    try:
        result = shell("git rev-parse --abbrev-ref HEAD", check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def git_default_branch() -> str | None:
    """Return the default branch name of the Git repository.

    Checks ``refs/remotes/origin/HEAD`` first, then falls back to
    common names (``main``, ``master``).

    Returns
    -------
    str or None
    """
    try:
        result = shell(
            "git symbolic-ref refs/remotes/origin/HEAD",
            check=True,
        )
        return result.stdout.strip().split("/")[-1]
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    for name in ("main", "master"):
        try:
            shell(f"git show-ref --verify --quiet refs/heads/{name}")
            return name
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    return None
