from Tkinter import *

import math
root = Tk()
# root.minsize(500,400)
root.title("Function Calculator")

""" A menubutton is the part of a drop-down menu that stays on the screen all the time.
Every menubutton is associated with a Menu widget that can display the choices for that menubutton
when the user clicks on it."""


# Row # 0
Label(root, text="1. Enter x.").grid(row=0, column=0)
x_widget = Entry(root, justify=CENTER)
x_widget.grid(row=0, column=1)

# Radio buttons to specify radians or degrees for the trig functions only.
v = IntVar()
radians_button = Radiobutton(root, text="Radians", variable=v, value=0)
radians_button.grid(row=0, column=2)

degrees_button = Radiobutton(root, text="Degrees", variable=v, value=1)
degrees_button.grid(row=0, column=3)
degrees_button.select()  # Program starts with this radio button selected.

# Row # 1
Label(root, text="2. Select function f.").grid(row=1, column=0)

my_menu_button = Menubutton(root, text='Select Function', relief='raised', padx=2, pady=2)
my_menu_button.grid(row=1, column=1)

selected_function_indicator = Label(root, text="Function: None", bg="gold", width=20)
selected_function_indicator.grid(row=1, column=2, columnspan=2)

function_menu = Menu(my_menu_button)

def calculate(i):
    func = function_list[i]
    try:                    # Handle input for univariate functions.
        x = float(x_widget.get())
    except Exception as e:  # Likely user has provided a tuple for a bivariate function.
        x_tuple =  x_widget.get()
        n = x_tuple.find(',')
        x = float( x_tuple[:n])
        y = float( x_tuple[n+1:])

    print '\nSelected function:', function_list[i]
    print 'Selected x value:', x

    if func == "sin":
        # Indicate the selected function in the label named selected_function_indicator.
        selected_function_indicator.config(text="Function: " + func)

        if v.get() == 1:        # angle x was entered in degrees.
            x = math.radians(x) # Convert x from degrees to radians
        result = math.sin(x)
        print "The result is:", result
        result_widget.delete(0, END)
        result_widget.insert(0, result)

    if func == "sqrt":
        # Indicate the selected function in the label named selected_function_indicator.
        selected_function_indicator.config(text="Function: " + func)

        result =  math.sqrt(x)
        print "The result is:", result
        result_widget.delete(0, END)
        result_widget.insert(0, result)

    if func == "exp":
        # Indicate the selected function in the label named selected_function_indicator.
        selected_function_indicator.config(text="Function: " + func)

        result =  math.exp(x)
        print "The result is:", result
        result_widget.delete(0, END)
        result_widget.insert(0, result)

    if func == "pow":  # A bivariate example
        # Indicate the selected function in the label named selected_function_indicator.
        selected_function_indicator.config(text="Function: " + func)

        result =  math.pow(x, y)
        print "The result is:", result
        result_widget.delete(0, END)
        result_widget.insert(0, result)


     # Add if blocks here for each new function!



function_list = ["sin", "cos", "tan", "sqrt", "exp"]  # <-- Add function names here.
n = len(function_list)
for i in range(0,n):
    # m.add_command(label='Option %s' % (i), command=lambda i=i: callback(i))
    function_menu.add_command(label=function_list[i], command=lambda i=i: calculate(i))

my_menu_button.configure(menu=function_menu)

"""
Note the use of i = i. This provides a snapshot of i at the time when each function object is created .
If you leave out 'i=i' from this example, then things don't work correctly.
Each menu command ends up processing the same value - the final value of the loop variable.
"""

# Row # 2
Label(root, text="3. Result y = f(x).").grid(row=2, column=0)

result_widget = Entry(root, justify=CENTER)
result_widget.grid(row=2, column=1)


root.mainloop()