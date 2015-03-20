import random

def combat(rand, num_soldiers, num_enemies, enemy_type):
    
    if (num_soldiers < num_enemies):
        print "Your troops are %d units less than the enemies, will it be tough?" % (num_enemies - num_soldiers)
    else:
        print "Number shouldn't be a problem"
    
    if num_soldiers == 1:
        num_soldiers -= rand.randint(0, 1)
    else:
        num_soldiers = num_soldiers - (num_enemies * enemy_type // 10)
    
    print "%d of your soldiers have survived!" % num_soldiers
    
    return num_soldiers

def start_battalion(rand, battalion_number, num_soldiers):
    print "Let's see how battalion %d does..." % battalion_number
    print "There go %d soldiers into the battlefield. Which kind of surprises the destiny will award them?" % num_soldiers
    
    enemies = ['goblins', 'orcs', 'trolls', 'barbarians']
    enemies_strengths = [1, 2, 3, 4]
    
    round_count = 1
    while num_soldiers > 0:
        print "Round %d of the battle will start" % round_count
        
        num_enemies = rand.randint(1, num_soldiers * 2)
        
        enemy_index = rand.randint(0, len(enemies) - 1)
        enemy_type = enemies[enemy_index]
        enemy_strength = enemies_strengths[enemy_index]
        
        print "Your %d remaining soldiers of battalion %d will battle %d %s" % (num_soldiers, battalion_number, num_enemies, enemy_type)
        
        num_soldiers = combat(rand, num_soldiers, num_enemies, enemy_strength)
        
        round_count += 1

def start(rand):
    num_soldiers = rand.randint(1, 1000)
    
    print "Your troops are marching to the battlefield. You command %d soldiers. How many battalions do you want them to divide into?" % num_soldiers
    num_battalions = int(raw_input("> "))
    
    print "Ok, here is how the soldiers are organized:"
    
    battalions = []
    
    for i in range(0, num_battalions):
        battalions.append(num_soldiers / num_battalions)
    
    if num_soldiers % num_battalions != 0:
        battalions[len(battalions) - 1] += num_soldiers % num_battalions
    
    count = 1
    for battalion in battalions:
        print "Here is battalion %d of %d soldiers" % (count, battalion)
        count += 1
    
    count = 1
    for battalion in battalions:
        start_battalion(rand, count, battalion)
        count += 1

rand = random.Random()

start(rand)