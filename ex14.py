from sys import argv

script, user_name, time = argv
prompt = 'Your answer here, please -> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "It's %s, it's getting late, so I'd like to ask you a few questions." % time
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)