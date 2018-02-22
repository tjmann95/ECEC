
# Example 2 - Getting the strings of code from a file.
# The hacker will taunt you by dynamically executing the code to print his poem.

print "\n\nExample 2 - Getting the strings of code from a file."
print "The hacker will taunt you by dynamically executing the code to print his poem."

hackers_file_name = "hackers_poem.py"  # File with the hacker's code.

# The code below, merely prints out the hacker's actual code.
# Note it still includes the print statements, so these instructions have not been executed.
# Make a small adjustment, so each instructions is actually executed.
# You should see the final complete poem, minus the print statements.
print "Here is the hacker's code.\n"
theFile = open(hackers_file_name, "r")
for line in theFile:
    print line[:-1]  # Each line ends with a carriage return, which has been stripped away using [:-1]
theFile.close()

print "\n\nNow YOU are the hacker, and you will execute your code to taunt a victim with your snarly poem."
print "Just use 'exec' to execute each string of code."
print "Add a for loop now.\n\n"

# Make a copy of the for loop here, but this time dynamically execute each line using exec!
# You don't need to strip of the carriage return here with [:-1]. It's optional.
# Add for loop here and execute each line of code!
theFile = open(hackers_file_name, "r")
for line in theFile:
    exec line[:-1]  # Each line ends with a carriage return, which has been stripped away using [:-1]
theFile.close()

print "\nExample 3 - Deleting your malware!"

message = """The hacker does not wish to leave any trace of their malware, \nafter their diabolical poem has been printed.
Add some new lines to the end of the code in the file hackers_poem.py \nso that the file will be deleted
after it has been executed. A second copy has been given, in hackers_poem2.py so you can safely delete one,
and still have the other to reproduce this activity later. """

print message
hint = """\n\nThe os module contains the method remove()
If the file is in the current working directory, you can just import os
then remove/delete a specified file without adding additional folder info:
os.remove(file_name)"""

print hint
# Here again is the name for the hacker's file.
hackers_file_name = "hackers_poem.py"

# Delete the file here, or place the instructions in the poem file itself.
# On some systems, only one of these methods will work.


