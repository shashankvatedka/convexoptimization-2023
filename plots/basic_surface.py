"""
Basic program to plot 2d surfaces using pyplot
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.style.use('_mpl-gallery')

# Make data
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
R = np.sqrt(x**2 + y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
plt.xlabel('x')
plt.ylabel('y')

plt.show()
