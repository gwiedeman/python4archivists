from lxml import etree as ET

xmlPath = 'C:\\Projects\\python4archivists\\mets.xml'

xmlObject = ET.parse(xmlPath)
root = xmlObject.getroot()

count = 0
for player in root:
	count = count + 1
	if count < 15:
		print(player.find("name").text)

"""
FA_string = ET.tostring(FA, pretty_print=True, xml_declaration=True, encoding="utf-8", doctype="<!DOCTYPE ead SYSTEM 'ead.dtd'>")

print "writing " + eadFile
file = open(os.path.join(eadDir, eadFile), "w")
file.write(FA_string)
file.close()
"""