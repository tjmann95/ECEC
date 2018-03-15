# Introduction to generators
# Consider this generator function which prints the lines of a poem and yields the line number after each line.

def poem():
    print "There was an old man with a beard";       yield 1
    print 'Who said, "it\'s just how I feared!"';    yield 2
    print "Two owls and a hen";                      yield 3
    print "Four larks and a wren";                   yield(4)
    print "Have all built their nests in my beard."; yield(5)

print "1. This code defines a generator function named poem."
print "Typing >>> poem() seems to do nothing, so this is not an ordinary function. "
poem()  # <-- Seems to do nothing!

print "\n2. However, the type command reports 'poem' is indeed a function: >>> type( poem )\n\t", type( poem )


print "\n3. Let's check if the function 'poem' is callable? >>> callable(poem)\n\t", callable(poem)


print "\n4. Awesome! it's callable, but what is it returning?"
gen1 = poem()  # gen1 is the object returned when poem is called.
print "When poem() is called like this, it returns a:", type(gen1)
print "Here is a string that represents it:", repr(gen1)


print "\n5. If all the yields are removed, the poem prints as usual."
del poem


def poem():
    print "There was an old man with a beard"
    print 'Who said, "it\'s just how I feared!"'
    print "Two owls and a hen"
    print "Four larks and a wren"
    print "Have all built their nests in my beard."

# Print the poem as usual.
poem()

print "\n6. Let's go back to the original version with the yields."
del poem

def poem():
    print "There was an old man with a beard";       yield 1
    print 'Who said, "it\'s just how I feared!"';    yield 2
    print "Two owls and a hen";                      yield 3
    print "Four larks and a wren";                   yield 4
    print "Have all built their nests in my beard."; yield 5


gen1 = poem()



print "One method to get the generator to do something, is to invoke the next() method. "
# The first call to next() prints the first line of the poem, returns 1 and stops. But it remembers where it is.
line_number = gen1.next()
print line_number

# The second call to next() prints the second line of the poem, returns 2 and stops. The pointer is set to the next line of code.
line_number = gen1.next()
print line_number

# Let's call it three more times to print out the rest of the poem. We won't bother with the numbers.
gen1.next(); gen1.next(); gen1.next()

print "\nNow the pointer is at the end of the generator. What happens if we call next() again? "
try:
    gen1.next()
except Exception as e:
    print "Sorry, you have stepped over the cliff:", repr(e)



print "\n7. Next we build a fresh generator, and use a for loop to step right through it."
print "We'll just toss out the line numbers using 'pass'. \n"

gen1 = poem() # Fresh generator with pointer at the beginning of the function.
for line in gen1:
    pass  # Toss out the line numbers. Just show the poem itself.


print "\n8. Next we build a fresh generator, and use a for loop to step right through it."
print "This time, we collect the line numbers which are yielded in a list.\n"

gen1 = poem() # Fresh generator with pointer at the beginning of the function.
line_number_list = []
for a in gen1:
    line_number_list.append(a)

print "\nOur poem contains these line numbers:", line_number_list


# * * * Exercises start here * * *

# A. Create a new version of the poem() method, but instead of the line number,
# it yields the cumulative word count for each line.
# Just treat words as being separated by white space such as spaces.
# You can split each string into a list, and use len() to count how many items it contains.
# Cumulative means that after line two, it returns the count in both lines 1 and 2, and so on.
# No need to print the lines of the poem. Just the cumulative word counts.

print "\n9. Cumulative Word Counts"

# Complete this generator function below.
def poem():
    word_count = 0
    line = "There was an old man with a beard"
    word_count += len(line.split())
    yield word_count

    line = 'Who said, "it\'s just how I feared!"'
    word_count += len(line.split())
    yield word_count

    line = "Two owls and a hen"
    word_count += len(line.split())
    yield word_count

    line = "Four larks and a wren"
    word_count += len(line.split())
    yield word_count

    line = "Have all built their nests in my beard."
    word_count += len(line.split())
    yield word_count

"""
B. Create yet another version of the poem() generator function, but now it yields the cumulative vowel count
for each line. Cumulative means that after line two, it returns the count in both lines 1 and 2, and so on.
No need to print the lines of the poem. Just the cumulative vowel counts. Use:  vowels = "aeiouAEIOU"
"""


print "\n10. Cumulative Vowel Counts"
# Complete this generator function below.

def poem():
    vowels = "aeiouAEIOU"
    vowel_count = 0
    line = "There was an old man with a beard"
    # Update the vowel_count here.
    for char in line:
        if char in vowels:
            vowel_count += 1
    yield vowel_count

    # Handle the remaining lines here.
    line = 'Who said, "it\'s just how I feared!"'
    # Update the vowel_count here.
    for char in line:
        if char in vowels:
            vowel_count += 1
    yield vowel_count

    line = "Two owls and a hen"
    # Update the vowel_count here.
    for char in line:
        if char in vowels:
            vowel_count += 1
    yield vowel_count

    # Update the vowel_count here.
    line = "Four larks and a wren"
    for char in line:
        if char in vowels:
            vowel_count += 1
    yield vowel_count

    # Update the vowel_count here.
    line = "Have all built their nests in my beard."
    for char in line:
        if char in vowels:
            vowel_count += 1
    yield vowel_count

f = poem()

# This for loop will print out the vowel_counts.
for count in f:
    print count


