#enter a path to the example text file here
myPath = "C:\\Users\\[username]\\python4archivists\\example.txt"

fileObject = open(myPath, "r")

textString = fileObject.read()
print(textString)

#make the textString variable equal the same string plus some more text
textString = textString + "\nAdd another line here!"

#print the new string
print(textString)

#remember to close the file
fileObject.close()

"""
saveDir = "C:\\Users\\[username]\\python4archivists\\newFile.txt"
file2 = open(saveDir, "w")
file2.write(textString)
file2.close()
"""