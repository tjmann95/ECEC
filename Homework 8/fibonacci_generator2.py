# Example that produces an *endless* iterator.
# Make sure you provide a termination criterion !!

def fibonacci():
    """Endless Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()  # A fresh endless iterator.

# Take great care to assure a termination criterion has been provided,
# or you will lock your computer in an infinite task.

print "1. The Fibonacci numbers out to f(10) using an endless iterator with termination criterion."
counter = 0
for x in f:
    print x,
    counter += 1
    if (counter > 10): break  # <-- Termination criterion




# This next example can be called a generator of generators.
print "\n2. The Fibonacci numbers out to f(10) using a generator of generators."

def firstn(g, n):
    for i in range(n+1):
        yield g.next()

print list( firstn(fibonacci(), 10) )


# a. Add code here to produce an endless tribonacci number function generator.
# Provide a termination criterion and print out the tribonacci numbers out to t(100).
# Use the convention: t(0)=0, t(1) = 0, t(2) = 1

# DONE FOR YOU. Free! T
def tribonacci():
    """Endless Tribonacci numbers generator"""
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c

print "\na. The tribonacci numbers out to tribonacci(10) using a generator of generators."
print list( firstn(tribonacci(), 10) )


# b. Write an endless tetranacci number function generator. Construct an endless iterator.
# Then print out the numbers to tetra(100).
# Use the convention: t(0)=0, t(1) = 0, t(2) = 0, t(3)=1

def tetranacci():
    """Endless Tetranacci number generator"""
    a, b, c, d = 0, 0, 0, 1  # Initialize a=0, b=0, c=0, and d=1 here.
    while True:
        yield a
        a, b, c, d = b, c, d, a + b + c

print "\nb. The tetranacci numbers out to tetranacci(10) using a generator of generators."
print list( firstn(tetranacci(), 10) )

