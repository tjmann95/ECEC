class Cup2:
    def __init__(self):
        self.color = None      # no change here, still public
        self._content = None   # now it's a protected variable. It has one underscore.

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

if __name__ == "__main__":

    print "\nExample showing the user has no trouble accessing a protected variable.\n\n"

    # 1. Pour yourself some tea in a red cup.
    redCup = Cup2()  # Construct a new cup object.
    redCup.color = "red"
    redCup._content = "tea"  # User has been naughty and insisted on accessing our protected variable!! Shame!


    # User again accesses the protected  variable here.
    print "1. Nice! A full cup of %s in my favorite %s cup." % (redCup._content, redCup.color)
    redCup.empty()

    print "Sip, sip, sip."
    print "On no! My cup is empty! Contents = %s."  % redCup._content

    message = "\nThat is very rude to access a protected variable using an underscore like that!"
    message += "\nOf course I can't stop you, but shame on you!!"

    print message

    # Now add some code.
    # 2. i. Pour yourself some coffee in a blue cup.
    # Then sip it until it is empty.
    blueCup = Cup2()
    blueCup.color = "blue"
    blueCup.fill("coffee")

    # 2. ii. Now refill your cup with tomato soup, then sip it until it is empty.
    blueCup.empty()
    blueCup.fill("tomato soup")




