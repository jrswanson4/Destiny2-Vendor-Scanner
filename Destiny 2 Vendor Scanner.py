from lxml import html
import requests
import json

HEADERS ={"X-API-Key": '4e149218cced48b5938726fc002a7201'} #Use your own API key here that you recieve from bungie

postmasterURL = "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/<Account type Here>/<Your Name Here>/"
print ("\n\nConnecting to Bungie:" + postmasterURL +"\n")
print ("Getting user data!")
res = requests.get(postmasterURL, headers = HEADERS)
print(res.json()) 

getCharacterInventory = "https://www.bungie.net/Platform/Destiny2/1/Profile/<Account #>/?components=201"
print ("\n\nConnecting to Bungie:" + getCharacterInventory +"\n")
print ("Getting user data!")

res = requests.get(getCharacterInventory, headers = HEADERS)
print(res.json())



