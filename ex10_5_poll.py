filename = r'D:\MyWorks\python\Excercises\text_files\ex10_5_poll.txt'

reason = ''
with open(filename, 'w') as file:
    while reason != 'quit':
        reason = input("Why do you like programming?")
        if reason != 'quit':
            file.write(reason + '\n')

with open(filename) as file:
    content = file.read()
    print(content)