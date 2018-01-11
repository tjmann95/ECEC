from time import sleep
import sys

print("PART 1\n")

s = "catfish hatchery"
print("The first word in " + repr(s) + " is" + repr(s[:3]) + ".\n")
print("The second word in " + repr(s) + " is " + repr(s[3:7]) + ".\n")
print("The last word in " + repr(s) + " is " + repr(s[-8:]) + ".\n")
print("The number of h's in " + repr(s) + " is: " + str(s.count('h')) + "\n")

target = "aeiouAEIOU"
vowels = 0
for char in s:
    if char in target:
        vowels += 1

print("The number of vowels in " + repr(s) + " is: " + str(vowels) + "\n")

country = "united states of america"
print(country.capitalize())
print(country.title())
print("I live in the " + country.title().replace("O", "o") + ".\n")

word1 = "dogcatcher"
word2 = "dogfish"
word3 = "dogberry"
words = [word1, word2, word3]

dog_start = []
fish_end = []
cat_contains = []
for word in words:
    if word.startswith("dog"):
        dog_start.append(word)
    if word.endswith("fish"):
        fish_end.append(word)
    if "cat" in word:
        cat_contains.append(word)

print("These words start with 'dog': " + " ".join(dog_start))
print("These words end with 'fish': " + " ".join(fish_end))
print("These words contain 'cat': " + " ".join(cat_contains) + "\n\n")

print("PART 2\n")

for i in range(5):
    print(i, end=" ")

print("\n")
for i in range(2, 6):
    print(i*i, end=" ")

print("\n")
for i in range(11, 20, 2):
    print(i, end=" ")

print("\n")
for i in range(1, 6):
    print("*"*i)

print("\n")
for i in range(5):
    print(" "*(4 - i) + "*"*(2*i + 1) + "\n")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
workdays = []
pay = 0
for i in range(5):
    workdays.append(days[i])
    pay += 1000

print("Joe completed a full day's work on: " + " ".join(workdays))
print("His pay for this week is: $" + str(pay))

# count = 10
# while count > -1:
#     sys.stdout.write(str(count) + " ")
#     sys.stdout.flush()
#     sleep(1)
#     count -= 1
# print("Blastoff!\n")

for i in range(5, 21):
    if i**3 > 1234:
        print("The first cube greater than 1234 is " + str(i) + "**3 = " + str(i**3))
        break

for i in range(1, 11):
    if i**4 > 1234:
        print("The first quartic greater than 1234 is " + str(i) + "**4 = " + str(i**4))
        break

bag_of_candy = ("mint " * 3).split() + ("chocolate " * 4).split() + ("gumdrop " * 3).split()
while "gumdrop" in bag_of_candy:
    bag_of_candy.pop()
while "mint" in bag_of_candy:
    bag_of_candy.remove("mint")