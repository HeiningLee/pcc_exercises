#ex6_6: more favorite languages
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'}

list_names = ['alpha','sarah','edward','phil','avy','yang']
for i in list_names:
    if i in favorite_languages.keys():
        print(i.title() + ', thank you for taking the poll!')
    else:
        print(i.title() + ', please take the poll.')
