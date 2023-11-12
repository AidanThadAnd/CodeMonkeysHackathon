import os
import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import gptResponse
# API for UPC lookup (100 LOOKUPS/DAY MAX) https://www.upcitemdb.com/wp/docs/main/development/


app = Flask(__name__)
CORS(app)


barcodeSession = requests.Session()
UPCITEMD_API_URL = "https://api.upcitemdb.com/prod/trial/lookup?upc=4002293401102"

#Takes barcode Number
#Returns name of product
@app.route('/grabItemName', methods=['POST'])
def grabItemName():
        try:
            request_data = request.get_json()
            barcodeID = request_data['barcode']
            
            print(barcodeID)
            UPCITEMD_API_URL = f"https://api.upcitemdb.com/prod/trial/lookup?upc={barcodeID}"

            headers = {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
              'Accept-Encoding': 'gzip,deflate',
            }

            response = barcodeSession.get(UPCITEMD_API_URL, headers=headers)

            if response.status_code == 200:
                data = response.json()
                try:
                 product_name = data["items"][0]["title"]
                 print(product_name)
                 disposablePrompt = print(gptResponse.how_to_dispose(product_name))
                 commonFixesPrompt = print(gptResponse.common_fixes(product_name))
                 return jsonify({"disposablePrompt": "disposablePrompt", "commonFixesPrompt": "commonFixesPrompt"})

                except KeyError:
                
                 return jsonify({"error": "Invalid barcode"})

            else:
                return jsonify({"error": "Invalid barcode"})
        
        except Exception as e:
            print(str(e))
            return jsonify({"error": "Error scanning barcode"}), 500

if __name__ == '__main__':
    app.run(debug=True)
