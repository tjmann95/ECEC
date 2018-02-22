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


