import requests
import json
import sys
sys.path.append('../mev/')
import find_mev_kprove_uniswapv2


ADDRESS = sys.argv[1]

if  __name__ == "__main__":
    commandData = requests.get(ADDRESS + "getData/2").text
    commandJson = json.loads(commandData)
    # do something with it at this point
    resp = {"key": "value"}
    commandResponse = requests.post(ADDRESS, data = resp) 


