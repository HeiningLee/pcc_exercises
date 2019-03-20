# ex6_10: favorite numbers
favorite_numbers = {
    'jen':[1,2],
    "sarah":[3],
    'edward':[4,5],
    'phil':[1,2,3],
    }

for i,q in favorite_numbers.items():
    if len(q)<=1:
        print("\nThe favorite number of "+i+" is "+str(q[0])+".")
    else:
        print("\nThe favorite numbers of "+i+" are:")
        for j in q:
            print(str(j))
