def call_this_number(number):
    print "Calling %d..." % number
    print "Someone will answer shortly"

def fake_number_generator():
    return 42

call_this_number(911)

call_this_number(900 + 11)

number_to_call = 911
call_this_number(number_to_call)

another_number = 900
call_this_number(another_number + 11)

catalan_emergency_number = 112
call_this_number(catalan_emergency_number)

call_this_number(number_to_call - catalan_emergency_number)

call_this_number(catalan_emergency_number * 3)

call_this_number(1 * number_to_call)

custom_number = number_to_call / catalan_emergency_number
call_this_number(custom_number)

call_this_number(fake_number_generator())

call_this_number(int(raw_input("Which number do you want to call? ")))