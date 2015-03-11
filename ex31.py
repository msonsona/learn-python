print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Dance with the bear."
    print "4. Jump through a door behind the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "The bear is so pleased that after a while, it just goes away."
    elif bear == "4":
        print "You enter a small room with a computer. A prompt asks you to type a number"
        number = int(raw_input("> "))
        
        if number < 10:
            print "A trap beneath you opens after %s seconds. Good bye!" % number
        elif 10 < number < 20:
            print "%s hungry wolves enter the room... Good bye!" % number
        else:
            print "Oh, you're so lucky! Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "Oh, you discovered a small, almost hidden door in the corner of the room."
    print "Behind it, a small room contains a box. Do you open it?"
    box = raw_input("> ")
    
    if box == "yes":
        print "You find a grenade inside the box. Do you throw it?"
        grenade = raw_input("> ")
        
        if grenade == "yes":
            print "You explode into pieces, what else you thought would happen?"
        else:
            print "There is no way out, so you starve to death. Good job!"
    else:
        print "Oh, maybe the box was your only option. Good bye!"
else:
    print "You stumble around and fall on a knife and die. Good job!"
