"""
Practice reading from files
"""
from sys import argv

if len(argv) == 2:
    script, filename = argv
else:
    filename = raw_input("What file do you want to open? ")

txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()