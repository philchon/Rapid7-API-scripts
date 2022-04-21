import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass


###### Username and password
userName = input("Username : ")
passWord = getpass("Password : ")

###### Headers
headers = {'Content-Type' : 'application/json'}



###### Building the post data
siteName = input("What is the scan site name? : ")
targetsIPAddress = input("What are the IP addresses you would like to scan? : ")
scanTemplateID = input("What is the scan template you would like to
use? (Use scan template ID!) : ")
scanEngineID = input("Which scan engine you would like to use? (Use
scan engine ID!) : ")
scanDescription = input("What is the description of this scan site? : ")
scanImportance = input("What is the importance of this site? (Valid
values are very_low, low, normal, high, and very_high) : ")
stringTargetsIPAddress = str(targetsIPAddress)

postRequest = {"name" : siteName,
               "engineID" : scanEngineID,
               "description" : scanDescription,
               "importance" : scanImportance,
               "scan" : {
                    "assets" : {
                         "includedTargets" : {
                              "addresses" : [targetsIPAddress],
                         },
                    },
               },
               "scanTemplateId": scanTemplateID}



###### API endpoint + TLS certificate bypass
createScanSite =
requests.post('https://console.domainname.com:port/api/3/sites',
verify=False, headers=headers, json=postRequest, auth = HTTPBasicAuth
(userName, passWord))
#   response = requests.get(api_url, headers=headers)

###### Converting response into JSON then printing
#print(createScanSite) - printing this line is no longer needed but can be turned on if you want to see the api 201 response

###### Parsed the scan site ID off the API response
returned_json_data = createScanSite.json()
newlyGeneratedScanSiteID = returned_json_data['id']
createdSitesWithScanID =
'https://console.domainname.com:port:3780/api/3/sites/' +
str(newlyGeneratedScanSiteID) + '/scans'
###### Creating a post request to start the scan

startScanPostRequest = {"assetGroupIds" : [],
                        "engineId " : scanEngineID,
                        "hosts" : [
                           targetsIPAddress
                       ],
                       "name" : siteName,
                       "templateId": scanTemplateID
                       }
###### API  request to start the scan
startScanSite = requests.post(createdSitesWithScanID, verify=False,
headers=headers, json=startScanPostRequest, auth = HTTPBasicAuth
(userName, passWord))
print(startScanSite)
#print(startScanSite.json())
if startScanSite.status_code == 201:
    print('API request successfull and scan has started')
else:
    print(startScanSite.json())
    print('Review response code and json message above')
print('This scan site URL is :
https://console.domainname.com:port/site.jsp?siteid=' +
str(newlyGeneratedScanSiteID))
