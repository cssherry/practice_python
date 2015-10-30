"""
Practice reading and writing files
"""
from sys import argv
from os.path import exists
from helper_functions import append_txt

if len(argv) == 2:
    script, filename = argv
else:
    filename = append_txt(raw_input("What file do you want to open? "))

file_exists = exists(filename)
if file_exists:
    txt = open(filename)
    print "\nHere's your file %r:" % filename
    print txt.read()
    txt.close()
else:
    print "\nThis will be a new file!"
    print "If you don't want that, hit CTRL-C (^C)."

# r+ writes like insert
# a+ reads from end of file, writes to end of file, creates file if it doesn't exist
# w+ will overwrite and read from end of file (file overwritten upon open)
# r, w, and a will only do their respective tasks
if file_exists:
    open_type = raw_input("Do you want to overwrite (w) or append (a)? ").lower()
    if open_type != "w" and open_type != "a" and open_type != "r":
        print "Not a valid option. We're going to append"
        open_type = "a"
    print "\nNow we're going to do your action"
    print "If you don't want that, hit CTRL-C (^C)."
else:
    open_type = "w"

print "\nNow I'm going to ask you for three lines."

txt = open(filename, open_type + "+")
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

# Need to seek to beginning of file or else overwrites
txt.seek(0)
print "\nYour file is now:"
print txt.read()
txt.close()