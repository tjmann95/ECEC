# Alert! Importing from __future__ must be at the very top!
from Tkinter import *

import random
# The order of the next two imports makes a critical difference.
from math import *
from cmath import *


def evaluate(event):
    # Define i and j to both be the complex square root of minus 1 here.
    j = complex(0, 1)
    i = complex(0, 1)

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
        result_entry_widget.delete(0, END)
        result_entry_widget.insert(0, e)
        result_entry_widget.configure(bg="red")
        root.after(2000, result_entry_widget.configure, {"bg": "white"})

# Append at least 20 new examples to  example_list here.
example_list = []
example_list.append("2 * sin(pi/2) * cos(pi/2)")
example_list.append("log(e**2)")
example_list.append("log(1000*1000, 10)")
example_list.append("max([1, 2, 3, 4])")
example_list.append("min([1, 2, 3, 4])")
example_list.append("gamma(5)")
example_list.append("atan(1)")
example_list.append("asin(1)")
example_list.append("floor(1.999)")
example_list.append("ceil(1.999)")
example_list.append("11 % 3")
example_list.append("tan(5)")


def clear():
    print "The clear button was pressed."
    # Add code to delete the text in the two entry widgets.
    result_entry_widget.delete(0, END)
    expression_entry_widget.delete(0,END)


def show_example():
    print "Example button pressed."
    example = random.choice(example_list)
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
clear_button = Button(root, {"text": "Clear"}, command=clear)
clear_button.grid(row=3, column=0)

root.mainloop()