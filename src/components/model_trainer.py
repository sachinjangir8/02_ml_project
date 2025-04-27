# here we will train our model...
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import custom_exception
from src.loger import logging
from src.utils import save_object,evaluate_madel

@dataclass
class Modeltrainerconfig:
    trained_moedl_file_path=os.path.join("artifacts","model.pkl")

class Model_traner:
    def __init__(self):
        self.model_trainer_config=Modeltrainerconfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("split training and test input data ")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                "RandomForestRegressor":RandomForestRegressor(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "LinearRegression":LinearRegression(),
                "KNeighborsRegressor":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatBoostRegressor":CatBoostRegressor(verbose=False),
                "AdaBoostRegressor":AdaBoostRegressor()
            }
            Model_report:dict=evaluate_madel(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)

            # to get best score values... from dist
            best_model_score=max(sorted(Model_report.values()))

            # to get best model name...
            best_model_name=list(Model_report.keys())[
                list(Model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise custom_exception("NO BEST MODEL FOUND")
            logging.info(f"best model found for the trainging and testing  dataset..")

# it is to save the model path..
            save_object(
                file_path=self.model_trainer_config.trained_moedl_file_path,
                obj=best_model 

            )
            predicted=best_model.predict(x_test)
            r2_scr=r2_score(y_test,predicted)
            return r2_scr
        except Exception as e:
            raise custom_exception(e,sys)