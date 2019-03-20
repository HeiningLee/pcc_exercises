#ex4_4
print("EX4_4: ")
nums = range(1,1000001)
print("\nThe max number is: " + str(max(nums)))
print("\nThe min number is: " + str(min(nums)))
print("\nThe sum is: " + str(sum(nums)))

#ex4_5
print("\nEx4_5:")
oddnums = range(1,20,2)
for oddnum in oddnums:
	print(oddnum)

#ex4_6
print("\nEx4_6:")
trinums = range(3,30,3)
for trinum in trinums:
	print(trinum)

#ex4_7
print("\nEx4_7:")
cubnums = [cubnum**3 for cubnum in range(1,11)]
for cubnum in cubnums:
	print(cubnum)

#ex4_10
print("\nEx4_10:")
girls = ['jessie','abby','avy','abigile','winnie']
print("\nThe first three girls in the list are: \n")
for girl in girls[:3]:
	print(girl)
print("\nThe girls from the middle of the list are: \n")
for girl in girls[1:4]:
	print(girl)
print("\nThe last three girls in the list are: \n")
for girl in girls[-3:]:
	print(girl)
	
#ex4_11
print('\nEx4_11')
mygirls = girls[:]
mygirls.append('jill')
girls.append('eda')
print(mygirls)
print(girls)
print("\n The girls they have are: ")
for girl in girls:
	print(girl)
print("\nThe girls I want are: ")
for mygirl in mygirls:
	print(mygirl)

#ex4_13
print('\nEx4_12 ')
girls = ('jessie','abby','avy','abigile','winnie')
print('\nThe original girls are: ')
for girl in girls:
	print(girl)
print('\nThe new girls are: ')
girls = ('jessie','macheal','avy','abigile','winnie')
for girl in girls:
	print(girl)
