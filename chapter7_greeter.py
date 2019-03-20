#chapter7_greeter

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, "+name+"!")

ask_age = "\nHow old are you?"
age = input(ask_age)
if int(age)>=18:
    print("\nYou are "+age+", you can take a vote.")
else:
    print("\nYou are not old enough to take a vote.")
