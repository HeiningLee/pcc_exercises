#ex7_9_soldout

sandwich_orders = ['beef','tuna','beef','pork','beef','chicken','beef']
sandwich_finished = []
print("We sold out all the beef in store.")
while 'beef' in sandwich_orders:
    sandwich_orders.remove('beef')


while sandwich_orders:
    sandwich_making = sandwich_orders.pop()
    print("Making "+sandwich_making+" sandwich, please stand by...")
    sandwich_finished.append(sandwich_making)
    
print("\nThe following sandwiches are finished:\n ")
for sandwich in sandwich_finished:
    print(sandwich)
