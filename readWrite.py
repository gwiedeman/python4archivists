#enter a path to the example text file here
windowsPath = "C:\\Users\\[USERNAME]\\python4archivists\\example.txt"
unixPath = "/home/[USERNAME]/python4archivists/example.txt"

fileObject = open(windowsPath, "r")

textString = fileObject.read()
print(textString)

#make the textString variable equal the same string plus more text
textString = textString + "\nAdd another line here!"

#print the new string
print(textString)

#remember to close the file
fileObject.close()

"""
saveDir = "newFile.txt"
file2 = open(saveDir, "w")
file2.write(textString)
file2.close()
"""