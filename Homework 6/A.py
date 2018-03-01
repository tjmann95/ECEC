# Two underscores in the beginning should not be used to mark a method as private.
# The purpose of two underscores is to avoid your method being overridden in a subclass.

# Class A has three methods named: method, _method and __method.


class A(object):

    def __init__(self):
        # There are three attributes.
        self.name = "I'm an A"   # Note - no underscores - public
        self._ID  = "Letter #1"  # Note - one underscore - protected
        self.__password = 1111   # Note - two underscores - private

    def _method(self):     # Starts with *ONE* underscore in the beginning! - protected
        print "I'm a method in A starting with ONE underscore."

    def __method(self):     # Starts with *TWO* underscores in the beginning! - private
        print "I'm a method in A starting with TWO underscores."

    def method(self):       # Here, the no underscore method() is public, and simply calls the two underscore __method()
        self.__method()

    def reveal(self):       # Reveals attributes with 0, 1 & 2 underscores. This method is public.
        print "Name:    \t",  self.name
        print "ID:   \t\t",   self._ID
        print "Password:\t",  self.__password


if __name__ == "__main__":
    a = A()  # Construct an object of type A.
    print "1. The letter little a is an object in the class A. The type of a is:", type(a)
    print "\nWe can show all three attributes using the public method reveal()."
    print "This is true even though the three attributes have 0, 1 & 2 underscores respectively. "
    a.reveal()


    print "\n\n2. The class A has three methods named: method, _method and __method."
    print "They only differ by the number of underscores."
    print "The public method named method(), simply calls __method, with two underscores."

    print "\ni. There is no problem calling method() - the one with no underscores.\n" \
          "It's public and calls the 2-underscore version"
    print "Here is the NO underscore method() in action:",
    a.method()   # I have no underscores. Use me here or invoke me by any object in a subclass.

    print "\nii. There is no problem calling _method() - the one with ONE underscore."
    print "Even though that method is protected, protected methods *CAN* be called within their own class. "
    print "But the user is not supposed to do that. It is considered very rude in Python!\n" + \
          "Shame on you (or me in this case)!"

    print "Here is the ONE underscore _method() in action:",
    a._method()   # I have ONE underscore. You should use me in my own class only! Protected!


    print "\niii. There is a BIG problem trying to call   '__method()' - the one with TWO underscores."
    print "We get an odd error message. "
    print "Here is an attempt to call the TWO underscore '__method()'."
    try:
        a.__method()
    except Exception as e:
        print "The two underscores method caused this error:", repr(e)


    print "\n * * * Getting the variables directly * * * "
    print "Here the user ignores the 'reveal' method and tries to print out all three attributes directly."

    print "Name:    \t",  a.name   # public
    print "ID:      \t",  a._ID    # protected
    try:
        print "Password:\t",  a.__password  # two underscores.
    except Exception as e:
        print "Woops! We got the error  message is:", repr(e)

    # Quiz alert! Study this carefully!
    # Add code here to print out the '__password' attribute using name mangling.
    # Recall you will need to combine the class name and the variable.
    print a._A__password