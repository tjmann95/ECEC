from Stack import *
import copy


# Custom method to check for equality of stacks.
def equals_with_details(stack1, stack2):
    while True:
        try:
            ch1 = stack1.peek()
            ch2 = stack2.peek()
            if stack1.pop() != stack2.pop():
                print "%s !=  %s" % (ch1, ch2)
                return False
            else:
                print "%s  =  %s" % (ch1, ch2)

        except IndexError:
            return True


# Fix this stub method to test if two stacks are equal.
def equals(stack1, stack2):
    return stack1.items == stack2.items


print "PALINDROME CHECKER\n"


# 1. Enter the test phrase to check if it is a palindrome.
phrase = "Madam, I'm Adam"
phrase = "Stack Cats!"

while True:
    # Add a while loop here. Use raw_input() to get a phrase from the user.
    phrase = raw_input("Enter a test phrase: ")  # Overwrites the previous value. Just use commenting to select one or the other.
    phrase = phrase.upper()
    if phrase == "Q":
        print "All done."
        break
    print "The test phrase is: ", phrase

    # 2. Build a stack of letters using just the alphabetical characters, all in upper case.
    letter_stack = Stack()  # Create an empty stack.
    for character in phrase:
        if character.isalpha():  # Ignore any characters that are not letters like spaces, and punctuation marks.
            letter_stack.push(character)
    print "The first stack is:\t\t", str(letter_stack)

    # 3. Create a second stack in the reverse order. Must use copy.deepcopy() and not just copy.copy()
    duplicate = copy.deepcopy(letter_stack)  # A temporary copy, which will be exhausted by popping to create the reverse stack.
    reverse_stack = Stack() # Create a new empty stack.
    while not duplicate.isEmpty():
        next_letter = duplicate.pop()
        reverse_stack.push(next_letter)
    print "The reversed stack is:\t", str(reverse_stack)


    # Now we need to check if the original stack of letters and the reverse stack are equal.
    # If they are, we have a palindrome.
    print "\nComparing letters forwards versus backwards."


    method1 = equals_with_details(letter_stack, reverse_stack)

    # Use your own equals() method here.
    method2 = equals(letter_stack, reverse_stack)
    # Add if/else blocks to print out appropriate Yes or NO messages.
    if method1 or method2:
        print "Yes, the phrase is a palindrome."
    else:
        print "No, the phrase is not a palindrome."