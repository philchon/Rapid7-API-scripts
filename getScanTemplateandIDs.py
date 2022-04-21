import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

###### Username and password
userName = input("Username : ")
passWord = getpass("Password : ")


headers = {'Content-Type' : 'application/json'}

scanTemplateResponse = requests.get('https://console.domainname.com:port/api/3/scan_templates',verify=False, headers=headers, auth = HTTPBasicAuth(userName, passWord))
#   response = requests.get(api_url, headers=headers)

print(scanTemplateResponse.json())
json_data = scanTemplateResponse.json()
dicts = json_data

scanTemplateName = json_data['resources'][0]['name']
scanTemplateDescription= json_data['resources'][0]['description']
scanTemplateID = json_data['resources'][0]['id']

for scanTemplateData in dicts['resources']:
    print('The Scan Template ' + scanTemplateData['name'] + ' has the Scan Template ID of ' + scanTemplateData['id'])
