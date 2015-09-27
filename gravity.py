import numpy as np
from scipy import stats
data = np.loadtxt("gravity.txt")
x, t = data[1:,0], data[1:,1]

print("""
mean: {0}
stdev: {1}
error of mean: {2}
	""".format(np.mean(cold),stats.tstd(cold),stats.sem(cold)))