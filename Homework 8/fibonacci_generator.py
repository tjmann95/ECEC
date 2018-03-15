# Here is a generator function to produce the first n Fibonacci numbers.
# Examples selected from this reference:    http://www.python-course.eu/generators.php


def fibonacci(n):
    """Fibonacci numbers generator, from start out to f(n)"""
    a, b, counter = 0, 1, 0  # pythonic tuple assignment
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

print "\nFibonacci sequence out to f(5)."
fib_gen = fibonacci(5)  # Construct a fresh generator

for x in fib_gen:  # Use a for loop to step through the generator.
    print x,

print "\n\nFibonacci sequence out to f(10)."
fib_gen = fibonacci(10)  # Construct a fresh generator, but now go out to f(10)
for value in fib_gen:
    print value,

# * * * Exercises start here. * * *
# Add code for part a below.
print "\n\nFibonacci sequence out to f(50)."

fib_gen = fibonacci(50)  # Construct a fresh generator, but now go out to f(50)
# Add your for loop here. Place a comma after the print statement to get them all on one line.
for value in fib_gen:
    print value,

# Add code for part b here.
fib_gen = fibonacci(100)  # Construct a fresh generator, but now go out to f(100)
print "\n\nFibonacci sequence out to f(100)."

# Fix and complete the while loop below.
k = 0
while True:
    try:
        if True: # <-- fix this stub.
            print "0 --> " + fib_gen.next()
    except StopIteration as e:
        break


# c. Define your tribonacci generator function here. t(0)=0, t(1) = 0, t(2) = 1
def tribonacci(n):
    """Tribonacci number generator, from start out to tribonacci(n)"""
    a, b, c, counter = 0, 0, 1, 0
    while True:
        if counter > n: return # Fix this stub.
        yield a
        a, b, c, counter = b, c, a + b + c, counter + 1

print "\nTribonacci sequence out to tribonacci(10)."
trib_gen = tribonacci(10)  # Construct a fresh generator
for x in trib_gen:
    print x,
