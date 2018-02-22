# Alert! Importing from __future__ must be at the very top!
from __future__ import division    # Uncomment this line for traditional python division. That is 3/2 = 1.


from Tkinter import *

import random
from math import *    # Reverse the order of the math and cmath imports to "turn off" most complex functions.
from cmath import *



def evaluate(event):
    i = complex(0,1)
    j = complex(0,1)

    # i. Add code here to get() the string from symbol_widget.
    # Replace the stub below.
    code_string = symbol_widget.get()

    # ii. Use compile() to compile the code string and mame the result code_object
    code_object = compile(code_string)
    # iii. Apply exec to the code object.
    exec code_object

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
        result_entry_widget.configure(bg="red")
        result_entry_widget.insert(0, repr(e) )
        root.after(2000, result_entry_widget.configure, {"bg": "white"} )


# Append at least 20 new examples to  example_list here.
example_list = []
example_list.append("2 * sin(pi/2) * cos(pi/2)")
example_list.append("log(8,2)")
example_list.append("pi")
example_list.append("log(e**2)")
example_list.append("(1-pi**2)/(1+pi**2)")

example_list.append("11 % 3")
example_list.append("-11 % 3")
example_list.append("11 % -7")
example_list.append("log(10**6, 10)")
example_list.append("ceil(1.234)")

example_list.append("floor(1.999)")
example_list.append("max(4, 3, 2, 1, 100)")
example_list.append("min(8, 0, -8, 2)")
example_list.append("sqrt(pi)")
example_list.append("atan(1)")

example_list.append("factorial(4)")
example_list.append("gamma(0.5)")
example_list.append("gamma(5.0)")
example_list.append("tan(pi/4)")
example_list.append("lgamma(100)")

example_list.append("bin(1024)")
example_list.append("hex(16**4-1)")
example_list.append("int('FF',16)")
example_list.append("int('Drexel',36)")
example_list.append("int( bin(101010),2)")

# Optional complex examples.
# Change to False if you do not want complex examples
if True:  # Decide if you want to add these complex examples or not.
    example_list.append("phase(complex(0,1))")
    example_list.append("sqrt(-1)")
    example_list.append("exp(j*pi)")
    example_list.append("(3+4*j)*(3-4*j)")
    example_list.append("j*j")


def clear():
    print "The clear button was pressed."
    # Add code to delete the text in the two entry widgets.
    result_entry_widget.delete(0, END)
    expression_entry_widget.delete(0,END)


def show_example():
    print "Example button pressed."
    # example = "2 * sin(pi/2) * cos(pi/2)"
    # The above has been replaced with this random expression to calculate.
    example = random.choice(example_list)

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

clear_button = Button(root, {"text":"Clear"}, command=clear)
clear_button.grid(row=3, column=0)

Label(root, text="Define symbols below.").grid(row=4, column=0, sticky = W)
symbol_widget = Entry(root, justify=CENTER, width=20)
symbol_widget.grid(row=5, column=0, sticky=W)

symbol_widget.insert(0, "a = 1; b = 2;")

# root.after(15000, root.destroy)
root.mainloop()