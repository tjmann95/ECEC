from Tkinter import *
from lunardate import *
import datetime
# Can only deal with years from 1900 to 2049 (in chinese calendar).


root = Tk()
root.title("Chinese Zodiac Calculator")
root.minsize(500,500)


""" A menubutton is the part of a drop-down menu that stays on the screen all the time.
Every menubutton is associated with a Menu widget that can display the choices for that menubutton
when the user clicks on it."""

# Row # 0
intro = "1. Enter your western birth date to find your Chinese zodiac animal sign.\n"
intro += "2. Then press OK to see your zodiac sign!"

Label(root, text=intro, pady=10, justify=LEFT).grid(row=0, column=0,columnspan=3, sticky=W)

# Default values for the birthdate. These are updated when the user enters their data.
birth_year = 2000
birth_month = 1
birth_day = 1

# Row # 1
Label(root, text="Select Year").grid(row=1, column=0, sticky=W)

year_menu_button = Menubutton(root, text='Year', relief='raised', padx=2, pady=2)
year_menu_button.grid(row=1, column=1, sticky=W)

year_indicator = Label(root, text="Year: None", bg="gold", width=20)
year_indicator.grid(row=1, column=2, columnspan=2)
year_menu = Menu(year_menu_button, tearoff=1) # Tearoff menus supported on Unix. But not on some other platforms.

def update_year(year):
    global birth_year
    year_indicator.configure(text=year)
    birth_year = year
    print "You were born in the year %d, using the Western calendar." % year


year_list = range(1900,2050)
for year in year_list:
    # m.add_command(label='Option %s' % (i), command=lambda i=i: callback(i))
    year_menu.add_command(label=year, command=lambda year=year: update_year(year))
    # year_menu.add(year_list[i])
year_menu_button.configure(menu=year_menu)



# Add your code for Row # 2 here.
# It is very similar to the code for row #1, except months replace years.
Label(root, text="Select Month").grid(row=2, column=0, sticky=W)

month_menu_button = Menubutton(root, text="Month", relief="raised", padx=2, pady=2)
month_menu_button.grid(row=2, 1, sticky=W)

month_indicator = Label(root, text="Month: None", bg="gold", width=20)
month_indicator.grid(row=2, column=2, columnspan=2)
month_menu = Menu(month_menu_button, tearoff=1)

def update_month(month):
    global birth_month
    month_indicator.configure(text=month)
    birth_month = month
    print "You were born in the month %d, using the Western calendar." % month

month_list = range(1, 13)
for month in month_list:
    month_menu.add_command(label=year, command=lambda month=month: update_month(month))
month_menu_button.configure(menu=month_menu)




# Add your code for Row # 3 here.
# It is very similar to the code for row #1, except days replace years.
Label(root, text="Select Day").grid(row=3, column=0, sticky=W)

day_menu_button = Menubutton(root, text="Day", relief="raised", padx=2, pady=2)
day_menu_button.grid(row=3, column=1, sticky=W)

day_indicator = Label(root, text="Day: None", bg="gold", width=20)
day_indicator.grid(row=3, column=2, columnspan=2)
day_menu = Menu(day_menu_button, tearoff=1)


def update_day(day):
    global birth_day
    day_indicator.configure(text=day)
    birth_day = day
    print "You were born on the day %d, using the Western calendar." % day


day_list = range(1, 32)
for day in day_list:
    day_menu.add_command(label=day, command=lambda day=day: update_day(day))
day_menu_button.configure(menu=day_menu)







def calculate():
    print "\nOK, you have entered that your birthday in the Western calender is:", birth_year, birth_month, birth_day
    birthdate_western = datetime.date(birth_year, birth_month, birth_day)
    birthdate_chinese = LunarDate.fromSolarDate(birth_year, birth_month, birth_day)
    print "Your birth date in the Chinese calender is: ", birthdate_chinese
    chinese_year = birthdate_chinese.year
    index = (chinese_year - 1900) % 12
    zodiac_animal = "Rat,Ox,Tiger,Rabbit,Dragon,Snake,Horse,Goat,Monkey,Rooster,Dog,Pig".split(',')
    print "Your Chinese zodiac animal is the:", zodiac_animal[index]
    answer_label.configure(text="Your zodiac sign is the: " + zodiac_animal[index])

# Row # 4
Label(root, text="Zodiac Animal", pady=10).grid(row=4, column=0, sticky=W)

answer_label = Label(root, text="Your sign will appear here.", bg="beige", width=40)
answer_label.grid(row=4, column=1, columnspan=2)

ok_button = Button(root, text="OK", command=calculate)
ok_button.grid(row=4, column=3)

# Row # 5
zodiac_image = PhotoImage(file = "images/zodiac.gif")
Label(root, image=zodiac_image).grid(row=5, column=0, columnspan=4)
root.mainloop()