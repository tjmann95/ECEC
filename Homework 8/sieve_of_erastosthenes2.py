# A generator version of the Sieve of Eratosthenes for finding primes.
# Uses these three generator functions.

def intsfrom(i):  # An endless supply of integers starting at i.
    while True:
        yield i
        i = i + 1


def exclude_multiples(n, ints):
    for i in ints:
        if (i % n): yield i  # Only 0 gives False.  All non-zero values equal True.


def sieve(ints):
    while True:
        prime = ints.next()
        yield prime
        ints = exclude_multiples(prime, ints)


if __name__ == '__main__':

    print "\na. The first 20 primes are: "

    # Add your code here.

    print "\nb. The first 20 primes after 1000 are: "
    # Add your code here.
    ints = intsfrom(2)
    get_primes = sieve(ints)




    print "\n\nc. Goal: Find how many primes there are between one thousand and two thousand."
    # Add your code below.
    ints = intsfrom(2)
    get_primes = sieve(ints)

    # Toss out all the primes less than 1000 here.

    # Now count the number of primes between one and two thousand.
    count = 0


