# We will model a Tower of Hanoi as having three HanoiStacks and two integer counters.

# from Stack import *
from HanoiStack import *


class TowerOfHanoi:
    def __init__(self, n):
        self.A = HanoiStack()
        self.B = HanoiStack()
        self.C = HanoiStack()
        self.numberOfRings = n
        self.numberOfMoves = 0
        for k in range(self.numberOfRings, 0, -1):
            self.A.push(k)
        # Exactly one stack is at rest. Depends on even or odd number of rings.
        if n%2 == 0:
            self.C.isActive = False
        else:
            self.B.isActive = False


    def __str__(self):
        return "A: " + str(self.A) + "\nB: " + str(self.B) + "\nC: " + str(self.C)

    # The puzzle is solved when both stacks A and B are empty.
    def isDone(self):
        return self.A.isEmpty() and self.B.isEmpty()

    def updateStackActivityStatus(self):
        # Assume stacks A, B and C have indices 0, 1, 2.
        # Let the number of rings be n.
        # Then after k moves, the inactive stack has index: (2-k) %3 if k even, else (1+k) % 3
        k = self.numberOfMoves
        if self.numberOfRings % 2 == 0:
            inactive_index = (2-k) % 3
        else:
            inactive_index = (1+k) % 3

        self.A.isActive = True; self.B.isActive = True; self.C.isActive = True
        if inactive_index == 0: self.A.isActive = False;
        if inactive_index == 1: self.B.isActive = False;
        if inactive_index == 2: self.C.isActive = False;



    def solve(self):
        if self.isDone(): return
        # Find the  two active stacks.
        all_stacks = [self.A, self.B, self.C]
        active_stack = []
        for stack in all_stacks:
            if stack.isActive:
                active_stack.append(stack)
        active_stack[0]( active_stack[1])

        self.numberOfMoves +=1
        self.updateStackActivityStatus()
        print "\nAfter move number: ", self.numberOfMoves; print self



if __name__ == "__main__":
    tower = TowerOfHanoi(3)  # Construct the Tower of Hanoi with this many rings.
    print "Starting position:"
    print tower

    while not tower.isDone():
        tower.solve()

    print "\nThe puzzle has been solved in %d moves!" % tower.numberOfMoves




