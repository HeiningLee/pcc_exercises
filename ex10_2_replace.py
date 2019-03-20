file_path = r"D:\MyWorks\python\Excercises\text_files\learning_python.txt"

with open(file_path) as thefile:
    lines = thefile.readlines()

newtext = ''
for line in lines:
    line = line.replace('Python', 'C++')
    newtext += line
print(newtext)
