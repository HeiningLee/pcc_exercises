#ex7_8_delicatessen
sandwich_orders = ['beef','tuna','beef','pork','beef','chicken','beef']
sandwich_finished = []
while sandwich_orders:
    sandwich_making = sandwich_orders.pop()
    print("Making "+sandwich_making+" sandwich, please stand by...")
    sandwich_finished.append(sandwich_making)
    
print("\nThe following sandwiches are finished:\n ")
for sandwich in sandwich_finished:
    print(sandwich)
