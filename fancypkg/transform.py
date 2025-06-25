import pandas as pd
import numpy as np
from typing import Optional


def filter_col_by_var(df: pd.DataFrame, thresh: float = 1e-4) -> pd.DataFrame:
    """Filter a pd DataFrame by columns that have variance higher than threshold."""
    variances = df.var()
    df_filtered = df.loc[:, variances > thresh]

    return df_filtered


def correlation_pairs(
    df: pd.DataFrame, *, method: str = "pearson", exclude: Optional[list[str]] = None
) -> pd.DataFrame:
    """Compute a correlation pairs table from a DataFrame

    Args:
        df: Input DataFrame.
        method: Correlation method. One of {'pearson', 'spearman', 'kendall'}.
        exclude: List of column names to exclude from the correlation.

    Returns:
        d.DataFrame with columns ['var1', 'var2', 'correlation', 'abs_correlation']
    """

    if exclude:
        df = df.drop(columns=exclude)
    # compute corr matrix
    corr = df.corr(method=method)
    # Apply mask to keep only upper triangle (no diagonal)
    mask = np.triu(np.ones(corr.shape), k=1).astype(bool)
    corr = corr.where(mask)
    # Reshape to tidy format
    corr = corr.stack().reset_index()
    corr.columns = ["var1", "var2", "correlation"]
    corr["abs_correlation"] = corr["correlation"].abs()
    corr = corr.sort_values("abs_correlation", ascending=False).reset_index(drop=True)

    return corr
