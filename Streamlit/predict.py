
import joblib 

import numpy as np




def predict_diabetes(input):
    dia_model = joblib.load('saved/DTree_model.pkl')
    predict = dia_model.predict(input)
    return predict

