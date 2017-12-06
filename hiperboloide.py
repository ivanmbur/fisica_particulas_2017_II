import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rc

rc("text", usetex = True)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
x = np.linspace(-10, 10)
y = x
m = 3
X, Y = np.meshgrid(x, y)
z = np.sqrt(m*m + X*X + Y*Y)
ax.plot_surface(X, Y, z)
ax.set_xlabel(r"$\vec{p}$", fontsize = 30)
ax.set_zlabel("$p^0$", fontsize = 30)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.savefig("hiberboloide.png")
