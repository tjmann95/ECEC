import time
import random


print "EXERCISES Part 2 of Review - Loops!"
print "You can learn more about loops here: http://www.learnpython.org/en/Loops"

# Part B: For loops.

# EXERCISES for Part 2

# 1. Print out this sequence, using a for loop and the range method.
# You can get more help on range() with the command below. Just uncomment it.
# help(range)

print "\n1. Print this sequence using range(n): \t\t0 1 2 3 4"
print '\tAnswer:\t',

# Add your code for exercise 1 here.



print "\n\n2. Print this sequence of squares using range(m, n): \t\t4 9 16 25"
print '\tAnswer:\t',

# Add your code for exercise 2 here.




print "\n\n3. Print this sequence of odd numbers using range(start, stop, step): \t\t11 13 15 17 19"
print '\tAnswer:\t',
# Add your code for exercise 3 here.




print "\n\n4. Using a for loop, print this pattern."
pattern = """
*
**
***
****
*****"""
print pattern

print '\tAnswer:\t',
# Add your code for exercise 4 here. You must generate the pattern using string multiplication.
# Do not use the pattern provided above in your code. That is just to illustrate the question.



print "\n\n5. Using a for loop, print this pattern."
pattern = """
    *
   ***
  *****
 *******
*********
"""

print pattern

print '\tAnswer:\t',

# Add your code for exercise 5 here. You must generate the pattern using string multiplication and concatenation.





message6 = """\n\n6. You can also use for loops to step though the items in any iterable object such as a string, list or tuple.
Here is a list of the days of the week. """

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print message6
print days
print "Using a for loop, print out the five days that Joe works (Monday - Friday) and pay him $1000 dollars for each day worked."
print '\tAnswer:\t'

print "\nJoe completed a full days work on: ",
pay = 0

# Add your code for exercise 6 here. Use a for loop and the range() command.
# Increment his pay by $1000 for each day he worked.





print "\n\n7. Using a while loop, count down from 10 to 0!"
print "Use time.sleep(1), to countdown once each second. Print Blastoff! after the countdown ends. "
count = 10

# Add your code for exercise 7 here. Use a  while and test that count > -1.







print "\n\n8a. Using a for loop with a break statement, find the first cube greater than 1234."
# Add your code for exercise 8a here.



print "8b. Find the first quartic greater than 1234. A quartic is an integer to the fourth power."
# Add your code for exercise 8b here.



# * * * * * * * *  9. BAG OF CANDY * * * * * * * *
print "\n\n9. Consider this representation of a bag of mixed candies as a list obtained using the split() command."
bag_of_candy = ("mint " * 3).split() + ("chocolate " * 4).split()  + ("gumdrop " * 3).split()
print "The bag of candies contains:", bag_of_candy

message9A = """\nA. Joey loves candy, and he loves gumdrops the most! Use a while loop and the pop() command so,
Joey eats the gumdrops first. Note bag_of_candy is a list. Your code should assume that the gumdrops are
the last items added to the list so that pop() works just fine. Do not use a for loop.
"""
print message9A
# 9A. Add your while loop here and pop() statement here.
# Create output similar to that shown in the PDF with instructions.



print "Oh, ... no more gumdrops left!", bag_of_candy

message9B = """\nB. Joey loves mints more than chocolates. Use another while loop and the remove() command
to help Joey gobble up all the mints. Do not use a for loop.
"""
print message9B
# 9B. Add a second while loop here and remove() each mint, until no mints are left.





print "Oh, ... no more mints left!", bag_of_candy




message9C = """\nC. Use the exact while header below, to help Joey polish off all the chocolates.
He just keeps popping candies, until the bag is empty. """
print message9C

# 9C. Complete the while loop here and pop() until the bag of candy is empty.


print "Oh, ... no more candies left!", bag_of_candy




# D. Eat another bag of candies using a while loop nested inside a for loop.

print "\n\nD. Let's start over  with a new ordered bag of candies. Joey is still hungry!"
print "But now, scramble the order using the shuffle command from the random module."

bag_of_candy = ("mint " * 3).split() + ("chocolate " * 4).split()  + ("gumdrop " * 3).split()
random.shuffle(bag_of_candy) # shuffles the list in place. Non-type command.
print bag_of_candy # now the candies are in random order.

# Use a while loop, nested in a for loop to eat all the candies in Joey's favorite order.
# Use the remove command instead of pop. Output should be identical to the above approach.
favorite_candies = ["gumdrop", "mint", "chocolate"]


# Add a for loop to step through Joey's list of favorite candies.
# Place a while loop inside the for loop.