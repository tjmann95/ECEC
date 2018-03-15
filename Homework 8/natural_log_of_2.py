# Evaluate the natural log of 2 using a slowly converging series and also after applying Aitken acceleration.


import math
from decimal import *
getcontext().prec = 100

print "1. A neverending generator function to find the natural log of 2."

def natural_log_of_2():
    n = Decimal(1)
    next_term = Decimal(1) # Start the series with 1.0 with lots of precision.
    sign = Decimal(1)
    while True:  # The iterator will be infinite!
        yield next_term
        # Update all the variables here.

# We can just copy/paste the Aitken extrapolation code.
# Accelerates a series using the non-linear Aitken extrapolation.
def accelerate(my_generator):
    s0 = my_generator.next()
    s1 = my_generator.next()
    s2 = my_generator.next()
    while True:
        accelerated_term = s2 - ((s2 - s1)**2) / (s0 - 2 * s1 + s2)
        yield accelerated_term
        s0, s1, s2 = s1, s2, my_generator.next()

print "\na. Approximate the natural log of 2 using the slow method."
slow_gen = natural_log_of_2()

# Add code here.

print "Natural log of 2: ", Decimal(2).ln()

# Add code here to accelerate the conversion.


 