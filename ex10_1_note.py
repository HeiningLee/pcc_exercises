# read and print the learning note.

file_path = r"D:\MyWorks\python\Excercises\text_files\learning_python.txt"

with open(file_path) as file:
    content = file.read()
    print(content.rstrip())

with open(file_path) as file:
    for line in file:
        print(line)

with open(file_path) as file:
    lines = file.readlines()

notes = ''
for line in lines:
    notes += line.strip()
print(notes)
print("######")



