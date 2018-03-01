"""
A subclass of the Stack superclass designed to help solve the Tower of Hanoi problem.
Unlike classical stacks, HanoiStacks are callable.

If A and B are  HanoiStacks  then
A(B) is defined so that the stack with the smaller element on top is popped and then pushed onto the other stack.
No value is returned, but both stacks are changed; unless both stacks are empty, and then nothing happens.

Since the definition is symmetric, A(B) and B(A) produce the same result.
Is is also always the case that A(A(B)) and B(A(B)) have no effect. The previous action is undone.

Each new element on a HanoiStack must be smaller than the previous, except the first.
"""

from Stack import *


# Note that super() can only be used with new-style classes.
# Therefore Stack was converted to new-style for this homework.

class HanoiStack(Stack):
    # A HanoiStack is first of all, a Stack.
    def __init__(self):
        super(HanoiStack, self).__init__()
        # A HanoiStack has a flag which makes it active or inactive.
        self.isActive = True

    # But HanoiStacks can call each other.
    def __call__(self, other):
        # We will have to handle a few special cases first.
        # If both HanoiStacks are empty, just return. Use isEmpty() twice.
        if self.isEmpty() and other.isEmpty():
            return

        # If the calling stack named 'self' is empty, pop 'other' and push that onto 'self'.
        if self.isEmpty():
            self.push( other.pop() )
            return
        # If the called stack named 'other' is empty, pop 'self' and push that onto 'other'.
        if other.isEmpty():
            other.push( self.pop() )
            return

        # Now handle the general case. Assume neither stack is empty.
        # Pop the stack with the smaller item on top and push that onto the other stack.
        # If the top of stack 'self' is less than the top of 'other', pop 'self' and push onto 'other'
        if self.peek() < other.peek():
            other.push( self.pop() )
        else:
            self.push( other.pop() )

    def __str__(self):
        if self.isActive:
            return "+ "  + str(self.items)
        else:
            return "- "  + str(self.items)





if __name__ == "__main__":
    A = HanoiStack()
    print "1. A was just created. Is A empty?", A.isEmpty()

    A.push(3);  A.push(2);   A.push(1);
    print "Is A empty after pushing items onto it?", A.isEmpty()

    print "Here is A with its items:",  A
    print "Note the plus sign which indicates its status is active.\n\n"


    print "2. B and C are two empty HanoiStacks."
    B = HanoiStack()
    C = HanoiStack()
    B.isActive = False

    print "Here are all three HanoiStacks A, B and C. Which one is the inactive one?"
    print "A:", A
    print "B:", B
    print "C:", C

    print "\n\n3. Hey! We have a Tower Of Hanoi with n = 3. Let's solve it in 2**n - 1 = 7 moves. "


    print "\nMove 1: A(C), then move the inactive arrow one to the right from B to C since n is odd."
    A(C);     B.isActive = True;    C.isActive = False;
    print "A:", A
    print "B:", B
    print "C:", C


    print "\nMove 2: A(B), then move the inactive arrow one to the right from C to A since n is odd."
    A(B);     C.isActive = True;    A.isActive = False;
    print "A:", A
    print "B:", B
    print "C:", C


    print "\nMove 3: B(C), then move the inactive arrow one to the right from A to B since n is odd."
    B(C);     A.isActive = True;    B.isActive = False;
    print "A:", A
    print "B:", B
    print "C:", C


    print "\nMove 4: A(C), then move the inactive arrow one to the right from B to C since n is odd."
    A(C);     B.isActive = True;    C.isActive = False;
    print "A:", A
    print "B:", B
    print "C:", C


    print "\nMove 5: A(B), then move the inactive arrow one to the right from C to A since n is odd."
    A(B);     C.isActive = True;    A.isActive = False;
    print "A:", A
    print "B:", B
    print "C:", C



    # Add code here to solve the  problem with two more moves.  Moves number 6 and 7.
    # Have the two active stacks call each other, move the inactive arrow one to the right since n is odd.
    B(C)
    A.isActive = True
    C.isActive = False

    A(B)
    A.isActive = False
    B.isActive = True
