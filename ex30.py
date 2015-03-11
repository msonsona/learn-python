# Assign variables
people = 50
cars = 40
trucks = 15

# If there are more cars than people, or 50 fifty people
if cars > people or people == 50:
    print "We should take the cars."
# If there are less cars than people
elif cars < people:
    print "We should not take the cars."
# If there are as many cars as people (and not 50)
else:
    print "We can't decide."

# If there are more trucks than cars
if trucks > cars:
    print "That's too many trucks."
# If there are less trucks than cars
elif trucks < cars:
    print "Maybe we could take the trucks."
# finally, if there are as many trucks as cars
else:
    print "We still can't decide."

# If there are more people than trucks
if people > trucks:
    print "Alright, let's just take the trucks."
# If there are as many people as trucks or less
else:
    print  "Fine, let's stay home then."

# If there are exactly 50 people
if people == 50:
    print "There are 50 people!"
# Otherwise
else:
    print "There aren't 50 people."