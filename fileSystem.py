import os

import datetime
def humanTime(timestamp):
	return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

import platform
print("I am running a " + os.name + " system, specifically " + platform.system() + " " + platform.release())

directory = "C:\\Users\\[USERNAME]\\python4archivists"

#start our counting variables
folderCount = 0
fileCount = 0
#loop though everything in a directory with os.listdir()
for item in os.listdir(directory):
	
	#count each folder and file
	if os.path.isdir(item):
		folderCount = folderCount + 1
	elif os.path.isfile(item):
		fileCount = fileCount + 1

#print what we found to the command line		
print("Found " + str(folderCount) + " folders and " + str(fileCount) + " files")

"""
#find the exampleDir folder within our example files
for item in os.listdir(directory):
	if item == "exampleDir":
		
		#combine the original directory with this item and "WeMadeThis" into a path
		newFolderPath = os.path.join(directory, item, "WeMadeThis")
		#check if this new path exists and then make it
		if not os.path.exists(newFolderPath):
			os.mkdir(newFolderPath)
		
		#walk the directory to get lists of files and folders
		for rootDir, folders, files in os.walk(item):
			#loop through the list of files
			for file in files:
				#print the file name and full path
				print("filename: " + file)
				fullPath = os.path.join(rootDir, file)
				print("	path: " + fullPath)
				
				#print the file size
				print("	size: " + str(os.path.getsize(fullPath)))
				#print timestampes
				print("	Last Modified: " + humanTime(os.path.getmtime(fullPath)))
				print("	Last Accessed: " + humanTime(os.path.getatime(fullPath)))
				print("	Created: " + humanTime(os.path.getatime(fullPath)))
"""