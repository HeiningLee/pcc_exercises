#chapter7_even_or_odd
number = input("Enter a number, and I will tell you if it's even or odd:")
number = int(number)

if number%2 == 0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")
