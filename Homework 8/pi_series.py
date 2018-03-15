# A generator to find pi.
import math
print "1. A neverending series to find pi. But it converges really, really slowly."

def pi_series():
    sum = 0
    i = 1.0  # Guarantees division will use floats.
    j = 1
    while True:  # The iterator will be infinite!
        sum += j / i
        yield 4 * sum
        i += 2;  # The odd divisors
        j *= -1  # The alternating signs


print "Estimate pi by summing Leibnitz's series (*4) out to n = 20."
slow_gen = pi_series()
for n in range(0,21):
    print "Out to n = %2d --> " % n, slow_gen.next()


print "Ack! Very slow convergence."

print "\n2. That sure is a slow convergence! Let's apply the non-linear Aitken extrapolation to accelerate the convergence!"

# Accelerates a series using the non-linear Aitken extrapolation.
def accelerate(my_generator):
    s0 = my_generator.next()
    s1 = my_generator.next()
    s2 = my_generator.next()
    while True:
        accelerated_term = s2 - ((s2 - s1)**2) / (s0 - 2 * s1 + s2)
        yield accelerated_term
        s0, s1, s2 = s1, s2, my_generator.next()


fast_gen = accelerate( pi_series())  # The accelerated generator.
for n in range(0,21):
    print "Out to n = %2d --> " % n, fast_gen.next()
print "Awesome! The convergence is much faster."


print "\n3. Let's compare the slow and fast series going out to n = 100. That's 101 terms."

print "a. Estimate pi by summing Leibnitz's slow series out to n = 100."
slow_gen = pi_series()
for n in range(0,101):
    result = slow_gen.next()
print "Out to n = 100 --> ",  result


print "b. Estimate pi by summing the accelerated series out to n = 100."
fast_gen = accelerate( pi_series() )  # A fresh accelerated generator.
for n in range(0,101):
    result = fast_gen.next()
print "Out to n = 100 --> ",  result
print "Actual value of pi is: ", math.pi

