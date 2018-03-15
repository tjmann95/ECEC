# Introduction to generators #2.
# Consider this generator which prints the lines of a poem and yields the line number after each line.


def poem():
    print "There was an old man with a beard";       yield 1
    print 'Who said, "it\'s just how I feared!"';    yield 2
    print "Two owls and a hen";                      yield 3
    print "Four larks and a wren";                   yield 4
    print "Have all built their nests in my beard."; yield 5


gen1 = poem()

for a in gen1:
    try:
        gen1.next()
    except:
        pass


