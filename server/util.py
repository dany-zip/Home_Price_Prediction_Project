import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None          # 3 global variables are created


def get_estimated_price(location,sqft,bhk,bath):
    try:                                            #if error is found use try catch block
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1

    x = np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >= 0:
        x[loc_index]=1
    
    return round(__model.predict([x])[0],2)    #since predicted value is float so use round function to round of 2dp


def get_location_names():
    load_saved_artifacts()
    return __locations

def load_saved_artifacts():   # column.json and pickle file will be loaded

    # print("loading saved artifacts.......starts")
    global __data_columns
    global __locations

    with open("C:/Project/server/artifacts/columns.json",'r') as f:    # Opening columns.json file and 'read'
       #json.load(f)['data_columns']      # object which loaded will be converted into dict.
                                          # for that we are using 'data_columns' key from json file
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]     # from 3rd index we are taking because look at json file

    # LOAD SAVED PICKLE MODEL
    global __model
    with open("C:/Project/server/artifacts/Bengaluru", 'rb') as f:

        __model =pickle.load(f)
    # print("loading of artifacts is ......done")



if __name__=='__main__':
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('Lucknow',1000,2,2))  # Other Location
    print("objective_achieved")