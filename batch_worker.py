import requests
import json
import sys

ADDRESS = sys.argv[1]

if  __name__ == "__main__":
    commandData = requests.get(ADDRESS + "getData/2").text
    commandJson = json.loads(commandData)
    # do something with it at this point
    resp = {"key": "value"}
    commandResponse = requests.post(ADDRESS, data = resp) 


