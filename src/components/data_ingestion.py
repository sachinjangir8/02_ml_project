#this is made for reading the database...... for trainging and testing
import os
import sys
from src.exception import custom_exception
from src.loger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
# IT IS USED TO CREATE A CLASS VARIABLE...
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DatatransformationConfig

from src.components.model_trainer import Modeltrainerconfig
from src.components.model_trainer import Model_traner

# if you do not want to use init to create a variablre then use @dataclass decoretor..
@dataclass
class DataInjectionConfig:
    # HERE WE SAVED OUR DATAINPUTES...
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    Raw_data_path:str = os.path.join('artifacts','data.csv')

class DataInjection:
    # HERE WE WILL DEFINE __INIT__ constructer WHEN WE NEED TO DEFINE OTHER FUNCTIONS IN CLASS
    def __init__(self):
        self.Injestion_config=DataInjectionConfig()

    def initiate_data_injection(self):
        logging.info("Entered the data injection method or components :")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe : ')
            #here we gave the parameter ..and creating a directory
            os.makedirs(os.path.dirname(self.Injestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.Injestion_config.Raw_data_path,index=False,header=True)
            logging.info('train test split initilized..')
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.Injestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.Injestion_config.test_data_path,index=False,header=True)
            logging.info('Injection of the data is completed..')
            return(
                self.Injestion_config.train_data_path,
                self.Injestion_config.test_data_path
            )
        except Exception as e:
            raise custom_exception(e,sys)
        
if __name__=="__main__":
    obj=DataInjection()
    train_data,test_data=obj.initiate_data_injection()

    Data_transformation=DataTransformation()
    train_arr,test_arr,_=Data_transformation.initiate_data_transformation(train_data,test_data)

    Model_traner=Model_traner()
    print(Model_traner.initiate_model_trainer(train_arr,test_arr))