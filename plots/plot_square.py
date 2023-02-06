"""
Basic program to plot 2d surfaces using pyplot
"""

import matplotlib.pyplot as plt
from matplotlib.axis import Axis
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


plt.style.use('_mpl-gallery')

# Make data
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
Z = 2*x + 3*y + 1

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, Z, vmin=Z.min() * 2, cmap=cm.Blues)
"""
ax.set(xticklabels=[range(-5,5)],
       yticklabels=[range(-5,5)],
       zticklabels=[0])
"""
plt.xlabel('x')
plt.ylabel('y')

xz,yz,zz = np.zeros((3,3))
xaxis,yaxis,zaxis = np.eye(3) * np.max(np.abs(x))
mxaxis,myaxis,mzaxis = -np.eye(3) * np.max(np.abs(x))
ax.quiver(xz,yz,zz,xaxis,yaxis,zaxis,color='black',arrow_length_ratio=0.1)
ax.quiver(xz,yz,zz,mxaxis,myaxis,mzaxis,color='black',arrow_length_ratio=0.1) 

ax.xaxis.zoom(3)

plt.show()
