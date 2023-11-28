from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.utils.main_utils import read_yaml_file
from sensor.exception import SensorException
from sensor.logger import logging
import sys,os
import pandas as pd

class DataValidation:

    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig) -> None:
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e,sys)


    @staticmethod
    def read_data(self,filepath)->pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise SensorException(e,sys)

    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self._schema_config['columns'])
            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e,sys)

    def is_numerical_column_exist(self,dataframe:pd.DataFrame)->bool:
        try:
            numerical_columns = self._schema_config['numerical_columns']
            dataframe_columns = dataframe.columns

            numerical_columns_present = True
            for col in numerical_columns:
                if col not in dataframe_columns:
                    numerical_columns_present = False
        except Exception as e:
            raise SensorException(e,sys)

   
    def detect_dataset_drift(self):
        pass


    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            error_message = ""
            train_file_path:str = self.data_ingestion_artifact.trained_file_path
            test_file_path:str = self.data_ingestion_artifact.test_file_path

            # Reading data from train and test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all columns."

            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test dataframe does not contain all columns."


        except Exception as e:
            raise SensorException(e,sys)