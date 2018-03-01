class Cup1:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

if __name__ == "__main__":
    # 1. Pour yourself some tea in a red cup.
    redCup = Cup1()  # Construct a new cup object.
    redCup.color = "red"
    redCup.content = "tea"
    print "Nice! A full cup of %s in my favorite %s cup." % (redCup.content, redCup.color)

    redCup.empty()
    print "Sip, sip, sip."
    print "On no! My cup is empty! Contents = %s." % redCup.content


    # Now add some code.
    # 2. Pour yourself some coffee in a blue cup.
    # Then sip it until it is empty.
    blueCup = Cup1()
    blueCup.color = "blue"
    blueCup.content = "coffee"

    blueCup.empty()