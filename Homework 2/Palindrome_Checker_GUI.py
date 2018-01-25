from Tkinter import *
from Stack import Stack
import copy


# Flashes a widget, typically as a warning or to get attention.
def flash(my_widget, n): # Typically n = 2k will be even to give k complete cycles.
    if n == 0:
        root.after(2000, clear_result)  # Wait 2 seconds, then clear the error message.
        my_widget.config(bg="white")
    else:
        current_color = my_widget.cget("background")
        next_color = "red" if current_color == "yellow" else "yellow"
        my_widget.config(background=next_color)
        root.after(250, flash, my_widget , n-1)


# Method to check if two stacks are the same.
# This version does not consume  the stacks, but instead makes duplicates first.
def stack_equals(stack1, stack2):
    stack1_copy = copy.deepcopy(stack1)
    stack2_copy = copy.deepcopy(stack2)

    while True:
        try:
            ch1 = stack1_copy.peek()
            ch2 = stack2_copy.peek()
            if stack1_copy.pop() != stack2_copy.pop():
                print "%s!= %s" % (ch1, ch2)
                return False
            else:
                print "%s = %s" % (ch1, ch2)

        except IndexError:
            return True

def clear_result():
    test_results_widget.delete(0,END)
    test_results_widget.config(state=DISABLED)


def check_palindrome():
    global stack_of_example_palindromes
    # 1. Get the user's test phrase.
    phrase = test_phrase_widget.get().upper()

    # 2. Build a stack of letters using just the alphabetical characters, all in upper case.
    letter_stack = Stack() # Create an empty stack.
    for character in phrase:
        if character.isalpha():
            letter_stack.push(character)
    print 'Forward:', letter_stack

    # 3. Create a second stack in the reverse order. Must use copy.deepcopy() and not just copy.copy()
    duplicate = copy.deepcopy(letter_stack)  # A temp copy, which will be exhausted by popping to create the reverse stack.
    reverse_stack = Stack() # Create a new empty stack.
    while not duplicate.isEmpty():
        next_letter = duplicate.pop()
        reverse_stack.push(next_letter)
    print 'Reverse:', reverse_stack

    # 4. Check if the forward and reverse stacks of letters are equal.
    is_palindrome = stack_equals(letter_stack, reverse_stack)
    test_results_widget.config(state=NORMAL)
    test_results_widget.delete(0,END)
    if is_palindrome:
        test_results_widget.insert(0,"Yes! It's a palindrome!")
        if letter_stack not in stack_of_example_palindromes:
            stack_of_example_palindromes.push(letter_stack)
    else:
        test_results_widget.insert(0,"Not a palindrome!")
    flash(test_results_widget, 8)


# Complete this stub.
def print_to_console():
    global stack_of_example_palindromes
    stack_copy = copy.deepcopy(stack_of_example_palindromes)

    for item in stack_copy.items:
        print item

def show_random_palindrome():
    try:
        example = stack_of_example_palindromes.pop()
    except Exception as e:
        print e
        example = "Madam, I'm Adam!"
    test_phrase_widget.delete(0,END)
    test_phrase_widget.insert(0,example)


root = Tk()
root.title("Palindrome Checker")


stack_of_example_palindromes = Stack()
stack_of_example_palindromes.push("Stack Cats")
stack_of_example_palindromes.push("TacoCat")
# Push at least ten more example palindromes onto the stack of examples here.
# Here is one good source. http://www.palindromelist.net
stack_of_example_palindromes.push("A Santa at Nasa")
stack_of_example_palindromes.push("alula")
stack_of_example_palindromes.push("A but tuba")
stack_of_example_palindromes.push("A car, a man, a maraca")
stack_of_example_palindromes.push("A dog! A panic in a pagoda!")
stack_of_example_palindromes.push("A lad named E. Mandala")
stack_of_example_palindromes.push("A nut for a jar of tuna.")
stack_of_example_palindromes.push("Aerate pet area.")
stack_of_example_palindromes.push("Air an aria.")
stack_of_example_palindromes.push("Aba")

palindrome_image1 = PhotoImage(file="images_for_palindromes/TacoCat.gif")
palindrome_image2 = PhotoImage(file="images_for_palindromes/StackCats.gif")

outside_frame = Frame(root, bg="blue", padx=4, pady = 4)
outside_frame.grid(row=0, column=0, columnspan=4)
# The outside frame merely acts as a blue frame about the GUI.

top_frame = Frame(outside_frame, bg="lightyellow", padx=4, pady = 4)
# top_frame.grid(row=0, column=0, columnspan=4, sticky=NSEW)
top_frame.pack()

# Next, we add frame2 for the control buttons.
bottom_frame = Frame(outside_frame, padx=4, pady = 4, bg="yellow")
# bottom_frame.grid(row=1, column=0, columnspan=4, sticky=NSEW)
bottom_frame.pack(fill=X, anchor=CENTER)

image_label1 = Label(top_frame, bg="black", image = palindrome_image1)
image_label1.grid(row=0, column=0, columnspan=2, sticky=NSEW)
image_label2 = Label(top_frame, bg="black", image = palindrome_image2)
image_label2.grid(row=0, column=2, columnspan=2, sticky=NSEW)

Label(top_frame, text="Test Phrase", bg="lightyellow", fg ="blue").grid(row=1, column=0)
test_phrase_widget = Entry(top_frame, justify=CENTER, width=40)
test_phrase_widget.grid(row=1, column=1, columnspan=3)

Label(top_frame, text="Test Results", bg="lightyellow", fg ="blue").grid(row=2, column=0)
test_results_widget = Entry(top_frame, justify=CENTER, width=40, state=DISABLED)
test_results_widget.grid(row=2, column=1, columnspan=3)

# Add some control buttons
show_button = Button(top_frame, text="Show Random", command = show_random_palindrome)
show_button.grid(row=3, column=0, columnspan=2, sticky=SW)

check_button = Button(top_frame, text="Check", command = check_palindrome)
check_button.grid(row=3, column=2, sticky=W)

print_button = Button(top_frame, text="Print to Console", command=print_to_console)
print_button.grid(row=3, column=3, sticky=E)


root.mainloop()