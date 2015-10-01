import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

#data = np.loadtxt("gravity.csv",delimiter=",")
data = np.loadtxt("gravity.txt")
p, t = data[:,0], data[:,1]
#print("p:", p)
#print("t:", t)
v = []
for position in range(len(p)):
    if position == 0:
        v.append(p[position]/0.025)
    if position > 0:
        v.append((p[position]-p[position-1])/0.025)
plt.plot(t,p, 'o', label="Position vs Time", markersize = 3)
plt.legend()
plt.show()
plt.plot(t,v,'o', label="Velocity (from avg velocity) vs Time", markersize = 3)
plt.legend()
plt.show()

poly = np.polyfit(t,p,2)
print("p(t), ax^2+bx+c = {0}x^2 + {1}x + {2}".format(poly[0], poly[1], poly[2]))
A = np.vstack([t, np.ones(len(t))]).T
vtm, vtc = np.linalg.lstsq(A, v)[0]

vderiv = []
for position in range(len(p)):
    vderiv.append(2*poly[0]*position + poly[1])
plt.plot(t,vderiv,'o', label="Velocity (from deriv) vs Time", markersize = 3)
plt.legend()
plt.show()
print("v(t) from v_avg, cm/s = {0}x + {1}".format(vtm, vtc))
print("a(t) from v_avg, cm/m^s = {0}".format(vtm))
print("a(t) from v_avg, m/m^s = {0}".format(vtm/100))
print("a(t) from p(T), m/m^s = 2*a/100 = {0}".format(2*poly[0]/100))
