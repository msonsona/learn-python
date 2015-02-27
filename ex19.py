# Defining the cheese_and_crackers function, which receives two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print the value of first parameter formatted within a string
    print "You have %d cheeses!" % cheese_count
    # Print the value of the second parameter formatted within a string
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Print a couple of strings more
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Call function with numbers as parameters
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Assign values to two variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Use these variables to call the function with them as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call the function with math expressions as parameters
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Call the function combining variables and math expressions as parameters
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)