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
