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


class Airplane:
    def spin_propellers(self):
        print "\tPropellers spinning!"

    def fly(self):
        print("Airplane flying")
        self.spin_propellers()

class Whale:
    def swim(self):
        print("Whale swimming")


# polymorphic method
def lift_off(entity):
    entity.fly()


# construct some objects from these classes
bird = Bird()
duck = Duck()
airplane = Airplane()
whale = Whale()

lift_off(bird)  # prints Bird flying
lift_off(duck)  # prints Duck flying
lift_off(airplane)  # prints Airplane flying

# examples that fail the duck test

try:
    lift_off(whale)  # Throws error: Whale object has no attribute fly
except Exception as e2:
    print "Ack! Whales cannot fly!", e2
    whale.swim()