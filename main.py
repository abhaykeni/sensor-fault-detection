from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.exception import SensorException
import os,sys
if __name__== '__main__':
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        raise SensorException(e,sys)
    