__author__ = 'robincarr'

# 1. Import all of the Toolkit Interface using the keyword from.
from Tkinter import *

# 2. Construct a top-level window named root.
root = Tk()


# 3. Set the title of the root window to "Wye-Delta Resistor Calculator"
root.title("Wye-Delta Resistor Calculator")

def clear(widget):
    widget.config(state=NORMAL)
    widget.delete(0,END)

def clear_all():
    resistor_list = [resistor1, resistor2, resistor3, resistora, resistorb, resistorc]
    for widget in resistor_list:
        clear(widget)
    # Now all widgets are in state=NORMAL. Not what we want.
    # Activate only those chosen by the selected radio button.
    value = v.get()
    if value == 1:
        wye_to_delta_GUI()
    else:
        delta_to_wye_GUI()


def wye_to_delta_GUI():
    resistor1.config(state=NORMAL)
    resistor2.config(state=NORMAL)
    resistor3.config(state=NORMAL)

    resistora.config(state=DISABLED)
    resistorb.config(state=DISABLED)
    resistorc.config(state=DISABLED)


def delta_to_wye_GUI():
    resistora.config(state=NORMAL)
    resistorb.config(state=NORMAL)
    resistorc.config(state=NORMAL)

    resistor1.config(state=DISABLED)
    resistor2.config(state=DISABLED)
    resistor3.config(state=DISABLED)

def check_then_calculate():
    try:
        calculate()
    except ValueError as e:
        print 'First enter the resistor values, then press the Calculate button!'
        print 'The exception type is:', type(e)
        alert_message_widget.config(state=NORMAL)
        alert_message_widget.delete(0, END)
        alert_message_widget.insert(0, 'First enter the resistor values, then press the Calculate button!')
        change_color(alert_message_widget, 3*2)

    except ZeroDivisionError as e:
        print 'Resistors cannot be ZERO. Enter non-zero values only!'
        print 'The exception type is:', type(e)
        alert_message_widget.config(state=NORMAL)
        alert_message_widget.delete(0, END)
        alert_message_widget.insert(0, 'Resistors cannot be ZERO. Enter non-zero values only!')
        change_color(alert_message_widget, 3*2)

    except AssertionError as e:
        print 'Resistors  must be positive. Enter positive values only!'
        print 'The exception type is:', type(e)
        alert_message_widget.config(state=NORMAL)
        alert_message_widget.delete(0, END)
        alert_message_widget.insert(0, 'Resistors  must be positive. Enter positive values only!')
        change_color(alert_message_widget, 3*2)



def calculate():
    # First find out which radio button is selected.
    value = v.get()
    print '\nRadio button #%d selected: ' % value
    if value == 1:
        print 'Transforming from wye to delta.'
        r1 = float( resistor1.get() )
        r2 = float( resistor2.get() )
        r3 = float( resistor3.get() )
        assert r1 >= 0
        assert r2 >= 0
        assert r3 >= 0

        # Compute the equivalent delta resistors
        # Let's first define the product P as follows.
        P = r1*r2 + r1*r3 + r2*r3
        ra = P/r1
        rb = P/r2
        rc = P/r3
        # Display the results
        resistora.config(state=NORMAL) # Need to adjust the state so we can write to it.
        resistora.delete(0,END)
        resistora.insert(0,ra)

        resistorb.config(state=NORMAL) # Need to adjust the state so we can write to it.
        resistorb.delete(0,END)
        resistorb.insert(0, rb)

        resistorc.config(state=NORMAL) # Need to adjust the state so we can write to it.
        resistorc.delete(0,END)
        resistorc.insert(0, rc)


    if value == 2:
        print 'Transforming from delta to wye.'
        ra = float( resistora.get() )
        rb = float( resistorb.get() )
        rc = float( resistorc.get() )
        assert ra >= 0
        assert rb >= 0
        assert rc >= 0

        # Compute the equivalent wye resistors
        # Let's first define the sum S as follows.
        S = ra + rb + rc
        r1 = round(rb*rc / S, 6)
        r2 = round(ra*rc / S, 6)
        r3 = round(ra*rb / S, 6)
        # Display the results
        resistor1.config(state=NORMAL) # Need to adjust the state so we can write to it.
        resistor1.delete(0,END)
        resistor1.insert(0,r1)

        resistor2.config(state=NORMAL) # Need to adjust the state so we can write to it.
        resistor2.delete(0,END)
        resistor2.insert(0,r2)

        resistor3.config(state=NORMAL) # Need to adjust the state so we can write to it.
        resistor3.delete(0,END)
        resistor3.insert(0,r3)

