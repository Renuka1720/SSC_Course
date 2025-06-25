import fancypkg.transform as trf
import pandas as pd

if __name__ == "__main__":
    npop = pd.read_csv("data/npop.t", sep=r"\s+")
    npop = trf.filter_col_by_var(npop)
    test = trf.correlation_pairs(npop, exclude="time")
    print(test)
