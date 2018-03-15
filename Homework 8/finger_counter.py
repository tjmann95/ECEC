import time


print "\nExample: A very simple demo for generators. Counting fingers!\n"

print "Step 1: Define your generator function using the 'def' keyword. Ours is named: finger_counter()"
def finger_counter():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print "\nStep 2: Construct a generator, say  'f', by calling the generator function: f = finger_counter()"
print "A generator function is simply a function which returns a generator."

f = finger_counter()
print "Indeed, the generator function produces an object 'f' which has the type: ", type(f)


print "\nStep 3: Walk through the generator by invoking the next() command, one step at a time."
print "It stops at each yield, but remembers exactly where it left off for when it is called again. "
print "OK, let's count the fingers on one hand by calling next() five times."
print "Check the code to see the two alternative syntaxes for calling next()."

print f.next()  # Yields the 1, and stops.
print f.next()  # Yields the 2, and stops.
print f.next()  # Yields the 3, and stops.
# You can use this alternative syntax instead.
print next(f)   # Yields the 4, and stops.
print next(f)   # Yields the 5, and stops.

# If you uncomment the next line, you will trigger a StopIteration exception. No more fingers!
# next(f)

print "\n4. StopIteration: If you attempt to go past the end of the generator, a StopIteration exception is thrown."
print "Let's try calling it for a sixth time, even though we only have five fingers. (Unless you have polydactlyly.)"

try:
    print f.next()  # A sixth call! But we only have five fingers.
except Exception as e:
    print "Sorry, you went too far and triggered this exception:", repr(e)



print "\n5. Let's start over by constructing a fresh generator: f = finger_counter()"
f = finger_counter()  # A fresh generator with the pointer at the beginning.
print "You can also use a for loop to step through the generator f >>> for value in f: print value"
print "The loop header 'for value in f', walks through all the results yielded by the generator. " \
      "\nThere is no need to call next()."

print "OK, let's count the fingers on one hand again, but using the convenience of a for loop.\n" \
      "We'll also add timing to count one finger per second."
for value in f:
    print value; time.sleep(1)



print "\n6. You can also step through a generator using a while loop."
print "But then, you must explicitly catch the StopIteration exception when you purposely 'go over the cliff'."

# We'll start over with a fresh generator.
f = finger_counter()  # Fresh generator with the pointer just before the first finger.

while True:
    try:
        print f.next(); time.sleep(1)
    except StopIteration as e:
        print "There are no values left.", repr(e)
        break

# EXERCISES START HERE.  ADD CODE BELOW.

# A. i. Create a modified  finger_counter() generator function to yield the counts for all ten fingers on both hands.
# ii. Call next() ten times to count all ten fingers. Use both syntax variations.
# iii. Add a for loop  to count all ten. Then add a time.sleep(1) command so the fingers are counted once per second.
#  The time module has already been imported at the top.
def finger_counter2():
    yield "R1"
    yield "R2"
    yield "R3"
    yield "R4"
    yield "R5"
    yield "L1"
    yield "L2"
    yield "L3"
    yield "L4"
    yield "L5"

f2 = finger_counter2()
print f2.next()
print next(f2)
print next(f2)
print next(f2)
print next(f2)
print next(f2)
print next(f2)
print next(f2)
print next(f2)
print next(f2)

# B. Construct a fresh ten-finger counter, and use a while loop to step through it.
# In this case, you will have to go over the cliff, and catch the StopIteration exception.
f2 = finger_counter2()
while True:
    try:
        print f2.next(); time.sleep(1)
    except StopIteration as e:
        print "No fingers left.", repr(e)
        break