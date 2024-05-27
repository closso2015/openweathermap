import getopt,sys
import requests
import os
import json
from datetime import datetime
from datetime import date
import pytz
import re

api_key = None
openweathermap_url = "https://api.openweathermap.org/data/3.0/onecall?lat=44.26&lon=-70.5&exclude=minutely,hourly,daily&units=imperial&appid="

def usage():
    print("Options:")
    print("-h, --help          - Print help for this application")
    print("-k, --api-key       - API key to use with the specified user")

def main():
    global api_key

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hk", ["api-key=","help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err)) # will print something like "option -a not recognized"
        sys.exit(2)

    api_key = None

    try: 
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                return 0
       
            elif o in ("-k", "--api-key"):
                api_key = a

            else:
                print("Unhandled option %s" % (o))
                assert False, "unhandled option"
                
    except Exception as e:
        print("Failed in option processing %s" % (str(e)))
        usage()
        return 0

    if api_key == None :
        usage()
        return 0
   

    os.environ['REQUESTS_CA_BUNDLE'] = os.path.join( '/etc/pki/ca-trust/extracted/openssl/', 'ca-bundle.trust.crt')

    print("openweathermap_url: %s api-key: %s" % (openweathermap_url, api_key))


    #echo 'items.find({"repo":{"$eq":"carbonblack"},"@build.name":{"$eq" : "*"}}).include("name", "@build.name", "@build.number" ,"stat.downloads")' >./aql.query

    #https://artifactory-pub.bit9.local:5002/v2/_catalog

    #response = requests.post('https://' + artifactory + '/artifactory/api/search/aql', auth=(user, api_key), data=payload)
    response = requests.get(openweathermap_url + api_key)
    if response.status_code != 200:
        print("Request failed: %s" % (response.status_code))
        return
    wxdata_dictionary = json.loads(response.text)

    #print(registry_dictionary)
    # Iterating over registries
    for wxdata_elem in wxdata_dictionary.values():
        print(wxdata_elem)

    #process_repo(repo_dictionary['results'])

if __name__ == "__main__":
    main()
