import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.components.exception import CustomException
from sklearn.metrics import mean_squared_error

def save_object(file_path, obj):
 try:    
    dir_path=os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)


    with open(file_path, 'wb') as file_obj:
        dill.dump(obj, file_obj)
 except Exception as e:
    raise CustomException(e, sys)
 
 

from sklearn.metrics import mean_squared_error

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluate different machine learning models.
    
    Parameters:
        X_train (array-like): Training features.
        y_train (array-like): Training labels.
        X_test (array-like): Testing features.
        y_test (array-like): Testing labels.
        models (dict): Dictionary containing model names as keys and model objects as values.
        
    Returns:
        dict: Dictionary containing model names as keys and corresponding evaluation scores as values.
    """
    model_scores = {}
    
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = mean_squared_error(y_test, y_pred)
        model_scores[model_name] = score
        
        para=param[list(models.keys())[i]]

    
    return model_scores
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)