from pathlib import Path
import pandas as pd


# ── Path helpers ──────────────────────────────────────────────────────────────
def resolve_path(path):
    """Return an absolute, expanded Path object."""
    return Path(path).expanduser().resolve()


def ensure_parent_dir(path):
    """Create parent directories if they do not exist."""
    resolved = resolve_path(path)
    resolved.parent.mkdir(parents=True, exist_ok=True)


# ── pandas I/O ────────────────────────────────────────────────────────────────
def read_dataframe(path):
    """
    Read a DataFrame from a CSV file.
    """
    path = resolve_path(path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(path)

    raise ValueError(f"Unsupported DataFrame file type: {suffix}")


def write_dataframe(df, path, *, index=False):
    """
    Write a DataFrame to CSV.
    """
    path = resolve_path(path)
    ensure_parent_dir(path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        df.to_csv(path, index=index)
    else:
        raise ValueError(f"Unsupported DataFrame file type: {suffix}")
