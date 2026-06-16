import json
import pickle
import numpy as np
import os

__location = None
__model = None
__data_columns = None


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __location
    global __model
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_DIR = os.path.join(BASE_DIR, "model")
     # If your folder is named Model, use "Model"
    with open(os.path.join(MODEL_DIR, "columns.json"), "r") as f:
        __data_columns = json.load(f)["columns"]
        __location = __data_columns[3:]
    with open(os.path.join(MODEL_DIR, "model.pkl"), "rb") as f:
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
