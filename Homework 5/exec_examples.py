# Some more examples using exec.
import pprint

# The exec command does not only accept strings as arguments.
# You can also pass it bytecode.

print "Example 1: Passing bytecode to exec"

# Let's create some bytecode to add 1 +2.

code_object = compile('a = 1 + 2', '<string>', 'exec')
# What is the type of this code_object?
print "The code_object returned by compile is of type:", type(code_object)

print "Recall that dir(), when called without an argument, returns the names in the current scope."
print "a. Note that compiling the code object does not result in a = 1+2 being defined. There is no 'a' below."

print dir()


# OK, now let's execute this bytecode, and print out the sum.
exec code_object
print "The value of a = 1+2 is:", a
print "b. After exec'ing the code, a = 1+2 is defined. "
print "Your compiler may complain that 'a' is an unresolved reference, but it works! Note 'a' now appears below."
print dir()



print "\n\nExample 2: What's up with that second argument '<string>'?"
print "The second argument to compile is the filename hint.\n" + \
      "If we are compiling from an actual string there we should provide a value enclosed in angular brackets, \n" + \
      "because this is what Python will do. <string> and <stdin> are common values. "

# Let's repeat the same problem, but with code in the file: demo1.py
print "First delete 'a' from the local scope, and check that it has indeed been removed.\n" \
      "There should ne no 'a' below."
del a
# Check that 'a' has been removed.
print dir()

print "The file demo1.py has the single statement \"a = 1 +2\""
print "Let's compile demo1.py."
code_object = compile('a = 1 + 2', "demo1.py", 'exec')

print "Now exec the code object."
exec code_object
print "Awesome! The value of 'a' is:",  a
print "Let's check that 'a' has been added back to the local namespace. Do you see an 'a' below?"
print dir()



print "\n\nExample 3: The third argument to the compile command."

print "The third parameter can be one of 'exec', 'eval' and 'single'."

print "i. The first one is what exec is using."
print "ii. The second is what the eval function uses. "
print "The difference is that the exec can contain statements, but eval only expressions."
print "iii. The choice 'single' is a hybrid mode which is only used for interactive shells."
print "It exists solely to implement things like the interactive Python shell and we will not use it."

print "\nLet's test this out, by attempting to use 'eval' instead of 'exec'."
print "Even though the source code in demo1.py contains a statement, let's try 'eval' instead of 'exec' anyways."
print "What could go wrong? Also try 'single'."
del a  # Let's delete 'a' first.
print dir()
code_object = compile('a = 1 + 2', "demo1.py", 'exec')  # exec changed to eval! But the code includes statements!
exec code_object
print a
print dir()

del a
print "\n\nExample 4: Always execute against a new environment!!!!"
print "Above, we did something you should never, ever, ever use; executing code in the calling code's namespace.\n" + \
      "What should you do instead? Always execute against a new environment. See code for example 4. "

code = compile('a = 1 + 2 +3 ', '<string>', 'exec')  # Let's change 'a' for clarity.
new_name_space = {}  # Declare a new namespace, in which no variables have been declared.
exec code in new_name_space  # Exec the code in a fresh, new  namespace!

try:
      print "The value of a is:", a
except Exception as e:
      print repr(e)

print "But the code was exeuted! We can find the result for 'a' = 1 + 2 + 3 in the new  name space.!"
print "The value of 'a' is:", new_name_space['a']


print "\n\nExample 5: Outside of a function or class declaration, the local scope is the global scope. "
print "i. Let's test that now."
print "Does the local scope equal the global scope?", locals() is globals()
print "\nii. Now let's see if that is true inside a function."


def height():
    print "As soon as we enter the function, the local namespace is:", locals()

    height = [5, 10]
    print "Next we define 'height' inside the function, and the local namespace becomes:", locals()

    print locals()
    locals()['height'] = [4, 2]
    print locals()
    print "ii. Now does the local scope equal the global scope?", locals() is globals()
    return height

print height()