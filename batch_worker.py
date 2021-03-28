import requests
import json
import sys
sys.path.append('../mev/')
from find_mev_kprove_uniswapv2 import reordering_mev


ADDRESS = sys.argv[1]

if  __name__ == "__main__":
    commandData = requests.get(ADDRESS + "getData/2").text
    commandJson = json.loads(commandData)
    # do something with it at this point
    temp = open("temp.txt", "w")
    temp.write(command_json['spec_file'])
    reordering_mev(commandJson['transactions'], "temp.txt", "out.txt", commandJson['acc'], commandJson['tokens'], commandJson['balances'], commandJson['pre_price'], commandJson['post_price'])

    resp = {"key": "value"}
    commandResponse = requests.post(ADDRESS, data = resp) 


