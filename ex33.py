def my_range(number):
    i = 0
    numbers = []
    
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + 1
        print "Numbers now: ", numbers
        print "At the botton i is %d" % i
    
    print "The numbers: "
    
    for num in numbers:
        print num
    
    return numbers

numbers_1 = my_range(5)
numbers_2 = my_range(10)
numbers_3 = my_range(50)