import numpy as np
from scipy import stats
data = np.loadtxt("rockets.txt")
col = data[:]
print("mean: ", np.mean(col))
print("stdev: ", stats.tstd(col))
print("error of mean: ", stats.sem(col))