import os

# Examples for Dynamic Execution using exec statement


# Example 1 - Hello World!
print "Example 1 - Hello World!"

# Try other equivalent variants of s, to explore your options with nested quotes. See PDF.

s = 'print "Hello, World!"'
exec s


print "Because the code string requires quotes; it can cause problems with other nested quotes."

# Try other versions for example 1 here. See the PDF.
s = "print "Hello, World!""
exec s
s = "print 'Hello, World!'"
exec s
s = "print \"Hello, World!\""
exec s
s = "print(\"Hello, World!\")"
exec s




