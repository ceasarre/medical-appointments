import numpy as np


# CONST FROM DATA ANALYZES IN ml_test dir
MAX_AGE = 102
MAX_MISSED = 18
MAX_DAY_DIFF = 179


def map_to_int(x):
    if x == True:
        return 1 
    else:
        return 0

def convert_handicap(x):
    if int(x) == 0:
        return np.array([1, 0, 0, 0, 0])
    elif int(x) == 1:
        return np.array([0, 1, 0, 0, 0])
    elif int(x) == 2:
        return np.array([0, 0, 1, 0, 0])
    elif int(x) == 3:
        return np.array([0, 0, 0, 1, 0])
    else:
        return np.array([0, 0, 0, 0, 1])
    


def prepare_vec(person):
    time_delta = (person.date_of_appointment - person.date_of_set_appointment).days
    data = []
    data.append(int(person.gender))
    data.append(int(person.age)/ MAX_AGE)
    data.append(map_to_int(person.scolarship))
    data.append(map_to_int(person.hipertension))
    data.append(map_to_int(person.diabetes))
    data.append(map_to_int(person.alcoholism))
    data.append(map_to_int(person.sms_received))
    data.append(int(person.num_app_missed) / MAX_MISSED)
    data.append(int(time_delta) / MAX_DAY_DIFF)
    handicap = convert_handicap(person.handicap)
    # Add handicap to data - todo
    data = np.array(data)
    data = np.concatenate((data, handicap))
    data = data.reshape(1,-1)

    return data

def predict(data):
    import pickle
    model = pickle.load(open("check_noshow/RFC_predictor.sav", "rb"))
    prediction = model.predict(data)
    
    if prediction == 1:
        return f'Pacjent się nie pojawi'
    else:
        return f'Pacjent się prawdopodbnie pojawi'

