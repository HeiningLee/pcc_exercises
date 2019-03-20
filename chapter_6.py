# chaper6 : dictionary in list
print('Dict in list:')
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# aliens in list
aliens = []
# create new aliens with a loop
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)# add new_alien to the end of list: aliens
    
    
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
            
for alien in aliens[:10]:
    print(alien)
print('...')

print('Total number of aliens: '+str(len(aliens)))
