from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
print "The type of our fig object is: ", type(fig)

ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# A large sphere for the head.
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='magenta', alpha=0.5)
# A pair of ears.
ax.plot_surface(x*0.75+7, y*0.75, z*0.75+12, rstride=4, cstride=4, color='b', alpha=0.5)
ax.plot_surface(x*0.75-7, y*0.75, z*0.75+12, rstride=4, cstride=4, color='b', alpha=0.5)

# Add some eyes.



# Add a nose.


plt.xlabel('x'); plt.ylabel('y');


plt.title("Cartoon Character")
plt.show()



