import requests
import json

#login data
backendURL = "http://localhost:8089"
user = "admin"
pw = "admin"

#inital request for session
r = requests.post(backendURL + "/users/" + user + "/login", data = {"password":pw})

if r.status_code == 200:
	print ("Connection Successful")

	sessionID = r.json()["session"]
	headers = {'X-ArchivesSpace-Session':sessionID}
	
	repoID = "2"
	resourceNumber = "174"
	resource = requests.get(backendURL + "/repositories/" + repoID + "/resources/" + resourceNumber,  headers=headers).json()
	
	

else:
	print (r)
	