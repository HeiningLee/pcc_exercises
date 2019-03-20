#ex6_9: favorite places
favorite_places = {
    'jen':['a'],
    'sarah':['c','d'],
    'edward':['e'],
    'phil':['a','b','c','d'],
    }
for i in favorite_places.keys():
    if len(favorite_places[i])>1:
        print("\nThe favorite places of " + i.title() + " are: ")
        for j in favorite_places[i]:
            print(j.title())
    else:
        print("\nThe favorite place of " + i.title() + " is " +
            favorite_places[i][0].title()+". ")
