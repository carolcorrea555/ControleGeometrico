import matplotlib.pyplot as plt
import numpy as np

def a(t):
    if t <= 2:
        return 0.5
    elif t <= 5:
        return -0.2
    else:
        return 0.3

def v(t):
    if t <= 2:
        return 0.5*t
    elif t <= 5:
        return v(2) - 0.2*(t-2)
    else:
        return v(5) + 0.3 * (t-5)

def x(t):
    if t <= 2:
        return 0.5*t*t
    elif t <= 5:
        return x(2) + v(2)*(t-2) - 0.2*(t-2)*(t-2)
    else:
        return x(5) + v(5)*(t-5) + 0.3 * (t-5) * (t-5)

dom = np.arange(0,10,0.01)
plt.plot(dom, [x(t) for t in dom])
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("piecewisecte_sol.png")