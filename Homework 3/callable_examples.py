import string
import random
import math

intro1 = """A callable is an object that allows you to use round parenthesis ( )
and eventually pass some parameters, just like functions.
"""
print intro1

intro2 = """In Python, a callable is an object which has a __call__ method.
You usually don't see the call method.
That's hidden behind the scenes. But you are using it every time you use round parentheses ().
"""
print intro2

intro3 = """If f is callable, you can enter f() or perhaps f(10) if it requires  an argument.
f(10) for a callable object f is equivalent to f.__call__(10)
Here are some examples to show that equivalence.
"""
print intro3


print "Example 1: The int() method is callable."
print  'Is "int" callable?', callable(int)
print "The string '10' equals the integer:", int('10')
print "The string '10' equals the integer:", int.__call__('10')

print "Convert the binary number '111111' to base 10."
print "Converting to base 10 we get:", int('111111’, 2)
print "Converting to base 10 we get:", int.__call__('111111’, 2)


print "\nExample 2: The max() method is callable."
print  'Is "max" callable?', callable(max)
print "The max of 1, 2 & 3 is:", max(1, 2, 3)
print "The max of 1, 2 & 3 is:", max.__call__(1, 2, 3)


print "\nExample 3: The upper() method in the string module is callable."
print 'Is "upper" callable?', callable(string.upper)

s = "usa"
print "I live in the %s." % s.upper()
print "I live in the %s." % string.upper(s)

print "I live in the %s." % s.upper.__call__()
print "I live in the %s." % string.upper.__call__(s)


print "\nExample 4: The sin() method in the string math is callable."
print 'Is "sin" callable?', callable(math.sin)

print "The sin of 0 radians is:", math.sin(0)
print "The sin of 0 radians is:", math.sin.__call__(0)
print "Is the math module itself callable?", callable(math)


print "\nExample 5: Strings are not callable."
my_string = "I am a string."
print "Is this string callable?", callable(my_string)
print "Is the string  module callable?",callable(string)
try:
    print "Testing if a string is callable."
    my_string(10) # Here we try to call a string.
except Exception as e:
    print "Nope! A string object is not callable."
    print e.message

print "\nExample 6: You can create your own callable objects by defining the __call__ method in a class. "


class MyCallable(object):
    def __call__(self, x):
        print "I was called by %r" %x

i_can_call = MyCallable()
print "Am I callable?", callable(i_can_call)
i_can_call("Hello")
i_can_call("Who's calling?")
i_can_call(10)
i_can_call(math)


print "\nExample 7: A custom function defined using def is callable."
def knock_knock(name):
    print "Who's there?", "It's me, %s." % name
print "Is knock_knock callable?", callable(knock_knock)

knock_knock("Fluffy, your cat")
knock_knock.__call__("Fluffy, your cat")

print "\nExample 8: Is callable itself callable."
print "Is callable itself callable?",  callable(callable)
print "Here it is being called on itself.", callable.__call__(callable)


print "\nExample 9: UncallablePerson example."
class UncallablePerson:
    def __init__(self, name):
        self.name = name
        self.phone_number = None

Joe = UncallablePerson("Joe")
God = UncallablePerson("God")
print "What is Joe's phone number?", Joe.phone_number
print "Is Joe callable?", callable(Joe)

print "What is God's phone number?", God.phone_number
print "Is God callable?", callable(God)


"""
print "\nExample 10: The builtin quit() method is callable."
print "Is the quit method callable?", callable(quit)

quit.__call__()  # This will indeed quit!
print "If this prints, the above quit call did not work."
"""


# * * * * * * * * * Be sure to comment out example 10 before proceeding! * * * * * * * * *
# EXERCISES
# A. Add your code for exercise A here. See PDF. There are seven parts!
# Demonstrate the __call__ method equivalence for each,(if it is callable).
a = 3
if callable(a):
    a.__call__()
if callable(math):
    math.__call__()
if callable(math.sqrt):
    math.sqrt.__call__()
if callable(math.pi):
    math.pi.__call__()
if callable(range):
    range.__call__()
if callable(for):
    for.__call__()
if callable(if):
    if.__call__()


# B. Add your code for exercise B here.

class RudePerson:

    def __init__(self, name, insult):
        self.name = name
        self.insult = insult

    def __call__(self, target, *args, **kwargs):
        saying = self.name + ": " + self.insult + " " + target
        print saying

# Construct two rude people. Then have them call each other and fling insults!
b = RudePerson("Bill", "You suck")
t = RudePerson("Ted", "Ur shit")
print b(t)