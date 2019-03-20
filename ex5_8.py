#ex5_8:accounts manager
usernames = ['abby','avy','jessie','winnie','admin']##
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin! would you like to see a status report?")
        else:
            print("Hello "+username+", thank you for logging in again! ")
else:
    print("We need to find some users!")
#ex5_10:new username
current_usernames = ['abby','avy','jessie','jinnie','admin']##
new_usernames = ['ABBY','aVy','Jill','Misa','Eva']
for new_username in new_usernames:
    if new_username.lower() in current_usernames:
        print(new_username+": this names has been used.")
    else:
        print(new_username+": username available.")
        
#ex5_11: Serial numbers
nums = range(1,10)
for num in nums:
    if num == 1:
        suffix = 'st'
    elif num == 2:
        suffix = 'nd'
    elif num == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(str(num)+suffix)
