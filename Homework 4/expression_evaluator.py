# Alert! Importing from __future__ must be at the very top!
from Tkinter import *

import random
# The order of the next two imports makes a critical difference.
from cmath import *
from math import *


def evaluate(event):
    # Define i and j to both be the complex square root of minus 1 here.


    try:
        answer = eval(expression_entry_widget.get())
        result_entry_widget.delete(0, END)
        result_entry_widget.configure(bg="gold")
        result_entry_widget.insert(0, str(answer) )
        root.after(2000, result_entry_widget.configure, {"bg": "white"} )
    except Exception as e:
        print repr(e)
        # Add code here to display the error message in result_entry_widget.
        # Change the background to red instead of gold to signal an error.


# Append at least 20 new examples to  example_list here.
example_list = []
example_list.append("2 * sin(pi/2) * cos(pi/2)")



def clear():
    print "The clear button was pressed."
    # Add code to delete the text in the two entry widgets.
    result_entry_widget.delete(0, END)
    expression_entry_widget.delete(0,END)


def show_example():
    print "Example button pressed."
    example = "2 * sin(pi/2) * cos(pi/2)"
    # Add code here to instead choose example at random from example_list.

    expression_entry_widget.delete(0, END)
    expression_entry_widget.insert(0, example)
    evaluate("<Return>")


root = Tk()
root.title("Golden Dragon Ring Calculator")
root.minsize(500,400)

background_image = PhotoImage(file = "images/DragonAbacusRing3.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

print root.attributes()# root.attributes("-transparent", 0.5)

robot1 = PhotoImage(file="images/robot_calculator.gif")


Label(root, text="Enter Expression:").grid(row=0, column=0, padx=100)
expression_entry_widget = Entry(root, justify=CENTER, width=40)
expression_entry_widget.bind("<Return>", evaluate)
expression_entry_widget.grid(row=0, column=1)


# Label(root, image=robot1).grid(row=0, column=2, rowspan=3)


Label(root, text="Result").grid(row=1, column=0)
result_entry_widget = Entry(root, justify=CENTER, width=40)
result_entry_widget.grid(row=1, column=1)


example_button = Button(root, {"text":"Example"}, command=show_example)
example_button.grid(row=2, column=0)


# Add and place the clear_button here.

root.mainloop()