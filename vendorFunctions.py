### Function definitions for getting Vendor items

import requests_oauthlib 
import json
from os import getcwd

def getBansheeItems() -> str:
    jsonFile = open(getcwd() + "DestinyVendorInfo.json", 'r')
    jsonData = json.loads(jsonFile.read())
    jsonFile.close()
    
    # Get Banshee's ID
    bansheeId = jsonData["Vendors"][1]["ID"]

    # Make the vendor request

    # Banshee's items are indexed the same always?
    bansheeItemIds = jsonData["Vendors"][1]["DataKeys"]

    # Extract the ItemHash keys
    # itemHashes = [itemHash in hashes for hashes in ["Response"]["sales"][bansheeItemIds]["itemHash"]]

    # Get the itemHash name
    pass

def getXurItems() -> str:
    pass