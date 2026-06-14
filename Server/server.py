from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)   # Enable CORS for all routes


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({
        'locations': util.get_location_names()
    })


@app.route('/predict_price', methods=['POST'])
def predict_price():

    data = request.get_json()

    location = data['location']
    sqft = float(data['sqft'])
    bath = int(data['bath'])
    bhk = int(data['bhk'])

    estimated_price = util.predict_price(
        location,
        sqft,
        bath,
        bhk
    )

    return jsonify({
        'estimated_price': estimated_price
    })


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)