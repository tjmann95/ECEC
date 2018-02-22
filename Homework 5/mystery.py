# Please read this reference carefully.
# Many examples are from there. Be CERTAIN to read the Warnings and Gotchas at the end.

# http://late.am/post/2012/04/30/the-exec-statement-and-a-python-mystery.html

print "WARNING: Never execute untrusted code submitted by end-users of your system!\n"


print "1. Here is the Hello World! example again as a code object."
code_object = compile("print \"Hello, world!\"", '<string>', 'exec')

print "Find out if the code_object is callable using callable()."
isItCallable = callable(code_object)
print isItCallable

# Try calling it anyway to see the error message.
try:
    code_object()
except Exception as e:
    print repr(e)

print "\n2. OK, our code object is not callable. That's what exec is for."
print " i. Here the code_object is executed using parentheses: >>> exec(code_object)"
exec(code_object)
print "ii. Here the code_object is executed without parentheses: >>> exec code_object "
exec code_object


print "\n3. Assignment statements in code objects"

# Now here is a function that takes a code object and x, and returns whatever variable x is input.
# All it does is dynamically execute the code object and return the input x.
# Is it possible that x might change? Note no lines of code explicitly change x.

def exec_code_and_return_x(code_object, x):
    exec code_object
    return x

# Is it possible that x might change? Let's see if we can increment and return.
my_code_object = compile("x = x + 1", '<string>', 'exec')
print "a. If we input x = 1, and increment x we get: ", exec_code_and_return_x(my_code_object, 1)
print "Good! That was expected!"

print "\nb. But sometimes the output might be surprising!"
print "Here is a new code object. See code inside mystery.py"

my_code_object = compile("del x", '<string>', 'exec')  # This code object deletes x instead of incrementing it.
print "b. If we input x = 1, and then delete it, we still get: ", exec_code_and_return_x(my_code_object, 1)
print "That's weird! It printed x!! You might have expected an error, since x has been deleted."


print "\nc. Example to show why an error might be expected."
x =1; del x; print "After deleting x=1, attempting to print it gives:"

try:
    print "Trying to print the deleted variable x: ", x
    print "The  type of the deleted x variable is:", type(x)
except Exception as e:
    print repr(e)


print "\n4. To understand this mystery, we know to look more closely at how SCOPING works!"
print "Without any additional instructions, exec uses the current global and local namespaces to execute your code." + \
    "\nThis means that (as we saw above), code objects being exec'd can modify variables in scope when it is exec'd" + \
    "\n(as well as any globals the code object happens to manipulate)."

print "You can customize (to a certain extent) the scope given to the code object by using the in \"arguments\" to exec:"
print "Examine the code now to see how that is done.\n"

code_globals = {}
code_locals = {}  #
code_object = compile("x = 1", '<string>', 'exec')
exec code_object in code_globals, code_locals
print "Now the local variables are: ", code_locals.keys()
print "The glocal variables are always available:", code_globals.keys()


print "\n\n5. Now that we know about scoping, it is time to solve the above mystery."
print "Let's go back to the code object to delete x. See code now. "
my_code_object = compile("del x", '<string>', 'exec')  # This code object deletes x instead of incrementing it.
print "Recall, that if we input x = 1, and then delete it, we still get the 1 back: ", exec_code_and_return_x(my_code_object, 1)
print "MYSTERY: Why can't the code object delete the local variable x?"

print "\nHere is a simple method without using exec that shows deleting the local variable. See code now."
# Some code which deletes a local variable, then attempts to return it. Generates an error because x has been deleted.
def delete_local_then_return_it():
    x = 1
    del x
    return x

try:
    delete_local_then_return_it()
except Exception as e:
    print repr(e)

print "\nSolving the mystery. The implementation of exec, that is, of the EXEC_STMT opcode, " +\
      "\narranges for a NEW PYTHON STACK FRAME to be pushed, which means that it HAS ITS OWN ARRAY OF LOCALS," +\
      "\n(those used by the code object being exec'd."

print "\nOK, Now run and study the file mystery_solved.py"
