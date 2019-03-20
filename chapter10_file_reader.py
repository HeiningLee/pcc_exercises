# open and read a text file
file_path = r"D:\MyWorks\python\Excercises\text_files\pi_digits.txt"
with open(file_path) as file:
    content = file.read()
    print(content.rstrip())
    print("######")

with open(file_path) as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())
print("######")

with open(file_path) as file:
    for line in file:
        print(line.rstrip())
print("######")

with open(file_path) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string = pi_string + line.strip()
print(pi_string)
print(len(pi_string))

