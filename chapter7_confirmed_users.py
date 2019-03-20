# chapter7_confirmed_users
# first, create a list of unconfirmed users
# and an empty list to store confirmed users
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# verify every unconfirmed user, until the list of unconfirmed users is empty
while unconfirmed_users:
    verifying_user = unconfirmed_users.pop()
    print("Verifying "+verifying_user+"...")
    confirmed_users.append(verifying_user)
    
# display the verified users
print("\nThe following users have been verified:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
    
