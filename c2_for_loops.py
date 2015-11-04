import re # Use for regex splitting

names = re.split("\W+", raw_input("Who is involved? "))
 # Now going through all the names and printing them

print "Thanks! Including: "
for name in names:
  print name

print "When in order, the names are: "

# Range does not include the last elements
# Use len instead of .length
for idx in range(0, len(names)):
  print "%d) %s" % (idx, names[idx])
  # Use .append instead of .push
  names.append(idx)

print names