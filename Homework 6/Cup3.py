class Cup3:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable - two underscores!!

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def getContent(self):   # A method has been added so the user can access the private __content field.
        return self.__content


if __name__ == "__main__":

    print "\nExample showing the use of a private variable with two underscores.\n\n"

    # Pour yourself some tea in a red cup.
    redCup = Cup3("orange")  # Construct a new cup object, but note now you must provide the color at construction!
    redCup._color = "red"    # Woops! We meant it to be red. You can still directly change the color.
                             # Even though _color is protected.
    redCup.fill("tea")
    print "1. Nice! A full cup of %s in my favorite %s cup." % (redCup.getContent(), redCup._color)

    print "Sip, sip, sip."
    redCup.empty()
    print "Ack! My cup is empty! Contents =", redCup.getContent()

    print "\n2. Let's fill it up again with Red Bull this time. "
    redCup.fill("Red Bull")
    print "Nice! A full cup of %s in my favorite %s cup." % (redCup.getContent(), redCup._color)
    print "Sip, sip, sip."
    redCup.empty()
    print "Ack! My cup is empty! Contents =", redCup.getContent()


    print "\n\n3. Let's refill one more time with 'red wine'."
    redCup.fill("red wine")

    print "OK, now let's try to access that private variable '__content' from outside."
    print "What's in the cup now? ",

    try:
        print redCup.__content  # Nope! You can't do this!!
    except Exception as e:
        print "\nTrying to access the private variable directly produced this error message."
        print repr(e)

    # Instead you must use getContent() which the coder has been kind enough to provide.
    print "Try again using the public accessor. What's in the cup now? ", redCup.getContent()



    print "\n\n4. Even though the '__content' is private, a clever user can still get to it."

    message = "\nPython supports a technique called *name mangling*.\n" + \
              "This feature turns every member name prefixed with at least two underscores and\n" \
              "suffixed with at most one underscore into _<className><memberName> ."
    print message

    print "Below, we exploit name mangling to get to the protected '__content'."
    blackCup = Cup3("black")
    blackCup.fill("Ambrosio")

    print "What's in the cup now? ", blackCup._Cup3__content  # Dang! A hacker can still get to it!



    # Add code here to fill a transparent cup with coins. It's a piggy bank!
    """
    i.  Now add code to create a transparent cup and fill it with "coins". We are using it as a piggy bank.
    ii. Then access and print out the contents using the public method getContent().
    iii. Finally, access the contents using name mangling instead.  """
    transCup = Cup3("transparent")
    transCup.fill("coins")
    print transCup.getContent()
    print transCup._Cup3__content

