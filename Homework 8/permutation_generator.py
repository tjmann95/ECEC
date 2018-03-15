# Example featuring a recursive function generator.
# See: http://www.python-course.eu/generators.php


# Awesome! A recursive example!
def permutations(items):  # <- Expects an iterable such as a string, list or tuple.
    n = len(items)
    if n == 0: yield () # An empty tuple
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield (items[i],)+cc

print "Example usages\n"
print "1. We can call the method directly on any iterable, such as a string."
print "\nThe 3! permutations of the word 'cat' are:"
for p in permutations( "cat"): print ''.join(p)

# Either of these will produce the same output.
# for p in permutations( ['c', 'a', 't'] ): print ''.join(p)
# for p in permutations( ('c', 'a', 't') ): print ''.join(p)

print "\n2. We can call the method directly on any iterable, such as a list or tuple."
# These permutations are numbered as they are printed.
print "The 4! permutations of the four letters in the word 'game' are:"
count = 0
for p in permutations(tuple("game")):  # <- Input is a list, which is also iterable.
    count += 1
    print "%3d." % count, ''.join(p)


print "\n3. In this example, the characters are NOT unique. We'll solve that shortly."
print "Many of these permutations of the letters in the word 'banana' are repeated:"
count = 0
"""
for p in permutations(list("banana")):
    count += 1
    print "%3d." % count, ''.join(p)
"""


# Revised method returns only distinct permutations. DONE FOR YOU - FREE!
def distinct_permutations(items):  # <- Expects any iterable as its input. (string, list, tuple)
    n = len(items)
    distinct_permutations = set() # Create an empty set.
    if n==0: yield set() # Yield an empty set if there are no items to permute.
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                next_perm = (items[i], )+cc  # tuple addition. Note the comma! Won't work without it.
                if next_perm not in  distinct_permutations:
                    distinct_permutations.add(next_perm)
                    yield next_perm

print "\n4. The *distinct* permutations of the letters in the word 'banana' are:"
count = 0
for p in distinct_permutations("banana"):
    count += 1
    print "%3d." % count, "".join(p)

