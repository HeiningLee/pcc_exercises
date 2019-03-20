#ex3_4
guests = ["Charlie","Jack","John","Jon"]
print("The list of guests are as follows:\n")
for guest in guests:
	print("\t"+guest)
n= len(guests)
print('\tWe invited '+str(n)+' guests.')
print("But, Jack is not comming")
print("So the list of guests are as follows:\n")

guests[1] = "Lucus"
for guest in guests:
	print("\t"+guest)
n= len(guests)
print('\tWe invited '+str(n)+' guests.')
print("And behold the table is growing bigger!")
print("We can now invite more guests!")
print("Now the list of guests are as follows:\n")

guests.insert(0,'Hond')
guests.insert(2,'Honk')
guests.append('Hont')
for guest in guests:
	print("\t"+guest)
n= len(guests)
print('\tWe invited '+str(n)+' guests.')
print("And fuck the motherfucking table!")
print("It shrinked to one half of the size!")
print("We can now just invite two guests!")
for i in range(0,4):
	guest_out = guests.pop(i)
	print("\t"+guest_out + "! Im so sorry that you are fucked!")

for guest in guests:
	print("\tDon\'t worry "+guest + ", you\'re still invited!")
print("At last, the list of guests are as follows:\n")
for guest in guests:
	print("\t"+guest)
n= len(guests)
print('\tWe invited '+str(n)+' guests.')
