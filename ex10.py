tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\n on a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "We have 3 cats: %s, %s and %s" % (tabby_cat, persian_cat, backslash_cat)
print "We have 3 cats: %r, %r and %r" % (tabby_cat, persian_cat, backslash_cat)