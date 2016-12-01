import requests
import json
from DACS import iso2DACS

#login data
backendURL = "http://localhost:8089"
user = "admin"
pw = "admin"
repoID = "2"
resourceNumber = "2"

#inital request for session
connectASpace = requests.post(backendURL + "/users/" + user + "/login", data = {"password":pw})

if connectASpace.status_code == 200:
	print ("Connection Successful")

	sessionID = connectASpace.json()["session"]
	headers = {'X-ArchivesSpace-Session': sessionID}
	
	resource = requests.get(backendURL + "/repositories/" + repoID + "/resources/" + resourceNumber,  headers=headers).json()
	
	for date in resource["dates"]:
		beginDate = date["begin"].split("T")[0]
		endDate = date["end"].split("T")[0]
		isoDate = beginDate + "/" + endDate
		date["expression"] = iso2DACS(isoDate)
	print (resource["dates"][0]["expression"])
	
	#Always remember to .dumps()
	jsonData = json.dumps(resource)
	
	postResource = requests.post(backendURL + "/repositories/" + repoID + "/resources/" + resourceNumber,  headers=headers, data=jsonData)
	print (postResource.json()["status"])
	

else:
	print (connectASpace)