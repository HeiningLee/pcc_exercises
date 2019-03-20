#chapter7_polling

responses = {} # set up an empty dict
polling_active = True # initialize a marker for the loop

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("\nWould you like to let another person respond?(y/n) ")
    if repeat == 'n':
        polling_active = False
        
print("--- Poll Results ---")
for name, response in responses.items():
    print(name+" would like to climb "+response)
