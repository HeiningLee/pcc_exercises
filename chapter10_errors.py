''' use try-except to deal with errors '''

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
