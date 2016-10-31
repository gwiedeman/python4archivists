import csv

csvPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "executedJuveniles.csv")

csvFile = open(csvPath, "r")
csvObject = csv.reader(csvFile)

#loop though the CSV file
for row in csvObject:
	print(row[2])
	
csvFile.close()

"""
#Function to make DACS display date from ISO format
def DACS(isoDate):
	if isoDate.lower().strip() == "date unknown":
		return "Undated"
	else:
		calendar = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
		year = isoDate[:4]
		if len(isoDate) == 4:
			return isoDate
		else:
			month = isoDate[5:7]
			day = isoDate[-2:]
			if day.startswith("0"):
				day = day[-1:]
			dacs = year + " " + calendar[month] + " " + day
			return dacs

#set and empty list and initialize the count at 0
newList = []
rowCount = 0

#open the original CSV again and read it
csvFile = open(csvPath, "r")
csvObject = csv.reader(csvFile)

for row in csvObject:
	#count the number of times though the loop
	rowCount = rowCount + 1
	#if more than the first time though the loop
	if rowCount > 1:
		#make a list of the rowCount, the 3rd column, and the 4th column using the DACS function
		rowList = [rowCount - 1, row[2], DACS(row[3])]
		#append that list to the newList - its just a list of lists
		newList.append(rowList)

#close the original CSV file
csvFile.close()


newCSV = "C:\\Users\\[USERNAME]\\python4archivists\\csvDACS.csv"

newFile = open(newCSV, "w", newline='')
newCSV =  csv.writer(newFile, delimiter='|')
newCSV.writerows(newList)
newFile.close()
"""
