import requests
import json
import sys, os, io
sys.path.append('../mev/')
from find_mev_uniswapv2 import reordering_mev


ADDRESS = sys.argv[1]

if  __name__ == "__main__":
    index = os.getenv('AWS_BATCH_JOB_ARRAY_INDEX',2)

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    commandData = requests.get(ADDRESS + "getData/{}".format(index)).text
    commandJson = json.loads(commandData)

    reordering_mev(commandJson['transactions'], "bound.k", "out.txt", commandJson['acc'], commandJson['tokens'], commandJson['balances'], commandJson['pre_price'], commandJson['post_price'], commandJson['pair_address'], commandJson['block'], commandJson['convergence'])

    sys.sdout = old_stdout
    result = buffer.getvalue()

    resp = {"result": result}
    commandResponse = requests.post(ADDRESS + "postData/{}".format(index), data = resp)

