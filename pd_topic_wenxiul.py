
# Wenxiu Liao
# wenxiul@umich.edu

# ### sort_values()
# * The Series.sort_values() method is used to sort a Series by its values.
# * The DataFrame.sort_values() method is used to sort a DataFrame by its column or row values.
#     - The optional by parameter to DataFrame.sort_values() may used to specify one or more columns to use to determine the sorted order.

import numpy as np
import pandas as pd
from os.path import exists
from scipy import stats
from scipy import stats as st
from warnings import warn
from scipy.stats import norm, binom, beta
import matplotlib.pyplot as plt

df1 = pd.DataFrame(
    {"A": [2, 1, 1, 1], "B": [1, 3, 2, 4], "C": [5, 4, 3, 2]}
)
df1.sort_values(by="C")

# The by parameter can take a list of column names, e.g.:

df1.sort_values(by=["A", "B"])

# You can specify the treatment of NA values using the na_position argument:

s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"],
    dtype="string"
)
s.sort_values(na_position="first")

