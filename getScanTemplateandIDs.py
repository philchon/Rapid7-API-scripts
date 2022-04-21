import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

###### Username and password
userName = input("Username : ")
passWord = getpass("Password : ")


headers = {'Content-Type' : 'application/json'}
###### API request
scanTemplateResponse = requests.get('https://console.domainname.com:port/api/3/scan_templates',verify=False, headers=headers, auth = HTTPBasicAuth(userName, passWord))
#   response = requests.get(api_url, headers=headers)

###### Returning the json response code and creating a dictionary for the json response
print(scanTemplateResponse.json())
json_data = scanTemplateResponse.json()
dicts = json_data

###### Parsing the data through the resources key
scanTemplateName = json_data['resources'][0]['name']
scanTemplateDescription= json_data['resources'][0]['description']
scanTemplateID = json_data['resources'][0]['id']

###### For loop to iterate through all of the scan templates and return back the name as well as the ID to use in the createScanSite script
for scanTemplateData in dicts['resources']:
    print('The Scan Template ' + scanTemplateData['name'] + ' has the Scan Template ID of ' + scanTemplateData['id'])
