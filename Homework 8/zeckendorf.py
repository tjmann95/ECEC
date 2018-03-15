# This code borrowed from Rosetta Code
# https://rosettacode.org/wiki/Zeckendorf_number_representation#Python

nmax = 20  # Find z(n) out to this maximum value.

# Method to return the Zeckendorf representation of a positive integer.
# It's the greedy algorithm.


def zeckendorf(n):
    if n == 0: return [0]
    fib = [2, 1]
    while fib[0] < n: fib[0:0] = [sum(fib[:2])] # Extends the list of fibonacci numbers as far as needed.
    dig = [] # The list of Zeckendorf digits - each is a 0 or a 1.
    for f in fib:
        if f <= n:  # The fibonacci number f is part of the Zeckendorf sum.
            dig, n = dig + [1], n - f  # pythonic assignment, concatenate [1] to the list of digits, reduce the number n by f
        else:
            dig += [0]   # concatenate [0] to the list of digits
    return dig if dig[0] else dig[1:]  # Ignore any leading zero.


for i in range(nmax + 1):
    print('%3i: %8s' % (i, ''.join(str(d) for d in zeckendorf(i))))

