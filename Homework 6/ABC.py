from A import *

# Next define B as a subclass of A and C as a subclass of B.
# Objects in B can invoke all the public methods in the super class A.

class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.name = "I'm a B"
        self._ID= "Letter # 2"
        self.__password = 2222

    def _method(self):
        print "I'm a method in B starting with one underscore."

    def __method(self):
        print "I'm a method in B starting with two underscores."

    def __repr__(self):
        return "I'm an object in the class B."  # Same for all b's in this class.


class C(B):
    def __init__(self):
        super(C, self).__init__()
        self.name = "I'm a C"
        self._ID= "Letter # 3"
        self.__password = 3333

    def _method(self):
        print "I'm a method in C starting with one underscore."

    def __method(self):
        print "I'm a method in C starting with two underscores."

    def __repr__(self):
        return "I'm an object in the class C."  # Same for all c's in this class.



# Start of demo code
if __name__ == "__main__":
    a = A()  # Construct an object of type A.
    print "1. Little 'a' is an object in the superclass A. The type of a is:", type(a)
    a.method()  # Zero underscore method calls two underscore method, both in class A.
    a._method() # One underscore method from class A.


    b = B()  # Construct an object of type B.
    print "\n2. Now b is an object in the subclass B. The type of 'b' is:", type(b)
    print "The magic 'repr' method converts all b's to the string:", b
    print "Since every B is an A, 'b' can invoke any method from the superclass A."
    print "Below, 'b' invokes 'method', from the superclass. Note it reports itself as an A!!!"
    print "Little 'b', reports itself as an A!"
    b.method()



    print "\n3. Now for the weird stuff!"
    print "Examine the code to see how B attempts to override both '_method' and '__method' from the superclass A. "
    print "Note one method has one underscore, the other two. But the behavior is very different!"

    print "i. Calling the one underscore '_method' we see the override has worked! It knows it is in B (not A)."
    print "\t\t", ; b._method()

    print "\nii. But if we call method, which itself calls '__method', note it still uses the '__method' from the superclass."
    print "\t\t", ; b.method()

    print "\n4. Note  'b' can display all its attributes using the reveal() method from the  super class A."
    print "Every instance in B is also an A. But lookout! Not all of B's attributes have taken root. \n"
    print "Can you figure out which attributes change and which stick to the values in the superclass?"
    print "Hint: Look at that password!"
    b.reveal()


    print "\n\nNow confirm similar behavior for class C which is a subclass of B which is a subclass of A. "
    # Now add code here for an object c in C, similar to all the above code for b in B.
    # Carefully note the different behaviour for one and two underscore attributes and methods.
    c = C()  # Constructs an object of type C.
    c.method()
    c.reveal()