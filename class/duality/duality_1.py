import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-1,4,0.1)
x2 = np.arange(-1,4,0.1)
x1,x2 = np.meshgrid(x1,x2)
f0 = x1**2 + x2**2

y1 = np.arange(-1,4,0.1)
y3 = np.arange(-1,20,0.1)
y1,y3 = np.meshgrid(y1,y3)
y2 = 1 - y1 + 0*y3

fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(x1,x2,f0)
ax.plot_surface(y1,y2,y3)
plt.show()

x = np.arange(-1,1,0.1)
f = x**2 + (1-x)**2

v = np.arange(-2,1,0.1)
g = -v**2/2 - v
plt.plot(x,f)
plt.plot(v,g)
plt.grid(True)
plt.show()