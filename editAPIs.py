import requests
import json
from DACS import iso2DACS

#login data
backendURL = "http://localhost:8089"
user = "admin"
pw = "admin"
repoID = "2"
resourceNumber = "174"

#inital request for session
r = requests.post(backendURL + "/users/" + user + "/login", data = {"password":pw})

if r.status_code == 200:
	print ("Connection Successful")

	sessionID = r.json()["session"]
	headers = {'X-ArchivesSpace-Session':sessionID}
	
	resource = requests.get(backendURL + "/repositories/" + repoID + "/resources/" + resourceNumber,  headers=headers).json()
	
	for date in resource["dates"]:
		beginDate = date["begin"].split("T")[0]
		endDate = date["end"].split("T")[0]
		isoDate = beginDate + "/" + endDate
		date["expression"] = iso2DACS(isoDate)
	print (resource["dates"][0]["expression"])
	#jsonData = json.dump(resource)
	

else:
	print (r)
	