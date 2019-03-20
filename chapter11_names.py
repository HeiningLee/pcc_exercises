from chapter11_name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter first name: ")
    if first == 'q':
        break
    last = input("\nEnter last name: ")
    if last == 'q':
        break
    middle = input("\nEnter middle name: ")
    formatted_name = get_formatted_name(first, middle, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
