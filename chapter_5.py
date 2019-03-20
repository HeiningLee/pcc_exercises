#Chapter 5
#voting
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registed to vote?')
    
# voting_@
age = 17
if age >= 18:
    print("You're old enough to vote!")
    print('Have you registered yet?')
else:
    print("Sorry, you're too young to vote. ")
    print('Please register to vote as soon as you turn "18"!')
    
# if-elif-else
age = 3
if age<4:
    cost = 0
elif age<8:
    cost = 5
else:
    cost = 10

print('Cost is: '+ str(cost))

#topping: pizza making
requested_toppings = ['green peppers','meshrooms','extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if 'green peppers' == requested_topping:
            print("Sorry, we're out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")

print("Finished your pizza!")
        

