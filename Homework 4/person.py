""" A person has a first and last name, a certain number of teeth and a weight in pounds. """

# Unlike in most languages, whether a Python function, method, or attribute is public, private or protected
# is determined entirely by its name. If it starts with one underscore, it is protected.
# If a name starts with two underscores but does not end with two underscores, it is 'private'.

class Person(object):
    def __init__(self):            # All variables are protected
        self._firstName = ""
        self._lastName = ""
        self._numberOfTeeth = 32   # 32 is you still have them all.
        self._weight = 0           # Weight in pounds
        self._gender = False
        self._height = []
        self._age = 0
        self._numberOfFillings = 0
        self._numberOfCaps = 0

    def setNumberOfCaps(self, num):
        self._numberOfCaps = num

    def getNumberOfCaps(self):
        return self._numberOfCaps

    def setNumberOfFillings(self, num):
        self._numberOfFillings = num

    def getNumberOfFillings(self):
        return self._numberOfFillings

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

    def setHeight(self, height):
        self._height = height

    def getHeight(self):
        return self._height

    def setGender(self, gender):
        self._gender = gender

    def getGender(self):
        return self._gender

    def setFirstName(self, first):
        self._firstName = first

    def setLastName(self, last):
        self._lastName = last

    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def __repr__(self):
        return self._firstName + " " + self._lastName

    def getNumberOfTeeth(self):
        return self._numberOfTeeth

    def setNumberOfTeeth(self, number_teeth):
        self._numberOfTeeth = number_teeth

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    # A person can go on a diet and loose weight.
    def looseWeight(self,  weightLoss):
        self._weight -= weightLoss

    def gainWeight(self,  weightGain):
        self._weight += weightGain

    # Add Accessors and mutators for all the new protected variables here.




if __name__ == "__main__":
    # Let's "build" a person.
    monty = Person()
    monty.setFirstName("Monty")
    monty.setLastName("Python")
    print "This person is named:", monty
    monty.setWeight(200)
    print "Monty initially weighs %d pounds." % monty.getWeight()
    print "Sadly, Monty has recently gained 20 pounds, due to overindulgence throughout the holidays."
    monty.gainWeight(20)
    print "Now Monty weighs %d pounds." % monty.getWeight()
    monty.setGender(True)
    print "Monty is %s." % "male" if monty.getGender() == True else "female"
    monty.setHeight([5, 10])
    print "Monty is %d' %d\"." % (monty.getHeight()[0], monty.getHeight()[1])
    monty.setAge(34)
    print "Monty is %d years old." % monty.getAge()
