#ex7_4_pizza_toppings
prompt = "\nWhat topping do you want?"
topping = ""

while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print("\nWe'll add some "+topping+" on your pizza,"+
            "what else do you need?")
    else:
        print("\nGood Bye~")
    
