import time

class Bird:
    def flap_wings(self):
        print "\tFlap, ",
        for n in range(5):
            print "flap,",
            time.sleep(0.25)
        print "..."

    def fly(self):
        print("Bird flying")
        self.flap_wings()


class Duck(Bird):
    def fly(self):
        print("Duck flying")
        self.flap_wings()


class Dodo(Bird):
    def flap_wings(self):
        print "Flapping wings is useless! SPLAT!"

    def fly(self):
        print "Dodos can't fly!"


class Airplane:
    def spin_propellers(self):
        print "\tFlap, ",
        for n in range(5):
            print "spin,",
            time.sleep(0.25)
        print "..."

    def fly(self):
        print("Airplane flying")
        self.spin_propellers()

class Whale:
    def swim(self):
        print("Whale swimming")
        self.flex_body_wave_fins()

    def flex_body_wave_fins(self):
        print "Flexing body and tail back and forth. Steering with fins."
        print "\tFlexing: back, ",
        for n in range(4):
            if n % 2 == 0:
                print "forth, ",
            else:
                print "back, ",
            time.sleep(0.25)
        print "..."


# polymorphic method
def lift_off(entity):
    entity.fly()


# construct some objects from these classes
bird = Bird()
duck = Duck()
airplane = Airplane()
whale = Whale()
dodo = Dodo()

lift_off(bird)  # prints Bird flying
lift_off(duck)  # prints Duck flying
lift_off(airplane)  # prints Airplane flying

# examples that fail the duck test

try:
    lift_off(whale)  # Throws error: Whale object has no attribute fly
except Exception as e2:
    print "Ack! Whales cannot fly!", e2
    whale.swim()

try:
    lift_off(dodo)
except Exception as e1:
    print repr()