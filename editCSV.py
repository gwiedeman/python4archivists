import csv
from DACS import iso2DACS

windowsPath = "C:\\Users\\[USERNAME]\\python4archivists\\executedJuveniles.csv"
unixPath = "/home/[USERNAME]/python4archivists/executedJuveniles.csv"

csvFile = open(windowsPath, "r")
csvObject = csv.reader(csvFile)

#loop though the CSV file
for row in csvObject:
	print(row[2])
	
csvFile.close()

"""
#set and empty list and initialize the count at 0
newList = []
rowCount = 0

#open the original CSV again and read it
csvFile = open(windowsPath, "r")
csvObject = csv.reader(csvFile)

for row in csvObject:
	#count the number of times though the loop
	rowCount = rowCount + 1
	#if more than the first time though the loop
	if rowCount > 1:
		#make a list of the rowCount, the 3rd column, and the 4th column using the iso2DACS function
		rowList = [rowCount - 1, row[2], iso2DACS(row[3])]
		#append that list to the newList - its just a list of lists
		newList.append(rowList)

#close the original CSV file
csvFile.close()


newCSV = "C:\\Users\\[USERNAME]\\python4archivists\\csvDACS.csv"
#newCSV = "/home/[USERNAME]/python4archivists/csvDACS.csv"

newFile = open(newCSV, "wb")
newCSV = csv.writer(newFile, delimiter=',')
newCSV.writerows(newList)
newFile.close()
"""