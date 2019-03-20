filename = r"D:\MyWorks\python\Excercises\text_files\programming.txt"

with open(filename, 'w') as file:
    file.write("I love programming.\n")
    file.write("I love creating new games.\n")

with open(filename, 'a') as file:
    file.write("I also love finding meaning in large datasets.\n")
    file.write("I love creating apps that can run in a browser.\n")

with open(filename) as file:
    content = file.read()
    print(content)
