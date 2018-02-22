import inspect

print "\nSolving the mystery. The implementation of exec, that is, of the EXEC_STMT opcode, " +\
    "\narranges for a NEW PYTHON STACK FRAME to be pushed, which means that it HAS ITS OWN ARRAY OF LOCALS," +\
    "\n(those used by the code object being exec'd."

print "\nWe imported the \"inspect\" module to get a closer look."
print "Use the command \"inspect.currentframe()\" to inspect the current frame."
print "Next step is to explore the depth of the stack. A method is provided to do that. See code"


# Here is a method to inspect and return the depth of a stack.
def get_stack_depth():
    frame = inspect.currentframe()
    # begin depth at -1 to account for the extra
    # frame created when calling get_stack-depth
    depth = -1
    while frame:
        depth += 1
        frame = frame.f_back
    return depth

print "\n1. Example showing how stack depth grows using a recursive countdown method."
print "We countdown from 10 to 0 using recursion. With each call, the stack depth grows by 1. "

def countdown(n):
    if n < 0:
        return
    print n, # Print each number as we countdown to 0.
    frame = inspect.currentframe()
    print "\tNow the stack depth is:", get_stack_depth()
    n -= 1
    countdown(n)

print "\nAt the top level, before the countdown starts, the stack depth is: ", get_stack_depth()
countdown(10)
print "When the countdown method is finished, the stack depth drops back to: ", get_stack_depth()

print "\n\nExample 2. Now let's see how the stack grows when using the exec command."



def compare_stack_depths():
    print '1. Stack depth inside ordinary function call:', get_stack_depth()
    exec compile("print '2. Stack depth after using exec to run the same thing: ', get_stack_depth()", '<string>', 'exec')

compare_stack_depths()


print "Notice how 2 increased to 3. "
print "The implementation of exec, arranges for a new Python stack frame to be pushed, " + \
      "\nwhich means that it has its own array of locals!"


print "\n\nExample 3. Code objects can however modify the local variables on their own stack frame. "
x = 111; y = 222

def show_code_object_locals():
    code_globals = {}
    code_locals = {'x': 1, 'y' : 2}
    print "Now my local variables are x = 1 and y = 2.", "Proof:", code_locals
    print "The sum of x and y is:", code_locals['x'] + code_locals['y']
    print "Note just plain x refers to the x = 111 from the outer scope. Indeed x =", x

    print "Now the local variable x is deleted, but not y."
    exec compile("del x", '<string>', 'exec') in code_globals, code_locals
    return code_locals

print show_code_object_locals()