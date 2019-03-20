#ex6_8: pets
pet_0 = {
    'name':'blackbean',
    'type':'dog',
    'owner':'li xy'}
pet_1 = {
    'name':'flower',
    'type':'cat',
    'owner':'zhou c'}

pets = [pet_0, pet_1]
for pet in pets:
    print("\nPet info:")
    print("\tName: " + pet['name'].title())
    print("\tType: " + pet['type'].title())
    print("\tOwner: " + pet['owner'].title())
