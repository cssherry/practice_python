"""
Practice reading from files
"""
from sys import argv

if len(argv) == 2:
    script, filename = argv
else:
    filename = raw_input("What file do you want to open? ")

if filename[-4:] != ".txt":
    filename += ".txt"

# r+ == a+ == a
# w+ == w
txt = open(filename, 'a+')
print "\nHere's your file %r:" % filename
print txt.read()

print "\nNow we're going to erase the contents"
print "\tIf you don't want that, hit CTRL-C (^C)."

raw_input("\tIf you do want that, hit RETURN.")

txt.truncate()

print "\nNow I'm going to ask you for three lines."

line1 = raw_input("\tline 1: ")
line2 = raw_input("\tline 2: ")
line3 = raw_input("\tline 3: ")

print "\nI'm going to write these to the file."

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print "\nAnd finally, we close it."
txt.close()