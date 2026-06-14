from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])  
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
    if request.method == 'GET':
        # Handle GET request
        location = request.form['location']
        sqft = float(request.form['sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])
    else:
        # Handle POST request
        data = request.get_json()
        location = data['location']
        sqft = data['sqft']
        bath = data['bath']
        bhk = data['bhk']

    response = jsonify({
        'estimated_price': util.predict_price(location, sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)