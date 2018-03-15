# Ocassionally you may want a return in your  function that produces the generator.

# The body of a generator function should not contain a return statement of the form 'return expr'.
# However, a simple 'return' is allowed.


def f(n):
    if n < 3: yield 1
    else: return
    yield 2

gen1 = f(20)

print gen1.next()



