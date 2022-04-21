import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

###### Username and password
userName = input("Username : ")
passWord = getpass("Password : ")

###### API endpoint + TLS certificate bypass
scanScanEngineResponse = requests.get('https://console.domainname.com:port/api/3/scan_engines',verify=False, headers=headers, auth = HTTPBasicAuth(userName, passWord))
#   response = requests.get(api_url, headers=headers)

###### Converting response into JSON then into a dictionary
print(scanScanEngineResponse.json())
json_data = scanScanEngineResponse.json()
dicts = json_data


###### fields such as scan engine name, IP address, and scan engine ID have been parsed
scanEngineName = json_data['resources'][0]['name']
scanEngineAddress = json_data['resources'][0]['address']
scanEngineID = json_data['resources'][0]['id']

###### tryin to print the scan engine data in one line

for scanEngineData in dicts['resources']:
    print('Scan Engine ID: ' + str(scanEngineData['id']) + '   | Scan Engine Name:  ' + scanEngineData['name'] + '     | Scan Engine IP Address : ' + str(scanEngineData['address']))
