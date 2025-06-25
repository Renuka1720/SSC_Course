import transform as trf
from InputOutput import resolve_path, ensure_parent_dir
from InputOutput import read_dataframe, write_dataframe


if __name__ == "__main__":
    path = resolve_path("data/npop.t")
    npop = read_dataframe(path)
    # filter npop and compute correlation pairs
    npop_filtered = trf.filter_col_by_var(npop)
    cor_pairs = trf.correlation_pairs(npop_filtered, exclude="time")
    # write results into files
    ensure_parent_dir("results")
    write_dataframe(cor_pairs, "results/correlation_pairs.csv")
