name = 'Miquel Sonsona'
age = 30
height = 180 # centimeters
weight = 75 # just guessing
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
cm_per_inch = 2.54
lbs_per_kilo = 2.205

print "Let's talk about %r." % name
print "He's %d centimeters tall. That's %.2f inches." % (height, height / cm_per_inch)
print "He's %d kilos heavy. That's %d pounds." % (weight, weight * lbs_per_kilo)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight)