# ex6_4: more dictionary
dictionary = {'items':"the content of a dictionary",
    'key':'the handle of data',
    'value':'the data that saved in items'}

for i in dictionary.keys():
    print('\nThe meaning of '+str(i)+' is:')
    print(dictionary[i])
    
dictionary['rabbit']='a small rodent animal'
dictionary['puma']='a large catlike animal'

for i in dictionary.keys():
    print('\nThe meaning of '+str(i)+' is:')
    print(dictionary[i])
