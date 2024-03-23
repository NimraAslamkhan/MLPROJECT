import os
import sys
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from data_transformation import DataTransformation  
from exception import CustomException 
 

logging.basicConfig(level=logging.INFO)

class DataIngestionConfig:
    def __init__(self, train_data_path=os.path.join("artifacts", "train.csv"),
                       test_data_path=os.path.join("artifacts", "test.csv"),
                       raw_data_path=os.path.join("artifacts", "data.csv")):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.raw_data_path = raw_data_path

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion component")
        try:
            df = pd.read_csv(r"E:\githubprectiece\notebook\data\student csv.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion data is completed")
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    
data_transformation = DataTransformation()
data_transformation.initiate_data_transformation(train_data, test_data)