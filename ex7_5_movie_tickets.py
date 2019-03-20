#ex7_5_movie_tickets
prompt = "\nPlease enter your age:"
active = True
while active:
    age = input(prompt)
    if age == "quit":
        active = False
        continue## leap all the lines bellow
    elif int(age)<3:
        print("\nYour ticket is free.")
    elif int(age)<12:
        print("\n10 dollars please.")
    else:
        print("\n15 dollars please.")
    
