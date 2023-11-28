from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact,ModelTrainerArtifact,ModelEvaluationArtifact,ModelPusherArtifact
from sensor.components.data_ingestion import DataIngestion
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging

class TrainPipeline:

    def __init__(self) -> None:
        self.training_pipeline_config = TrainingPipelineConfig()
        

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Start data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and data ingestion artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
    
    def start_data_validation(self)->DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_transformation(self)->DataTransformationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_trainer(self)->ModelTrainerArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_evaluation(self)->ModelEvaluationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_pusher(self)->ModelPusherArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)
