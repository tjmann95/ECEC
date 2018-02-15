from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from fractions import gcd
step = 0.04
maxval = 1.0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def py_triple(cmax):
    # 1. Construct an empty list to hold all the triples as they are found.
    pythagorean_triple = []

    # 2. Use range with two arguments so n ranges over the values [1, 2, ..., 10].
    for n in range(1,11):
        # 3. Now impose conditions 1 and 2. Use range with three arguments so m ranges over the values:
        #   [n + 1, n + 3, n + 5, ... , 10]   if n odd, or[n+1, n+3, n+5, ... , 9] if n even.
        for m in range(n+1, 11, 2):
            # 4. Let k range over the values [1, 2, ... , 20] - because the smallest c is 5.
            for k in range(1, 21):
                # 5. Now impose condition 3. Use gcd to test if m and n are coprime.
                if gcd(m,n) == 1:  # Test if m and n are coprime.
                    # 6-7. Complete this pythonic assignment using Euclid's three formulas.
                    a, b, c = k*(m*m - n*n), k*(2*m*n), k*(m*m + n*n)
                    triple = [a, b, c]  # Store the triple as a list.
                    # 8. Sort the triple so that a <= b <= c.
                    triple.sort()
                    if c <= cmax:    # Only take triples in the target range.
                        # 9. Append the list [a, b, c] to the list of triples.
                        pythagorean_triple.append( triple )
    return pythagorean_triple


def primitive_py_triple(cmax):
    pythagorean_triple = []

    for n in range(1, 11):
        for m in range(n + 1, 11, 2):
            if gcd(m, n) == 1:
                a, b, c = m*m - n*n, 2*m*n, m*m + n*n
                triple = [a, b, c]
                triple.sort()
                if c <= cmax:
                    pythagorean_triple.append(triple)
    return pythagorean_triple


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
ax.plot_surface(Y, X, Z, rstride=4, cstride=4, cmap=cm.afmhot, alpha=0.4)

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
triples = py_triple(100)
prim_triples = primitive_py_triple(100)
for triple in triples:
    ax.plot([triple[0]], [triple[1]], [triple[2]], 'bo' if triple in prim_triples else 'ro')


plt.show()
