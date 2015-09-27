import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
figure = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-5,5,0.5)

y + z = 2
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
ax.plot_surface