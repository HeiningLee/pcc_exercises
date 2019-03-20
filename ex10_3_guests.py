file_path = r"D:\MyWorks\python\Excercises\text_files\guests.txt"

name = ''
with open(file_path, 'w') as file_object:
    while name != 'quit':
        name = input("Please input your name (input quit to end):")
        if name != 'quit':
            file_object.write(name + "\n")
            print("Name saved.")

with open(file_path) as fileout:
    content = fileout.read()
    print(content)
