from sys import argv
from os.path import exists

def append_txt(filename):
    """To append .txt extension if it doesn't already exist"""
    if filename[-4:] != ".txt":
        filename += ".txt"
    return filename

if len(argv) == 3:
    script, from_file, to_file = argv
else:
    from_file = raw_input("What file do you want to copy? ")
    to_file = raw_input("What do you want to call the copy? ")

if exists(append_txt(from_file)):
    open(append_txt(to_file), 'w').write(open(append_txt(from_file)).read())
    print "Alright, all done."
else:
    print "FAILED: file doesn't exist."