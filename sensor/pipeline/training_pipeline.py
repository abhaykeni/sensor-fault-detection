from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact,ModelTrainerArtifact,ModelEvaluationArtifact,ModelPusherArtifact
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging

class TrainPipeline:

    def __init__(self) -> None:
        self.training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Start data ingestion")
            logging.info("Data ingestion completed")
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
