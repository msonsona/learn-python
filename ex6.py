# Assign a string with a formatted value to variable x
x = "There are %d types of people." % 10
# Assign string "binary" to variable binary
binary = "binary"
# Assign string "don't" to variable do_not
do_not = "don't"
# Assign a string with two formatted strings stored in variables to y
y = "Those who know %s and those who %s." % (binary, do_not)

# Print value of variable x
print x
# Print value of variable y
print y

# Print a string with a formatted variable x
print "I said: %r." % x
# Print a string with a formatted variable y
print "I also said: '%s'." % y

# Assign boolean value False to variable hilarious
hilarious = False
# Assign string with a formatter to variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Use two previous variables to print a string with a formatted variable
print joke_evaluation % hilarious

# Assign a string to variable w
w = "This is the left side of..."
# Assign a string to variable e
e = "a string with a right side."

# Print the concatenation of two strings in variables w and e
print w + e