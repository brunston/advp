import numpy as np
from scipy import stats
import math

data = np.loadtxt("coffee.csv",delimiter=",")
mass, vt_avg = data[:,1], data[:,5]
log_mass, log_vt_avg = [], []

for item in range(len(mass)):
    log_mass.append(math.log(mass[item]))
    log_vt_avg.append(math.log(vt_avg[item]))
poly = polyfit(log_vt_avg, log_mass, 1)
print(poly)
