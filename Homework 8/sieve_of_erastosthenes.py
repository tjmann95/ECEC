# A generator version of the Sieve of Eratosthenes for finding primes.

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
    print "EXAMPLES"
    print "\n1. Exclude all even numbers in the range from 1 to 20 using exclude_multiples()."

    gen = exclude_multiples(2, range(1,21))
    for value in gen: print value,

    # ii.  Let's exclude all multiples of 3 from 1 to 30.
    print "\n\n2. Exclude all multiples of 3 in the range from 1 to 30."
    gen = exclude_multiples(3, range(1,31))
    for value in gen: print value,

    print "\n\n3. Find the first ten primes using sieve()."
    ints = iter(range(2, 101))  # Note the use of the iter() method. This means we can use next() with this iterator.

    get_primes = sieve(ints)
    for n in range(0,10):
        print get_primes.next(),

    print "\n\n4. Try to find the first ten primes when the input range is not large enough."
    ints = iter(range(2, 21))  # Ack! Does not contain ten primes.

    get_primes = sieve(ints)
    for n in range(0,10):
        try:
            print get_primes.next(),
        except StopIteration as e:
            print "Sorry, you ran out of numbers before all the primes could be generated. "

    print "\n\n5. Find the first 100 primes featuring xrange. Numbers generated as needed."
    print "Beware that xrange will disappear in python 3, where it is just called range."

    ints = iter(xrange(2, 50000000))  # Note the use of the iter() method. This means we can use next() with this iterator.

    get_primes = sieve(ints)
    for n in range(0,100):
        print get_primes.next(),


    print "\n\n6. Find the first 50 primes featuring the endless integer generator intsfrom(2). "
    ints = intsfrom(2)  # Endless integers starting at 2
    get_primes = sieve(ints)
    for n in range(0,50):
        print get_primes.next(),

"""
    for i in firstn(sieve(intsfrom(2)), 400):
        print i
"""
