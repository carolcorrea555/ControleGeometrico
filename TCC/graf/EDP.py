import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def phi1(s, t):
    return t + s**2/2

def phi2(s, t):
    return t + s

def phi3(s, t):
    return s

dom = np.arange(-10,10,0.2)
ax.scatter(xs=[phi1(s, t) for s in dom for t in dom],
            ys=[phi2(s, t) for s in dom for t in dom],
            zs=[phi3(s, t) for s in dom for t in dom], s=2.5)
plt.xlabel("x")
plt.ylabel("y")
plt.show()