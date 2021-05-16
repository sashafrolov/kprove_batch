import requests
import json
import sys, os
sys.path.append('../mev/')
from find_mev_uniswapv2 import reordering_mev


ADDRESS = sys.argv[1]

if  __name__ == "__main__":
    index = os.getenv('AWS_BATCH_JOB_ARRAY_INDEX',2)

    commandData = requests.get(ADDRESS + "getData/{}".format(index)).text
    commandJson = json.loads(commandData)
    # os.system("kompile mev.k --backend haskell")

    reordering_mev(commandJson['transactions'], "bound.k", "out.txt", commandJson['acc'], commandJson['tokens'], commandJson['balances'], commandJson['pre_price'], commandJson['post_price'])

    result = open("out.txt")

    resp = {"result": result.read()}
    commandResponse = requests.post(ADDRESS + "postData/{}".format(index), data = resp)