def reset_feedback():
    alert_message_widget.config(background=default_background)
    alert_message_widget.delete(0, END)
    alert_message_widget.config(state=DISABLED)

# Original  version which flashes the specified widget forever.
def change_color(my_widget):
    current_color = my_widget.cget("background")
    next_color = "red" if current_color == "green" else "green"
    my_widget.config(background=next_color)
    root.after(250, change_color, my_widget )


# Improved version which will change color n times, instead of forever.
def change_color(my_widget, n):
    if n==0:
        root.after(2000, reset_feedback)  # Wait 2 seconds, then clear the feedback message.
    else:
        current_color = my_widget.cget("background")
        next_color = "red" if current_color == "yellow" else "yellow"
        my_widget.config(background=next_color)
        root.after(250, change_color, my_widget , n-1)


# Now add labels for the two images.
Label(root, text="Wye Resistor Configuration").grid(row=0, column=0, columnspan=2)
Label(root, text="Delta Resistor Configuration").grid(row=0, column=2, columnspan=2)

image1 = PhotoImage(file = "images/wye_resistor_configuration.gif")
image2 = PhotoImage(file = "images/delta_resistor_configuration.gif")

Label(root, image = image1).grid(row=1, column=0, columnspan=2)
Label(root, image = image2).grid(row=1, column=2, columnspan=2)

Label(root, text="Select Transform").grid(row=2, column=0)

# We'll use radio buttons to select the direction of the transform.
v = IntVar()

radiobutton1 = Radiobutton(root, text="Wye -> Delta", variable=v, value=1, command = wye_to_delta_GUI)
radiobutton1.grid(row=2, column=1)
radiobutton1.select()

radiobutton2 = Radiobutton(root, text="Delta -> Wye", variable=v, value=2, command = delta_to_wye_GUI)
radiobutton2.grid(row=2, column=2)

# Now add Labels and Entry widgets for all 6 resistors.
Label(root, text="Resistor 1").grid(row=3, column=0)
Label(root, text="Resistor 2").grid(row=4, column=0)
Label(root, text="Resistor 3").grid(row=5, column=0)

Label(root, text="Resistor a").grid(row=3, column=2)
Label(root, text="Resistor b").grid(row=4, column=2)
Label(root, text="Resistor c").grid(row=5, column=2)

# Finish this line to construct the Entry widget named resistor1, and assure its text will be centered.
# Do not place it in the grid yet.
resistor1 = Entry(root, justify=CENTER)
resistor1.grid(row=3, column=1)  # Now place it in the grid in row #3 and column #1.

resistor2 = Entry(root, justify=CENTER)
resistor2.grid(row=4, column=1)

resistor3 = Entry(root, justify=CENTER)
resistor3.grid(row=5, column=1)


resistora = Entry(root, justify=CENTER, state=DISABLED)
resistora.grid(row=3, column=3)

resistorb = Entry(root, justify=CENTER, state=DISABLED)
resistorb.grid(row=4, column=3)

resistorc = Entry(root, justify=CENTER, state=DISABLED)
resistorc.grid(row=5, column=3)

calculate_button = Button(root, text="CALCULATE", command=check_then_calculate)
calculate_button.grid(row=6, column=2)

clear_button = Button(root, text="CLEAR", command=clear_all)
clear_button.grid(row=6, column=3)

# Add a widget to display error messages and alerts.
Label(root, text='Feedback' ).grid(row=7, column=0)
alert_message_widget = Entry(root, justify=CENTER, state=DISABLED, width=60)
alert_message_widget.grid(row=7, column=1, columnspan=3)
default_background = alert_message_widget.cget("background")
print default_background
# Call the main event loop of the root window.
root.mainloop()