print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        print("Bye-bye~")
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        print("Bye-bye~")
        break
    try:
        answer = int(first_number)/int(second_number)
        print(answer)
    except ValueError:
        pass
