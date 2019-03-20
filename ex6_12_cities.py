#ex6_12:cities
cities ={
    'huizhou':{
        'country':'china',
        'population':4000000,
        'fact':'my living city',
        },
    'guangzhou':{
        'country':'china',
        'population':80000000,
        'fact':'the capital of guangdong province',
        },
    'sishui':{
        'country':'china',
        'population':2000000,
        'fact':'my hometown',
        },
    }
    
for city, city_info in cities.items():
    print("\nThe infomation of "+city+" are as follows: ")
    for i in city_info.keys():
        print("\t"+i.title()+": "+str(city_info[i]).title())
        
