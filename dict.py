#introduction to dictionaries

#a simple dictionary
dict = {"key1": "value", "key2": 1}

#a useful dictionary
calendar = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

#print the value for the key "04"
print (calendar["04"])

#both lists and dictionaries can be nested
collection = {"title": "Hugo A. Bedau Papers", "dates": "1957-2003 ", "extent": [36, "cubic ft."]}
series1 = {"title": "Scholarship and Teaching", "dates": "1958-2002", "extent": [6, "cubic ft."]}
series2 = {"title": "Correspondence", "dates": "1957-2003", "extent": [4, "cubic ft."]}
series3 = {"title": "Advocacy Organization", "dates": "1958-2003", "extent": [10, "cubic ft."]}
series4 = {"title": "Subject Files", "dates": "1955-2003", "extent": [16.79, "cubic ft."]}

#here is a list of the dictionaries above
fonds = [collection, series1, series2, series3, series4]

for resource in fonds:
	print (resource["title"] + ", " + resource["dates"])
	
	#the value of extent is a list
	for extent in resource["extent"]:
		print ("	" + str(extent))