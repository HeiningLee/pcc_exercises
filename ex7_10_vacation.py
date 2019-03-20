#ex7_10_vacation
responses = {}
pollactive = True

while pollactive:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, "+
        "where would you go? ")        
    responses[name] = response
    repeat = input("\nWould you like to continue the poll?(y/n) ")
    if repeat == 'n':
        pollactive = False
        print("\nGood Bye~")
        
print("--- Poll Results ---")
for name, response in responses.items():
    print(name+" would like to visit "+response)
    
    
