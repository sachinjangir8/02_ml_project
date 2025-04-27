import os
import sys
import numpy as np
import pandas as pd
# it helps to create pkl file..
import dill 
from sklearn.metrics import r2_score

from src.exception import custom_exception

def save_object(file_path ,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open (file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise custom_exception(e,sys)

def evaluate_madel(x_train,y_train,x_test,y_test,models):
    try:
        reports={}
        for i in range(len(models)):
            model=list(models.values())[i]

            model.fit(x_train,y_train)

            y_train_prd=model.predict(x_train)
            y_test_prd=model.predict(x_test)

            train_model_score=r2_score(y_train,y_train_prd)

            test_model_score=r2_score(y_test,y_test_prd)

            reports[list(models.keys())[i]]=test_model_score

            return reports
    except Exception as e:
        raise custom_exception(e,sys)
