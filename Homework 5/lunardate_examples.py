import datetime

from lunardate import *
print "Alert: This library can only deal with years from 1900 to 2049 (in the chinese calendar).\n"

print "1. Example to convert the  western date (1976, 10, 1); year, month, day to a Chinese lunar date."
print LunarDate.fromSolarDate(1976, 10, 1), "\tYes, it's a leap month in the Chinese calender!"
print "This returns LunarDate(1976, 8, 8, 1), in which the four arguments are year, month, day and isLeapMonth."
print "The latter returns a 1 or a 0. "

print "\n2. Convert the Chinese date LunarDate(1976, 8, 8, 1) back to the western calender."
print "In the western calender this is the same as:", LunarDate(1976, 8, 8, 1).toSolarDate()



print "\n3. Find today's date in the western and the Chinese calender. "
print "Using the western calender, today is: ", datetime.date.today()  # The western date for today.
print "Using the Chinese calender, today is: ", LunarDate.today()      # The Chinese date for today.

print "\n4. Find future Chinese New Years"
print "This year, the Chinese New Year was on:       ",   LunarDate(2016, 1, 1, 0).toSolarDate()
print "Next year, the Chinese New Year will be on on:",   LunarDate(2017, 1, 1, 0).toSolarDate()
print "In 2018,   the Chinese New Year will be on on:",   LunarDate(2018, 1, 1, 0).toSolarDate()


print "\n5. Chinese dates for significant holidays this year. Note dates vary regionally. "
print "In 2016, Easter falls on March 27th, or in the Chinese calendar:          ",  LunarDate.fromSolarDate(2016, 3, 27)
print "In 2016, Passover starts on April 22nd, or in the Chinese calendar:       ",  LunarDate.fromSolarDate(2016, 4, 22)
print "In 2016, Eid al-Adha starts on September 12th, or in the Chinese calendar:", LunarDate.fromSolarDate(2016, 9, 12)

print "\n6. Find today in the Chinese calendar, and extract the components: year, month, day and isLeapMonth."
today = LunarDate.today()
print "Using the Chinese calender, today is: ", today     # The Chinese date for today.
print "Today, the Chinese year is: ", today.year          # The Chinese year for today.
print "Today, the Chinese month is: ", today.month        # The Chinese month for today.
print "Today, the Chinese day  is: ", today.day           # The Chinese day for today.
print "Is today in a Chinese leap month?", today.isLeapMonth

