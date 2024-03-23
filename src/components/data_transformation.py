import os
import sys
import numpy as np
import logging
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import pickle
from scipy.sparse import csr_matrix
from exception import CustomException
from logger import logging
from utils import save_object
from sklearn.preprocessing import StandardScaler
from scipy.sparse import issparse




@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")

class CustomException(Exception):
    pass

def save_object(file_path, obj):
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = ["gender", "race_ethnicity", "parental_level_of_education",
                                   "lunch", "test_preparation_course"]

            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="median")),
                ('scaler', StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="most_frequent")),
                ('one_hot_encoder', OneHotEncoder()),
                ('scaler', StandardScaler())
            ])

            logging.info("Numerical columns standard scaling completed")
            logging.info("Categorical columns encoding")

            preprocessor = ColumnTransformer(transformers=[
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
     try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        logging.info("Read train and test data completed")
        logging.info("Obtaining preprocessing object")

        preprocessing_obj = self.get_data_transformer_object()
        target_column_name = "math_score"
        numerical_columns = ["writing_score", "reading_score"]
        categorical_columns = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]

        # Extract input features and target feature
        input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
        target_feature_train_df = train_df[target_column_name]
        input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
        target_feature_test_df = test_df[target_column_name]

        logging.info("Applying preprocessing object on training dataframe and test dataframe")
        train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
        test_arr = preprocessing_obj.transform(input_feature_test_df)

        logging.info("Saving preprocessing object")
        save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj=preprocessing_obj)
        

        return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path

     except Exception as e:
        
        raise CustomException(e)
