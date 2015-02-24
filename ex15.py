# Importing argv from the sys module
from sys import argv

# Unpacking argument variables into script and filename vars
script, filename = argv

# Open the file named by the value in filename, and assign to variable txt
txt = open(filename)

# Print a string containing the filename passed as argument
print "Here's your file %r:" % filename
# Print the contents of the specified file, using read() function
print txt.read()

# Closing file txt
txt.close()

# Prompting the user
print "Type the filename again:"
# Read the input from the user
file_again = raw_input("> ")

# Open the file with the name the user gave
txt_again = open(file_again)

# Print the file's contents
print txt_again.read()

# Closing file txt_again
txt_again.close()