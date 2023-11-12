import os
import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

import gptResponse

app = Flask(__name__)

CORS(app)

barcodeSession = requests.Session()
BARCODE_API_URL = "https://www.buycott.com/api/v4/products/lookup"
BARCODE_ACCESS_TOKEN = "TB1g4mG7r2LjST04BSrLx-BtWdThbynryW-DUKm4"

#Takes barcode Number
#Returns name of product
@app.route('/grabItemName', methods=['POST'])
def grabItemName():
        try:
            request_data = request.get_json()
            barcodeID = request_data['barcode']
            
            print(barcodeID)
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
                data = response.json()

                # print(data)
                try:
                 product_name = data["products"][0]["product_name"]

                 disposablePrompt = gptResponse.how_to_dispose(product_name)
                 commonFixesPrompt = gptResponse.common_fixes(product_name)
                 return jsonify({"disposablePrompt": disposablePrompt, "commonFixesPrompt": commonFixesPrompt})

                except KeyError:
                
                 return jsonify({"error": "No barcode found"})

            else:
                return jsonify({"error": "Invalid barcode"})
        
        except Exception as e:
            print(str(e))
            return jsonify({"error": "Error scanning barcode"}), 500

if __name__ == '__main__':
    app.run(debug=True)
