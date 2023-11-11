#CHATGPT API KEY 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
#Buycot API Access token TB1g4mG7r2LjST04BSrLx-BtWdThbynryW-DUKm4
#Access Token Secret     zJMDNYr8RgSB63V820iTVmZRLgjgsoBYeCffMSHw
#Buycot Documentation    https://www.buycott.com/api/docs




#import openai
import os
#import pandas as pd
import time
import requests
import json

#openai.api_key = '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'

barcodeSession = requests.Session()
BARCODE_API_URL = "https://www.buycott.com/api/v4/products/lookup"
BARCODE_ACCESS_TOKEN = "TB1g4mG7r2LjST04BSrLx-BtWdThbynryW-DUKm4"


def grabItemName(barcodeID: str):
    params = { 
               "barcode": barcodeID,
               "access_token": BARCODE_ACCESS_TOKEN
              }

    headers = {
        "Content-Type": "application/json"
    }

    response = barcodeSession.get(BARCODE_API_URL, headers=headers, params=params)



    if response.status_code == 200:
        # If the response is in JSON format, use response.json()
        #data = response.json()
        data = response.json()

        # print(data)
        try:
         product_name = data["products"][0]["product_name"]
         return product_name
        
        except KeyError:
         print("ID doesn't exist")
         return "ID doesn't exist"
        
    else:
        return "Error: Invalid barcode"

    
name = grabItemName("070942001472")
print(name)