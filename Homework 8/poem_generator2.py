# Write a generator function for this poem.
# Here are the first five stanzas of the poem "Dragon Song".

stanza1 = """Twas a night of awe and magic
Every dragon--one and all
Had gathered by the sea to fly
And answer instinct's call.
"""

stanza2 = """One by one, they would step forth
and sing their own heartsong
Hoping it'd attract the one
To whom their heart'd belong.
"""

stanza3 = """A dragon stood, waiting his turn
to step forward and sing
a newcomer to the whole event
and tense as a coiled spring.
"""

stanza4 = """Finally his turn arrived
He stepped forth into the ring
Cleared his throat, searched deep inside
and then began to sing...
"""

stanza5 = """'Calling, calling, hear my cry
O love, I'm searching through the sky
For you, O love, wherever you fly
My love for you shall never die! no! Love shall never die.
"""

"""
a. Write a generator function using the header  >>> def dragon_song():
that on each call yields the next stanza. Do not use print, just yield the string
with the next stanza. Then construct a generator iterator using:
"""
# Add code below to complete the dragon song generator function.

def dragon_song():
    yield stanza1
    # Add the missing yields here.
    yield stanza2
    yield stanza3
    yield stanza4
    yield stanza5

poem_generator = dragon_song()

# b. Print this poem sample using a for loop here.
print "DRAGON SONG\n"
for stanza in poem_generator:
    print stanza



# c. Construct a fresh generator and print this poem sample using a while loop instead.
# Complete the try block.
poem_generator = dragon_song() # Fresh generator
while True:
    try:
        poem_generator.next()
    except StopIteration as e:
        pass
