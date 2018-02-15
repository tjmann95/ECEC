from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
step = 0.04
maxval = 1.0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# create supporting points in polar coordinates
r = np.linspace(0, 100, 101)
p = np.linspace(0, 2*np.pi, 101)
R, P = np.meshgrid(r, p)
# transform them to cartesian system
X, Y = R*np.cos(P), R*np.sin(P)

# Z = ((R**2 - 1)**2)
Z = R
# Alternative color maps you might explore.
# ax.plot_surface(X, Y, Z, rstride=4, cstride=4, cmap=cm.YlGnBu_r, alpha= 0.2)
# ax.plot_surface(X, Y, Z, rstride=4, cstride=4, cmap=cm.prism, alpha= 0.2)
# ax.plot_surface(X, Y, Z, rstride=4, cstride=4, cmap=cm.Pastel1, alpha=0.2)
# ax.plot_surface(X, Y, Z, rstride=4, cstride=4, cmap=cm.Accent, alpha=0.4)
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, cmap=cm.afmhot, alpha=0.4)

# ax.set_zlim3d(0, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cone of Pythagorean Triples')


# Now add a few Pythagorean triples manually.
ax.plot([5], [12], [13], 'bo')  # Primitive
ax.plot([10], [24], [25], 'ro') # Not primitive

ax.scatter(3, 4, 5, color='blue', s=30) # Primitive
ax.scatter(6, 8, 10, color='red', s=30) # Not primitive

# Now add all the missing triples onto the embedding cone.
# add code here (or above) including your methods to generate triples and primitive triples.

plt.show()
