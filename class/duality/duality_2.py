import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2,0.01)
f = x**3

l =  np.arange(0,4,0.01)
g = l*(1-(2/3)*np.sqrt(l/3))

plt.plot(x,f)
plt.plot(l,g)
plt.grid(True)
plt.show()