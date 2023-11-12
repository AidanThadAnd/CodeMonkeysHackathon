from flask import Flask, request, jsonify
import cv2
from pyzbar.pyzbar import decode

app = Flask(__name__)

# Endpoint to process barcode
@app.route('/scanBarcode', methods=['POST'])
def scan_barcode():
    try:
        # Get the image data from the request
        image_data = request.files['image'].read()

        # Convert the image data to a numpy array
        image_array = np.frombuffer(image_data, np.uint8)

        # Decode barcode using pyzbar
        decoded_objects = decode(cv2.imdecode(image_array, cv2.IMREAD_COLOR))

        if decoded_objects:
            barcode_data = decoded_objects[0].data.decode('utf-8')
            return jsonify({"barcodeData": barcode_data})
        else:
            return jsonify({"error": "No barcode found"})
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error scanning barcode"}), 500

if __name__ == '__main__':
    app.run(debug=True)