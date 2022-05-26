import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_package(score_1,package_1,score_2,package_2,score_3,package_3,speed,satisfied_level):
 
    x = np.zeros(len(__data_columns))
    x[0] = score_1
    x[1] = package_1
    x[2] = score_2
    x[3] = package_2
    x[4] = score_3
    x[5] = package_3
    x[6] = speed
    x[7] = satisfied_level
    return str(__model.predict([x])[0])


def load_saved_artifacts():
    global  __data_columns
    if __data_columns is None:
        with open("columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('thesis.pickle', 'rb') as f:
            __model = pickle.load(f)


if __name__ == '__main__':
    load_saved_artifacts()