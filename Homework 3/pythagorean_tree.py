import numpy as np

# Define the column vector (3, 4, 5).T which will be the root of our ternary tree.
# The T denotes transpose.
print "Explore the tree of primitive Pythagorean triples.\n".title()


x = np.matrix([[3, 4, 5]]).T # The T gives us the transpose.
print "The vector x containing the root of the pythagorean tree is:\n", x
# Note the "vector" is actually a 2x2 array.
print "\nThe root is level 0 in the tree."


print "\nNow find the three triples in level 1 of the tree. These are Ax, Bx and Cx."

# Define the matrix A using numpy.
A = np.matrix( ((1, -2, 2), (2, -1,  2), (2, -2,  3) ) )
print "\nThe matrix A is:\n", A

print "The product A*x is:\n", (A*x)
# Yes! It's in the first level of the tree.



# Define the matrix B using numpy, and display B*x.




# Define the matrix C using numpy, and display C*x.



# Complete all tasks stated in the PDF.