import numpy as np
from scipy import stats
data = np.loadtxt("rockets.txt")
col, cold = data[:], []
for item in range(len(col)):
	cold.append(np.radians(col[item]))
print("""
mean: {0}
stdev: {1}
error of mean: {2}
	""".format(np.mean(cold),stats.tstd(cold),stats.sem(cold)))