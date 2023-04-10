import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-1,1,0.01)
x2 = np.arange(-1,1,0.01)
x1,x2 = np.meshgrid(x1,x2)

f = 2*x1**2 - x2**2 + x1 + 2*x2/3
f[(x1**2+x2**2)>1] = np.inf

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(x1,x2,f)
plt.show()

print("Minimum value: ",np.min(f))


# Plot the dual function
l = np.arange(1.001, 10, 0.01)
g = -0.25/(2+l) - 1/(9*(l-1)) - l

plt.plot(l,g)
plt.xlabel('$\lambda$')
plt.ylabel('Lagrange Dual function')
plt.grid(True)
plt.show()

print('Maximum value of the dual: ',np.max(g))