# Examples of compound statements and multi-line statements in Python


# Reading assignment. Pleasre read this page cafrefully.
# http://www.tutorialspoint.com/python/python_basic_syntax.htm

""" Compound statements contain (groups of) other statements; they affect or control the execution
of those other statements in some way. In general, compound statements span multiple lines,
although in simple incarnations a whole compound statement may be contained in one line.
"""


""" Multiple Statements on a Single Line
The semicolon ( ; ) allows multiple statements on a single line given that neither statement starts a new code block.
"""

print "\nExample 1: Multiple statements on the same line separated by semicolons. Check the code."
x = 1; y = 2; z = 3  # Three statements in the same line separated by semicolons.
print "The values for x, y and z are: ", x, y, z


#  Multi-Line Statements
# Statements in Python typically end with a new line.
# Python does, however, allow the use of the line continuation character (\) to denote that the line should continue.

print "\nExample 2: Multi-Line Statements using the line continuation character \. Check the code"
item_one = 1.15; item_two = 2.50; item_three = 3.50    # Multiple statements - on one line.

 # One statement - on multiple lines.
total = item_one + \
        item_two + \
        item_three

print "The total cost is $"; print total    # Two print statements on one line.


print "\nExample 3: Pythonic assignment on one line and a Multi-Line Statement. Check the code!"

a, b, c, d = 1.15, 2.50, 3.50, 4.50   # Single statement on one line. Pythonic tuple assignment.
# Find the total a+b+c+d using a multi-line statement and the line continuation character \.
total = a + \
    b + \
    c + \
    d

print "The total a+b+c+d is: ", total    # Single line with one print statement.

""" A compound statement consists of one or more 'clauses.'
A clause consists of a header and a 'suite.'
The clause headers of a particular compound statement are all at the same indentation level.
Each clause header begins with a uniquely identifying keyword and ends with a colon.
A suite is a group of statements controlled by a clause.
A suite can be one or more semicolon-separated simple statements on the same line as the header,
following the header's colon, or it can be one or more indented statements on subsequent lines.
Only the latter form of a suite can contain nested compound statements.
"""

# Illegal compound statement.
print "\nExample 4: Compound statements with multiple headers. Check the code!"

x = "This is an illegal statement!"
test1 = "illegal" in x
test2 = "statement" in x
# if test1: if test2: print(x)
print "i. This statement is illegal: >>> if test1: if test2: print(x)"
print "The problem is that it is not clear which if statement a subsequent else would belong to."


print "\nExample 5: Compound statements on one line or two! Check the code!"
print "These next two compound statements produce the same result, " + \
      "even though the first takes one line and the second takes two."
x = 25
if 21 <= x < 30: print "You are eligible for our lowest cost life insurance!"

if 21 <= x < 30:
    print "You are eligible for our lowest cost life insurance!"

print "\nExample 6: A compound statements using fwer lines than normal."
grade = 75; letterGrade = "";

if grade >= 90:   letterGrade = "A"
elif grade >= 80: letterGrade = "B"
elif grade >= 70: letterGrade = "C"
elif grade >= 60: letterGrade = "D"
else:             letterGrade = "F"

print "Your number grade of %d results in an %s." % (grade, letterGrade)