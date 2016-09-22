from lxml import etree as ET

#enter a path to the mets.xml XML file here
myPath = "C:\\Users\\[USERNAME]\\python4archivists\\apap159.xml"

parser = ET.XMLParser()
xmlObject = ET.parse(myPath, parser)

#root is the top-level <ead> tag
root = xmlObject.getroot()
print("tag is " + root.tag)
print("@id is " + root.attrib["id"])

#lets find out which collection this is
collectionName = root.find("archdesc/did/unittitle").text
print("We are working with " + collectionName)

print("\nHere is each series:")
#for each child element under ead/archdesc/dsc
for series in root.find("archdesc/dsc"):
	if series.tag == "c01":
		print(series.find("did/unittitle").text)

		
		#as long as we stay at this level of indentation, we can stay within the for loop
		#lets set the @series for each <c01> to "series"
		series.set("level", "series")
		
		#lets make some changes to the EAD file, maybe add a <physloc> element to each series did?
		newElement = ET.Element("physloc")
		newElement.text = "This series is located in out off-site storage facility. We know researchers love this, you're welcome."
		did = series.find("did")
		did.append(newElement)
		
#now things we enter at this indentation will run after the for loop completes
#lets look for our new element
for series in root.find("archdesc/dsc"):
	if series.tag == "c01":
		print("\nDoes " + series.find("did/unittitle").text + " have a <physloc>?")
		if series.find("did/physloc") == None:
			print("No! its does not, we made a mistake...")
		elif series.find("did/physloc").text == None:
			print("Its there, but it doesn't have any text.")
		else:
			print("Yes it does!")
	
"""
#Our xml file won't change unless we write back to the disk
outputFile = "C:\\Users\\[USERNAME]\\python4archivists\\newEAD.xml"
xmlString = ET.tostring(root, pretty_print=True, xml_declaration=True, encoding="utf-8", doctype="<!DOCTYPE ead SYSTEM 'ead.dtd'>")

print("writing " + outputFile)
file = open(outputFile, "w")
file.write(xmlString)
file.close()
"""