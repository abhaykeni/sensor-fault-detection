from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.exception import SensorException
from sensor.logger import logging
import sys,os
import pandas as pd

class DataValidation:

    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig) -> None:
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(e,sys)


    @staticmethod
    def read_data(self,filepath)->pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise SensorException(e,sys)

    def validate_number_of_columns(self,dataframe)->bool:
        try:
            dataframe.columns()
        except Exception as e:
            raise SensorException(e,sys)

    def is_numerical_column_exist(self)->bool:
        pass

   
    def detect_dataset_drift(self):
        pass


    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path:str = self.data_ingestion_artifact.trained_file_path
            test_file_path:str = self.data_ingestion_artifact.test_file_path

            # Reading data from train and test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns


        except Exception as e:
            raise SensorException(e,sys)