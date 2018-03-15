# A generator to find the square root of 2.

# DONE FOR YOU Ti ILLUSTRATE THE DECIMAL CLASS.

import math
from decimal import *
getcontext().prec = 100

print "1. A neverending generating to find the square root of 2."

def square_root():
    a0 = Decimal(1) # Start the series with 1.0 Make sure it is a float.
    while True:  # The iterator will be infinite!
        a1 = (a0 + 2/a0)/2
        yield a1
        a0 = a1

# Accelerates a series using the non-linear Aitken extrapolation.
def accelerate(my_generator):
    s0 = my_generator.next()
    s1 = my_generator.next()
    s2 = my_generator.next()
    while True:
        accelerated_term = s2 - ((s2 - s1)**2) / (s0 - 2 * s1 + s2)
        yield accelerated_term
        s0, s1, s2 = s1, s2, my_generator.next()

print "\na. Approximate root 2 using the slow method."
slow_gen = square_root()
for n in range(0, 6):
    print "%2d\t\t  --> " %n, slow_gen.next()
print "Root of 2 is: ", Decimal(2).sqrt()

print "\nb. Approximate root 2 using the fast method."
fast_gen = accelerate( square_root() )
for n in range(0, 6):
    print "%2d\t\t  --> " %n, fast_gen.next()
print "Root of 2 is: ", Decimal(2).sqrt()
