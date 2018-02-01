# A greeting method with a variable number of arguments and type-checking.

def greeting(*args):  # A method with a variable number of parameters.

    # print type(args)  # It's a tuple! Do not include the '*' here.


    # Handle the case of no arguments here.


    # Handle the case of two arguments here.



    if len(args) == 1:
        argument = args[0]

        if isinstance(argument,str):
            print "Yes! It's my first day! My name is %s." % argument

        if isinstance(argument, bool):
            if argument:
                print "Sure! Let's have coffee together."
            else:
                print "Sorry! I'm flat broke!"
        elif isinstance(argument,int):
            print "Can I borrow $%d for coffee?" % argument


greeting()
greeting("Mork")
greeting("Mork", "Mindy")
greeting(10)
greeting(True)