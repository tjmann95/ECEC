# Example showing how to create 2D plots using matplotlib.pyplot

# 1. Be able to import both of these.
import matplotlib.pyplot as plt
import numpy as np


# Create a new figure

fig = plt.figure('Ocean Waves')
# fill the ocean with a nice sea-green color.
X = [-1, 1, 1, -1]; Y = [0, 0, 10, 10];
plt.fill(X, Y, 'b', color = [0, 1, 1],     linewidth=3,     alpha = 0.5)


# 2. Generate 201 points from -1 to 1 for the x values.
x = np.linspace(-1, 1, 201)

# Some diagnostics. Get help on np.linspace by typing: >> help(np.linspace)
print("The number of x values is: " + str(len(x)))
print("The first x value is: " + str(x[0]))
print("The  last x value is: " + str(x[-1]))
print("The type of x is: " + str(type(x)))
print("Slicing example where x is reversed: " + str(x[::-1]))
print("Slicing example showing every 10th element " + str(x[::10]))



# 3. Generate the first wave.
y = np.sin(4*np.pi*x)  # sinusoidal wave

                        #  Red Green Blue            # 0 = transparent, 1 = opaque
plt.plot(x, y, 'r', color = [0, 0, 1],     linewidth=3,     alpha = 1)

# Add a for loop to add 20 more waves, each 0.5 units higher and shifted to the right by 0.02
dx = 0.02; dy = 0.5
for n in range(1, 21):
    next_color = [0, n / 20, 1 - n / 20]
    print(n)
    next_alpha = next_color[2]
    plt.plot(x + 0.02*n, y + 0.5*n, color = next_color, linewidth=3, alpha=next_alpha       )


plt.grid(True)  # Add a grid.
plt.axis([-1, 1, 0, 10])  # Set the viewport.
plt.show()  # Finally show the resulting plot.




# Uncomment the line below for help
# help(np.linspace)