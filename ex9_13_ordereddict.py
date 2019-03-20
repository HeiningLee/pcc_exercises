from collections import OrderedDict


dict1 = OrderedDict()
dict1['items'] = "the content of a dictionary"
dict1['key'] = 'the handle of data'
dict1['value'] = 'the data that saved in items'
for i, j in dict1.items():
    print(i.title() + " means " + "'" + j + "'.")
