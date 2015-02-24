print "Which day is today?",
day_of_week = raw_input()
print "Of which month?",
month = raw_input("month? >")
print "And is it sunny?",
is_sunny = raw_input("Is sunny? >")

print "Ok, so today is a sunny %s of %s, is it? %s." % (
    day_of_week, month, is_sunny)