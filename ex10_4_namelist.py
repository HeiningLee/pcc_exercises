filename = r"D:\MyWorks\python\Excercises\text_files\guest_book.txt"

guest_name = ''
with open(filename, 'w') as file:
    while guest_name != 'quit':
        guest_name = input("Please input your name:")
        if guest_name != 'quit':
            print(guest_name.title() + ", Greeings!")
            file.write(guest_name.title() + "\n")

with open(filename) as fileread:
    content = fileread.read()
    print(content)