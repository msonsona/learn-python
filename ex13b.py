from sys import argv

script, topic = argv

print "The script is called:", script
what = raw_input("What do you know about %s? " % topic)
print "So you know %s about %s? Alright." % (what, topic)