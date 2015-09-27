import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.loadtxt("gravity.txt")
p, t = data[:,0], data[:,1]
print("p:", p)
print("t:", t)

plt.plot(t,p, 'o', label="Position vs Time", markersize = 3)
plt.legend()
plt.show()

A = np.vstack([t, np.ones(len(t))]).T
ptm, ptc = np.linalg.lstsq(A, p)[0]
print("y = {0}x + {1}".format(ptm, ptc))
