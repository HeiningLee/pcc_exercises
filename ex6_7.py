#ex6_7: the people list with personal info
people = []
people_0 = {
    'first':'albert',
    'last':'einstein',
    'yob':1879,
    'city':'new york',
    }
people_1 = {
    'first':'mary',
    'last':'curie',
    'yob':1867,
    'city':'paris',
    }
people_2 = {
    'first':'li',
    'last':'haining',
    'yob':1988,
    'city':'huizhou',
    }
    
people = [people_0,people_1,people_2]

for person in people:
    full_name = person['first'].title() + " " + person['last'].title()
    print("\n" + full_name + ": ")
    print("\tYear of birth:" + str(person['yob']))
    print("\tCity:" + person['city'])
