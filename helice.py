import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rc

rc("text", usetex = True)

theta = np.linspace(0, 6*np.pi, 1000)
x = np.cos(theta)
y = np.sin(theta)
z = theta

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.plot(x, y, z, label = "Simplemente conexo")
ax.plot(x, y, 0, label = r"$\pi_1(S^1)\cong \mathbb{Z}$")
ax.set_zlabel("$\leftarrow$", fontsize = 50)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.legend()
plt.savefig("helice.png")
