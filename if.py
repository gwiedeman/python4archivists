#this is a list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#add 10 to the end of the list
myList.append(10)

#check if 10 is in the list
if 10 in myList:
	print("Yes!")
else:
	print("no...")
	
#get length of a list with len()
if len(myList) > 15:
	print("bigger than 15")
elif len(myList) == 5:
	print("the list has five things in it")
else:
	print("then what is it?")
	print(len(myList))
	
#to get an item from the list you can use the index: list[0]
#the first item is [0], the second is [1], third is [2], etc.

print(myList[5])
	
#this is a dictionary
myDictionary = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
print (myDictionary)
if "05" in myDictionary:
	#we can nest our loop inside an if statement like this
	for month in myDictionary:
		print(month)
else:
	print("could not find '05' in the dictionary")
#dictionaries are generally used to store and look up things. If we ask our dictionary for the key 08, we should get the value August
print(myDictionary["08"])

#this can be useful for things like changing date formats