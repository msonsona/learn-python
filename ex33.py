def my_range(number, step):
    numbers = []
    
    for i in range(0, number):
        print "At the top i is %d" % i
        numbers.append(i * step)
        
        print "Numbers now: ", numbers
        print "At the botton i is %d" % i
    
    print "The numbers: "
    
    for num in numbers:
        print num
    
    return numbers

numbers_1 = my_range(5, 1)
numbers_2 = my_range(10, 2)
numbers_3 = my_range(50, 5)