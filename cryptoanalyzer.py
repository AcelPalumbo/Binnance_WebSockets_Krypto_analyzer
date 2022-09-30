import websocket
import json
import pprint
import numpy
import talib
from binance.client import Client

def getcurrencylist(data,curr,wallet):
    list=[]
    for row in data:

        if row['symbol'][-3:] == curr:
            row["site"] = "right"
            row["right"]=row['symbol'][-3:]
            row["left"] = row['symbol'][:3]
            row["wallet"]=wallet /float(row["price"])

            list.append(row)
        if row['symbol'][:3] == curr:
            row["site"] = "left"
            row["left"]=row['symbol'][:3]
            row["right"] = row['symbol'][-3:]
            row["wallet"]=wallet*float(row["price"])
            list.append(row)
    return list
def multiply_currency(cur):
    print(cur)


config = open("config.json", "r")
configcontent = config.read()
configtoobjects = json.loads(configcontent)
#
ApiKey = configtoobjects['BinancApiKey']
SecretKey = configtoobjects['BinancSecretKey']
#
client = Client(ApiKey, SecretKey)
# client.API_URL = 'https://testnet.binance.vision/api'
info = client.get_all_tickers()
wallet = 20
eth = getcurrencylist(info,"ETH",wallet)

for row in eth:
    secondlist = []
    if row['site']=="left":
        secondlist=getcurrencylist(info,row["right"],row["wallet"])
        # for ro in secondlist:
        #     if row['site'] == "left":
        #         lastlist=
        #     else:

    else:
        secondlist = getcurrencylist(info, row["left"], row["wallet"])
    print(secondlist)
    print("@@@@")

print("-------------")
print(eth)
print("-------------")

