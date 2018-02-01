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
B = np.matrix(((1, 2, 2), (2, 1, 2), (2, 2, 3)))

print "The product B*x is:\n", (B*x)
# Define the matrix C using numpy, and display C*x.
C = np.matrix(((-1, 2, 2), (-2, 1, 2), (-2, 2, 3)))

print "The product B*x is:\n", (C*x)
# Complete all tasks stated in the PDF.
level_1 = [A*x, B*x, C*x]
level_2 = []
for triple in level_1:
    level_2.append(A * triple)
    level_2.append(B * triple)
    level_2.append(C * triple)
print "Level 2: "
print level_2

print "Last in level 3: "
print C*level_2[-1]

def ternary(n):
    e = n//3
    q = n%3
    if n == 0:
        return "0"
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)

def thingy(n):
    result = x
    for digit in reversed(ternary(n)):
        if digit == "0":
            result = A * result
        elif digit == "1":
            result = B * result
        elif digit == "2":
            result = C * result
    return result

thingy(15)