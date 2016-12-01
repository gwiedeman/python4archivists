import json
from DACS import iso2DACS

#don't forget to change the path!
windowsPath = "C:\\Users\\[USERNAME]\\python4archivists\\resource.json"
unixPath = "/home/[USERNAME]/python4archivists/resource.json"

#open the file, load the json file into lists and dictionaries with .load()
jsonFile = open(windowsPath, "r")
jsonData = json.load(jsonFile)
jsonFile.close()

#lets take a look at what keys are in this file
print ("Here are the keys:")
for key in jsonData:
	print ("	" + key)
	
#looks like there is a "level" key and a "title" key
print ("\n\n" + jsonData["level"] + ": "+ jsonData["title"])

#there is also a notes key too, remove the # below to uncomment the line
#print (jsonData["notes"])

"""
print ("\nHere are the notes: ")
for note in jsonData["notes"]:
	print (note["type"])
	if note["type"] == "abstract":
		print (note["content"])
"""

#There are two sets of commente code above and below this line

"""
for date in jsonData["dates"]:
	beginDate = date["begin"].split("T")[0]
	endDate = date["end"].split("T")[0]
	isoDate = beginDate + "/" + endDate
	date["expression"] = iso2DACS(isoDate)
print (jsonData["dates"][0]["expression"])

#write the data back to a JSON file
output = open("newResource.json", "w")
json.dump(jsonData, output)
output.close()
"""