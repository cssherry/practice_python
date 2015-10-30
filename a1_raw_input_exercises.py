"""Functions used in http://learnpythonthehardway.org/book"""
def get_input():
    """This uses print statements to get input"""
    print "How old are you?",
    age = raw_input()
    print "How tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()

    print "So, you're %d old, %s tall and %d heavy." % (
        int(age), str(height), int(weight))

def get_input_shorter():
    """This uses strings within print statements"""
    age = raw_input("How old are you? ")
    height = raw_input("How tall are you? ")
    weight = raw_input("How much do you weigh? ")

    print "So, you're %d old, %s tall and %d heavy." % (
        int(age), str(height), int(weight))

def print_two(*args):
    """This function tests out splatting arguments and then unpackaging"""
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
