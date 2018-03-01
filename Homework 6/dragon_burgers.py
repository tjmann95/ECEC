from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()  # Sometimes we call the top window 'root' instead.
top.minsize(500,300)
top.title("Dragon Burgers")

intro = "Select all the condiments for your Delicious Dragon Burger using this simple menubutton.\n"
intro += "Press OK to submit your order."

dragon_image = PhotoImage(file="images/DragonBurger.gif")


Label(top, text = intro, justify=LEFT).grid()
Label(top, image = dragon_image).grid()

def place_order():
    condiments = "Dragon Burger with: "
    if mayoVar.get(): condiments += "Mayonnaise "
    if ketchVar.get(): condiments += "Ketchup "
    if tabascoVar.get(): condiments += "Tabasco Sauce "
    # Add more if statements here. One for each spicy topping.
    if hot1var.get(): condiments += "Hot 1 "
    if hot2var.get(): condiments += "Hot 2 "
    if hot3var.get(): condiments += "Hot 3 "
    if hot4var.get(): condiments += "Hot 4 "
    if hot5var.get(): condiments += "Hot 5 "


    display_condiments.delete(0, END)
    display_condiments.insert(0, condiments)
    message_label.configure(text="Enjoy your delicious Dragon Burger!!")

mb=  Menubutton ( top, text="Condiments", relief=RAISED, padx=2, pady=2 )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

mayoVar  = IntVar()
ketchVar = IntVar()
tabascoVar = IntVar()

# Add more IntVar() declarations here. One for each spicy topping.
hot1var = IntVar()
hot2var = IntVar()
hot3var = IntVar()
hot4var = IntVar()
hot5var = IntVar()

mb.menu.add_checkbutton ( label="Mayonnaise",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="Ketchup",
                          variable=ketchVar )
mb.menu.add_checkbutton ( label="Tabasco Sauce",
                          variable=tabascoVar )


# Add more checkbuttons here. One for each spicy topping.
mb.menu.add_checkbutton(label="Hot 1", variable=hot1var)
mb.menu.add_checkbutton(label="Hot 2", variable=hot2var)
mb.menu.add_checkbutton(label="Hot 3", variable=hot3var)
mb.menu.add_checkbutton(label="Hot 4", variable=hot4var)
mb.menu.add_checkbutton(label="Hot 5", variable=hot5var)




mb.grid()

display_condiments = Entry(top,justify=CENTER, width = 40 )
display_condiments.grid()

ok_button = Button(top, text="OK", command = place_order).grid(row=3, column=2, sticky=W)

message_label = Label(top, text = "Please select your condiments.")
message_label.grid(row=4)

top.mainloop()