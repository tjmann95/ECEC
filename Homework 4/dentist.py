# Every dentist is a person.
# The difference is a dentist is licensed to extract teeth.
# A person has a first and last name, a certain number of teeth and a weight.
# A Dentist can also extract a person's tooth.
# Example to illustrate the substitution principle and polymorphism.

from person import Person


class Dentist(Person):  # A dentist is a person!
    def __init__(self):
        super(Dentist, self).__init__()
        # Person.__init__(self) # an old fashioned way
        self._hasDentistLicense = True

    # Specialty method of dentist subclass. A dentist can extract a person's tooth.
    def extractTooth(self, patient):
        patient.setNumberOfTeeth(patient.getNumberOfTeeth() - 1 )


dentist1 = Dentist()
dentist1.setFirstName("Dr.")
dentist1.setLastName("Good")

patient1 = Person()
patient1.setFirstName("Monty")
patient1.setLastName("Python")

print "\nPatient #1: %s %s" % (patient1.getFirstName(), patient1.getLastName())

print "Your dentist's name is:", dentist1
print "Dentist: I'm sorry %s, we'll have to extract one of your %d teeth." % (patient1.getFirstName(), patient1.getNumberOfTeeth())
dentist1.extractTooth(patient1)
print "Dentist: There you go. All better now!"
print "%s, all your remaining %d teeth are in perfect condition!" %(patient1.getFirstName(), patient1.getNumberOfTeeth())
print "Dentist: That will be $1000.00"


patient2 = Dentist()
patient2.setFirstName("Doctor")
patient2.setLastName("Bad")
print "\nPatient #2: %s %s" % (patient2.getFirstName(), patient2.getLastName())
print "Dentist: I'm sorry %s %s, we'll have to extract two of your %d teeth." % (patient2.getFirstName(), patient2.getLastName(), patient2.getNumberOfTeeth())
print "Dentist: Yank, yank! All better now!"

dentist1.extractTooth(patient2)
dentist1.extractTooth(patient2)
print "%s %s, all your remaining %d teeth are in perfect condition!" %(patient2.getFirstName(), patient2.getLastName(), patient2.getNumberOfTeeth())
print "Dentist: That will be $2000.00"



# Can any person extract teeth - or only dentists?
print "\nPatient #3: %s %s" % (patient1.getFirstName(), patient1.getLastName()), "Ouch! he has injured another tooth!!"

print "Ack! Monty has wrecked another tooth playing hockey and it needs to be extracted."
print "Can a teammate extract his tooth for free?"

teammate = Person()
teammate.setFirstName("Temporary")
teammate.setLastName("Dentist")

try:
    teammate.extractTooth(patient1)
except Exception as e:
    print "Sorry, he's not a real dentist. He can't really extract your teeth."
    dentist1.extractTooth(patient1)
    print "Dentist: Yank, All better now!"
    print "Dentist: That will be another $1000.00"
    print "Dentist: Take better care of your remaining %d teeth." % patient1.getNumberOfTeeth()
