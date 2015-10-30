"""
This file will allow users to first create or open a file
Then you can overwrite lines or append
"""
from sys import argv
from os.path import exists

exit_command = "exit()"

def append_txt(filename):
    """To append .txt extension if it doesn't already exist"""
    if filename[-4:] != ".txt":
        filename += ".txt"
    return filename

def get_input(contents):
    """Query user for line number, and line they want"""
    line_number = raw_input("What line do you want? ")
    if line_number != exit_command:
        line_number = int(line_number) - 1
        if len(contents) > line_number:
            print line_number + 1, ": ", contents[line_number]
        else:
            print "You've chosen the last line"
    else:
        return "exit()"
    text = raw_input("What do you want to write? ")
    if text == exit_command:
        return "exit()"
    return {"line": line_number, "text": text}

if len(argv) >= 2:
    filename = argv[1]
else:
    filename = raw_input("What would you like to call the file? ")

filename = append_txt(filename)
if exists(filename):
    # file.read() returns back string, so need to make it an array and indexable
    file_content = open(filename).read().split("\n")
    print "\n", filename, " currently contains:"
    for idx, line in enumerate(file_content):
        print idx + 1, ": ", line
else:
    print "\nCreating file ", filename
    file_content = []

print "\nStop at any time by entering 'exit()'"
commands = get_input(file_content)
while commands != exit_command:
    if commands["line"] > len(file_content):
        file_content.append(commands["text"])
    else:
        file_content[commands["line"]] = commands["text"]
    commands = get_input(file_content)

print "\nCurrent file contents:"
print "\n".join(file_content)

open(filename, "w").write("\n".join(file_content))
