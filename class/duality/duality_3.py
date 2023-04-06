import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2,0.01)
l = np.arange(0,2,0.1)
x,l = np.meshgrid(x,l)
f = x**2 + l*(-x+1)

fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(x,l,f)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()