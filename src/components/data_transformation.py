# this is for data transformation like..label encoding
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import custom_exception
from src.loger import logging

from src.utils import save_object

@dataclass
class DatatransformationConfig:
    preprocesser_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.Data_transfermation_config=DatatransformationConfig()

    def Get_data_transformation_obj(self):
        '''
        this function is responsible for data transformation : \n
        '''
        try:
            numaric_features=["writing_score","reading_score"]
            categorical_features=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            # Now creating a pipeline to handle missing values..
            numeric_pipline=Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy="median")),
                    ("Scaler",StandardScaler(with_mean=False))
                ]
            )
               
            cat_pipline=Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy='most_frequent')),
                    ("OneHotEncoder",OneHotEncoder()),
                    ("Scaler",StandardScaler(with_mean=False))   
                ]
            )

            logging.info(f"Numaric columns standrad scalling completed {numaric_features}"),
            logging.info(f"categorical columns encoding completed {categorical_features}")

        # To combine the numaric and categorical features...
            preprocessor=ColumnTransformer([
                ("numeric_pipline",numeric_pipline,numaric_features),
                ("cat_pipline",cat_pipline,categorical_features)
            ])
            return preprocessor
            
        except Exception as e:
            raise custom_exception(e,sys)
        
        # here we are going to data transformation..
    
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)

            logging.info(  "Read train ,test data is completed :" )
            logging.info(  "obtaining preprocessing object : " )
            preprocessing_obj=self.Get_data_transformation_obj()

            Target_col_name="math_score"
            numerical_col=["writing_score","reading_score"]

            input_feature_train_df=train_df.drop(columns=[Target_col_name],axis=1)
            Target_feature_train_df=train_df[Target_col_name]

            input_feature_test_df=test_df.drop(columns=[Target_col_name],axis=1)
            Target_feature_test_df=test_df[Target_col_name]

            logging.info(f"applying preprocessing obj on training dataframe and testing dataframe ..")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,np.array(Target_feature_train_df)
            ]
            test_arr=np.c_[
                input_feature_test_arr,np.array(Target_feature_test_df)
            ]
            logging.info("saving preprocessing objects ...")

            save_object(
                file_path=self.Data_transfermation_config.preprocesser_obj_file_path,
                obj=preprocessing_obj

            )

            return(
                train_arr,
                test_arr,
                self.Data_transfermation_config.preprocesser_obj_file_path,
            )
        except Exception as e:
            raise custom_exception(e,sys)
