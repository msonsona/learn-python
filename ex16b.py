from sys import argv

script, filename = argv

print "We're going to read %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print "Reading the file. Here it is!"
print target.read()

print "And finally, we close it."
target.close()