'''
Practice allowing parameters at runtime
'''
from sys import argv

# Conditional I added to prevent error if not enough parameters passed
if len(argv) == 4:
    script, first, second, third = argv

    print "The script is called:", script
    print "Your first variable is:", first
    print "Your second variable is:", second
    print "Your third variable is:", third
else:
    first = raw_input("What is your variable? ")
    print "The script is called:", argv[0]
    print "Your first variable is:", first