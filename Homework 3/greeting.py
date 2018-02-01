

"""
Generally. There is no method overloading in python.
Overloading in other languages occurs when two methods have the same name, but different numbers of arguments.
In python, if you give more than one definition using the same name,
the last one entered rules, and any previous definitions are ignored.

"""

# Here an unsuspecting student attempts to overload a method named "greeting" with several definitions.

def greeting():
    print "Hi! Are you new here?\n"

# The second takes one argument, and can be used to greet a person whose name you know.
def greeting(name):
    print "Yes! It's my first day! My name is %s.\n" % name

# The third takes two arguments, and can be used to name both yourself and the addressee.
def greeting(name1, name2):
    print "Nice to meet you %s! My name is %s.\n" % (name1, name2)

# The fourth takes one argument, conceived to be an integer.
def greeting(n):
    print "Can I borrow $%d for coffee?\n" % n

# The fifth  takes one argument, conceived to be a boolean.
def greeting(b):  # A boolean.
    if b:
        print "Sure! Let's have coffee together.\n"
    else:
        print "Sorry! I'm flat broke!\n"

# Hmmm,  that did not work! There is no overloading in Python!
try:
    greeting()
except Exception as e:
    print e.message

try:
    greeting("Mork")
except Exception as e:
    print e.message

try:
    greeting("Mork", "Mindy")
except Exception as e:
    print e.message

try:
    greeting(10)
except Exception as e:
    print e.message

try:
    greeting(True)
except Exception as e:
    print e.message


