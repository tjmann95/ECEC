
import math
from fractions import Fraction


class FCFrac(object):
    def __init__(self):
        self.a = [] # Empty list
        self.p = []
        self.q = []

    def __str__(self):
        return  str(self.a).replace(",", ";", 1) # Replace just the first comma with a semi-colon.

    def __float__(self):
        self.setp()
        self.setq()
        result = self.p[-1]*1.0/self.q[-1]
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
        self.p[1] = 1 + self.a[0] * self.a[1]
        for k in range(2, len(self.a)):
            self.p[k] = self.a[k] * self.p[k-1] + self.p[k-2]

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
            self.q[k] = self.a[k] * self.q[k-1] + self.q[k-2]

    @staticmethod
    def findFCFrac(m, n):  # Here, m and n are integers representing the rational number m/n.
        result = FCFrac()  # Start with an empty continued fraction.
        common = gcd(m,n)
        m, n = m/common, n/common   # Remove the greatest common divisor, so the algorithm stops with n = 1.
        firstTerm = m/n
        result.a.append(firstTerm)
        while n !=1:        # <-- Stop when n = 1.
            m, n = n, m % n  # Pythonic tuple assignment.
            nextTerm = m/n
            result.a.append(nextTerm)
        return result


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





# Show 2; 1, 3, 4] =  47/17
if __name__ == "__main__":
    print "Example #1:"
    print "We wish to show the continued fraction [2; 1, 3, 4] =  47/17"

    # First construct
    myFrac = FCFrac()
    myFrac.a = [2, 1, 3, 4]
    print "Finite continued fraction #1 = ", myFrac


    print "This fraction has the float value:", float(myFrac)
    print "Exact rational form: ", Fraction(myFrac.p[-1], myFrac.q[-1])
    print "The coefficients a, partial numerators p and partial quotients q are:"
    print "Coefficients a:       ", myFrac.a
    print "Partial numerators p: ", myFrac.p
    print "Partial quotients  q: ", myFrac.q
