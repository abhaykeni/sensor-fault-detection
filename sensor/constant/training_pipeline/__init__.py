import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME


SAVED_MODEL_DIR:str = os.path.join('saved_models')

# Defining common constants for training pipeline
TARGET_COLUMN = 'class'
PIPELINE_NAME:str = 'sensor'
ARTIFACT_DIR:str = 'artifact'
FILE_NAME:str = 'sensor.csv'

TRAIN_FILE_NAME:str = 'train.csv'
TEST_FILE_NAME:str = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME:str = 'preprocessing.pkl'
MODEL_FILE_NAME:str = 'model.pkl'
SCHEMA_FILE_PATH:str = os.path.join('config','schema.yaml')
SCHEMA_DROP_COLS:str = 'drop_columns'


# Defining constants for data ingestion pipeline

DATA_INGESTION_COLLECTION_NAME:str = 'sensor'
DATA_INGESTION_DIR_NAME:str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
DATA_INGESTION_INGESTED_DIR:str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2 


# Defining constants for data validation pipeline

DATA_VALIDATION_DIR:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = 'validated'
DATA_VALIDATION_INVALID_DIR:str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = 'reprt.yaml'


# Defining constants for data transformation pipeline
DATA_TRANSFORMATION_DIR_NAME:str = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DIR:str = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = 'transformed_object'


# Defining constants for model trainer pipeline
MODEL_TRAINER_DIR_NAME:str = 'model_trainer'
MODEL_TRAINER_TRAINED_MODEL_DIR:str = 'trained_model'
MODEL_TRAINER_TRAINED_MODEL_NAME:str = 'model.pkl'
MODEL_TRAINER_EXPECTED_SCORE:float = 0.6
MODEL_TRAINER_OVER_AND_UNDER_FITTING_THRESHOLD:float = 0.05


#Defining constants for model evaluation
MODEL_EVALUATION_DIR_NAME:str = 'model_evaluation'
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE:float = 0.02
MODEL_EVALUATION_REPORT_FILE_NAME:str = 'report.yaml'


# Defining constants for model pusher

MODEL_PUSHER_DIR_NAME:str = 'model_pusher'
MODEL_PUSHER_SAVED_MODEL_DIR:str = SAVED_MODEL_DIR
