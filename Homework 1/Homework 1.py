from time import sleep
import sys
import random
import math

# print("PART 1\n")
#
# s = "catfish hatchery"
# print("The first word in " + repr(s) + " is" + repr(s[:3]) + ".\n")
# print("The second word in " + repr(s) + " is " + repr(s[3:7]) + ".\n")
# print("The last word in " + repr(s) + " is " + repr(s[-8:]) + ".\n")
# print("The number of h's in " + repr(s) + " is: " + str(s.count('h')) + "\n")
#
# target = "aeiouAEIOU"
# vowels = 0
# for char in s:
#     if char in target:
#         vowels += 1
#
# print("The number of vowels in " + repr(s) + " is: " + str(vowels) + "\n")
#
# country = "united states of america"
# print(country.capitalize())
# print(country.title())
# print("I live in the " + country.title().replace("O", "o") + ".\n")
#
# word1 = "dogcatcher"
# word2 = "dogfish"
# word3 = "dogberry"
# words = [word1, word2, word3]
#
# dog_start = []
# fish_end = []
# cat_contains = []
# for word in words:
#     if word.startswith("dog"):
#         dog_start.append(word)
#     if word.endswith("fish"):
#         fish_end.append(word)
#     if "cat" in word:
#         cat_contains.append(word)
#
# print("These words start with 'dog': " + " ".join(dog_start))
# print("These words end with 'fish': " + " ".join(fish_end))
# print("These words contain 'cat': " + " ".join(cat_contains) + "\n\n")
#
# print("PART 2\n")
#
# for i in range(5):
#     print(i, end=" ")
#
# print("\n")
# for i in range(2, 6):
#     print(i*i, end=" ")
#
# print("\n")
# for i in range(11, 20, 2):
#     print(i, end=" ")
#
# print("\n")
# for i in range(1, 6):
#     print("*"*i)
#
# print("\n")
# for i in range(5):
#     print(" "*(4 - i) + "*"*(2*i + 1) + "\n")
#
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# workdays = []
# pay = 0
# for i in range(5):
#     workdays.append(days[i])
#     pay += 1000
#
# print("Joe completed a full day's work on: " + " ".join(workdays))
# print("His pay for this week is: $" + str(pay))
#
# # count = 10
# # while count > -1:
# #     sys.stdout.write(str(count) + " ")
# #     sys.stdout.flush()
# #     sleep(1)
# #     count -= 1
# # print("Blastoff!\n")
#
# for i in range(5, 21):
#     if i**3 > 1234:
#         print("The first cube greater than 1234 is " + str(i) + "**3 = " + str(i**3))
#         break
#
# for i in range(1, 11):
#     if i**4 > 1234:
#         print("The first quartic greater than 1234 is " + str(i) + "**4 = " + str(i**4))
#         break
#
# bag_of_candy = ("mint " * 3).split() + ("chocolate " * 4).split() + ("gumdrop " * 3).split()
# print("The bag of candy contains:")
# print(bag_of_candy)
# while "gumdrop" in bag_of_candy:
#     bag_of_candy.pop()
#     print("Ate a gumdrop!")
# print("Oh, no more gumdrops left! " + str(bag_of_candy))
# while "mint" in bag_of_candy:
#     bag_of_candy.remove("mint")
#     print("Ate a mint!")
# print("Oh, no more mints left! " + str(bag_of_candy))
# while len(bag_of_candy) > 0:
#     bag_of_candy.remove("chocolate")
#     print("Ate a chocolate!")
# print("Oh, no more candies left! " + str(bag_of_candy))
#
# bag_of_candy = ("mint " * 3).split() + ("chocolate " * 4).split() + ("gumdrop " * 3).split()
# random.shuffle(bag_of_candy)
# print(bag_of_candy)
# favorite_candies = ["gumdrop", "mint", "chocolate"]
#
# for fav in favorite_candies:
#     print("The bag of candy contains:")
#     print(bag_of_candy)
#     while fav in bag_of_candy and bag_of_candy:
#         print("Ate a " + fav + "!")
#         bag_of_candy.remove(fav)
#     print("Oh, no more " + fav + "s left!")
# print("The bag of candy is empty!\n\n")

print("PART 3\n")

aliens = "Area-51"
for char in aliens:
    if char.isalpha():
        print("Yes, '" + char + "' is an alphabetical character.")
    else:
        print("No, '" + char + "' is not an alphabetical character.")
print("\n")

age = {"Alan": 19, "Brenda": 20, "Charlene": 21, "David": 19, "Ed": 24}
for name in age:
    if age[name] >= 21:
        print(name + " can attend the dance.")
print("\n")

grade = {"Brenda": 88, "Charlene": 77, "David": 100, "Ed": 66, "Frank": 50, "Alan": 91.5, }
for name in grade:
    print(name + " has earned a(n)", end=" ")
    if grade[name] >= 90:
        print("A")
    elif 80 <= grade[name] < 90:
        print("B")
    elif 70 <= grade[name] < 80:
        print("C")
    elif 60 <= grade[name] < 70:
        print("D")
    else:
        print("F")
print("\n")

names = list(grade.keys())
names.sort()

for name in names:
    print(name + " has earned a(n)", end=" ")
    if grade[name] >= 90:
        print("A")
    elif 80 <= grade[name] < 90:
        print("B")
    elif 70 <= grade[name] < 80:
        print("C")
    elif 60 <= grade[name] < 70:
        print("D")
    else:
        print("F")
print("\n")

grades = list(grade.values())
grades.sort(reverse=True)
rank = 1
for num in grades:
    for key, value in grade.items():
        if num == value:
            print(str(rank) + " " + key + " " + str(value))
    rank += 1

print("\n\nPART 4\n")

print(math.fabs(-2.34))
a = 5.
b = 12.
c = math.sqrt(a**2 + b**2)
print(c)
angle = math.sin(b/c)
print(angle)
print(math.degrees(angle))
print(bin(1000))
bin_number = "10100100010000100000"
print(int(bin_number, base=2))
print(bin(int(bin_number, base=2)))
print(math.log(10000000, 1000))
print(math.pow(1000, 7/3))