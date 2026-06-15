import json
import pickle
import numpy as np

# Global variables to hold the model and data columns
__location = None
__model = None
__data_columns = None

# Function to load the saved model and data columns
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __model
    global __location

    with open("D:\Projects\Realestate model\Model\columns.json", "r") as f:
        __data_columns = json.load(f)['columns']
        __location = __data_columns[3:]  # Assuming the first 3 columns are sqft, bath, bhk
    with open("D:\Projects\Realestate model\Model\model.pkl", "rb") as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")

# Function to predict the price based on the input features
def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __location

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_data_columns())
    print(predict_price('1st Phase JP Nagar', 1000, 2, 2))
    print(predict_price('Indira Nagar', 1000, 2, 2))
    print(predict_price('Indira Nagar', 1000, 3, 3))
