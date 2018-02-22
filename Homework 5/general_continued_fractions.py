# In this file, we allow our continued fractions to have both numerator and denominators.
# These are called general continued fractions.
# See this reference for info on general continued fractions.  http://mathworld.wolfram.com/ContinuedFraction.html
# ALso see this reference: https://en.wikipedia.org/wiki/Continued_fraction.

# Notice the a coefficients start with index 0, but the b coefficients start with index 1.


"""
Also Review In-Class Quiz #1 , to see the form of a simple continued fraction.

"""

import math
from fractions import Fraction
# New import to  enable high precision calculations.as
from decimal import *
getcontext().prec = 100   # Work with 100 digits of precision!
from sympy.mpmath import mp
mp.dps = 100  # number of digits

class GeneralContinuedFraction(object):
    def __init__(self):
        self.a = [] # Empty list, first element is labelled a0.
        self.b = ["#"] # Empty list, first element is labelled b1. Use the pound symbol to block b0.

        self.p = []
        self.q = []

    def __str__(self):
        return  "a=" + str(self.a).replace(",", ";", 1) + "  b=" + str(self.b).replace('1', '#', 1)

    def __float__(self):
        self.setp()
        self.setq()
        result = self.p[-1]*1.0 / self.q[-1]
        return result

    def float100(self):
        getcontext().prec = 100  # We'll work with 100 digits of precision.
        self.setp()
        self.setq()
        result = Decimal(self.p[-1]) / self.q[-1]
        return result


    def setp(self):
        if len(self.a) == 0:
           self.p = []
           return

        self.p = self.a[::]  # Set its size the same as a's. Then overwrite the terms.
        if len(self.a) == 1:
           self.p[0] = self.a[0]
           return

        # Handle the general case here of at least 2 terms.
        self.p[0] = self.a[0]
        self.p[1] = self.b[1] + self.a[0] * self.a[1]
        for k in range(2, len(self.a)):
            self.p[k] = self.a[k] * self.p[k-1] + self.b[k] * self.p[k-2]

    def setq(self):
        if len(self.a) == 0:
           self.q = []
           return

        self.q = self.a[::]  # Set its size the same as a's. Then overwrite the terms.
        if len(self.a) == 1:
            self.q[0] = 1
            return

        # Handle the general case here of at least 2 terms.
        self.q[0] = 1
        self.q[1] = self.a[1]
        for k in range(2, len(self.a)):
            self.q[k] = self.a[k] * self.q[k-1] + self.b[k] * self.q[k-2]


# In contrast to the above static method, here we define an ordinary function.
# Greatest common divisor.
def gcd(m,n):
    if m == 0:
        return n
    if n == 0:
        return m

    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


if __name__ == "__main__":
    print "Example #1:"  # We set n = 10, and explore the first expansion for pi.
    print "The value of pi out to 100 digits is:", mp.pi   # print pi to a hundred places
    print "How fast does our continued fraction converge to this value?"

    print "We set n = 10, and explore the first expansion for pi. "

    # First construct
    myFrac = GeneralContinuedFraction()
    n = 10  # Go out to an and bn, then stop.
    myFrac.a = [3] + [6] *(n)  # A total of (n+1) terms.

    # We'll define b as the same size as a, keeping in mind, b0 is never used.
    myFrac.b = [1]*(n+1)  # But b0 is never used! It's just a place holder.
    # Now update the b's to be the squares of the odd numbers.
    for k in range(1, n+1):
        myFrac.b[k] = (2*k-1)**2


    print "Finite continued fraction #1 = ", myFrac
    print "This fraction has the float value:", GeneralContinuedFraction.float100(myFrac)


    print "Exact rational form: ", Fraction(myFrac.p[-1], myFrac.q[-1])
    print "The coefficients a, partial numerators p and partial quotients q are:"
    print "Coefficients a:       ", myFrac.a
    print "Coefficients b:       ", myFrac.b

    print "Partial numerators p: ", myFrac.p
    print "Partial quotients  q: ", myFrac.q


    print "\n\nNow let's go out to n = 100."
    myFrac = GeneralContinuedFraction()
    n = 100  # Go out to an and bn, then stop.
    myFrac.a = [3] + [6] *(n)  # A total of (n+1) terms.

    # We'll define b as the same size as a, keeping in mind, b0 is never used.
    myFrac.b = [1]*(n+1)  # But b0 is never used! It's just a place holder.
    # Now update the b's to be the squares of the odd numbers.
    for k in range(1, n+1):
        myFrac.b[k] = (2*k-1)**2
    print "This fraction has the float value:", GeneralContinuedFraction.float100(myFrac)

    print "\n\nNow let's go out to n = 1000."
    myFrac = GeneralContinuedFraction()
    n = 1000  # Go out to an and bn, then stop.
    myFrac.a = [3] + [6] *(n)  # A total of (n+1) terms.

    # We'll define b as the same size as a, keeping in mind, b0 is never used.
    myFrac.b = [1]*(n+1)  # But b0 is never used! It's just a place holder.
    # Now update the b's to be the squares of the odd numbers.
    for k in range(1, n+1):
        myFrac.b[k] = (2*k-1)**2
    print "This fraction has the float value:   ", GeneralContinuedFraction.float100(myFrac)
    print "The value of pi out to 100 digits is:", mp.pi   # print pi to a hundred places

    print "\n\nNow let's go out to n = 10000."
    myFrac = GeneralContinuedFraction()
    n = 10000  # Go out to an and bn, then stop.
    myFrac.a = [3] + [6] *(n)  # A total of (n+1) terms.

    # We'll define b as the same size as a, keeping in mind, b0 is never used.
    myFrac.b = [1]*(n+1)  # But b0 is never used! It's just a place holder.
    # Now update the b's to be the squares of the odd numbers.
    for k in range(1, n+1):
        myFrac.b[k] = (2*k-1)**2
    print "This fraction has the float value:   ", GeneralContinuedFraction.float100(myFrac)
    print "The value of pi out to 100 digits is:", mp.pi   # print pi to a hundred places

    myFrac = GeneralContinuedFraction()
    n = 10
    myFrac.a = [2, 3] + [4]*(n)
    myFrac.b = [4]
    for k in range(1, 2*n, 2):
        myFrac.b.append(k*k+2)
    print "This fraction has the float value:   ", GeneralContinuedFraction.float100(myFrac)
    print "The value of pi out to 10 digits is:", mp.pi

    myFrac = GeneralContinuedFraction()
    n = 100
    myFrac.a = [2, 3] + [4]*(n)
    myFrac.b = [4]
    for k in range(1, 2*n, 2):
        myFrac.b.append(k*k+2)
    print "This fraction has the float value:   ", GeneralContinuedFraction.float100(myFrac)
    print "The value of pi out to 10 digits is:", mp.pi

    myFrac = GeneralContinuedFraction()
    n = 1000
    myFrac.a = [2, 3] + [4]*(n)
    myFrac.b = [4]
    for k in range(1, 2*n, 2):
        myFrac.b.append(k*k+2)
    print "This fraction has the float value:   ", GeneralContinuedFraction.float100(myFrac)
    print "The value of pi out to 10 digits is:", mp.pi
