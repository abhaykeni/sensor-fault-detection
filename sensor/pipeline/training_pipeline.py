from sensor.entity.config_entity import (TrainingPipelineConfig,DataIngestionConfig, DataValidationConfig,DataTransformationConfig,
                                         ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig)
from sensor.entity.artifact_entity import (DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact,
                                           ModelTrainerArtifact,ModelEvaluationArtifact,ModelPusherArtifact)
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evaluation import ModelEvaluation
from sensor.components.model_pusher import ModelPusher
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging

class TrainPipeline:

    is_pipeline_running = False
    
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
    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            self.data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_transformation(self, data_validation_artifact:DataValidationArtifact)->DataTransformationArtifact:
        try:
            self.data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                                                              data_transformation_config=self.data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_trainer(self, data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            self.model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config,
                                         data_transformation_artifact= data_transformation_artifact)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_evaluation(self,data_validation_artifact:DataValidationArtifact,
                               model_trainer_artifact:ModelTrainerArtifact)->ModelEvaluationArtifact:
        try:
            self.model_evaluation_config = ModelEvaluationConfig(training_pipeline_config=self.training_pipeline_config)
            model_evaluation = ModelEvaluation(model_evaluation_config=self.model_evaluation_config,
                                               data_validation_artifact=data_validation_artifact,
                                               model_trainer_artifact=model_trainer_artifact)
            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()
            return model_evaluation_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_pusher(self,model_evaluation_artifact:ModelEvaluationArtifact)->ModelPusherArtifact:
        try:
            self.model_pusher_config = ModelPusherConfig(training_pipeline_config=self.training_pipeline_config)
            model_pusher = ModelPusher(model_evaluation_artifact=model_evaluation_artifact,
                                       model_pusher_conifg=self.model_pusher_config)
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    
    def sync_artifact_dir_to_s3(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def sync_saved_model_dir_to_s3(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
        
    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_validation_artifact:DataValidationArtifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact:DataTransformationArtifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact:ModelTrainerArtifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            model_evaluation_artifact:ModelEvaluationArtifact = self.start_model_evaluation(data_validation_artifact=data_validation_artifact,
                                                                                            model_trainer_artifact=model_trainer_artifact)
            if not model_evaluation_artifact.is_model_accepted:
                raise Exception("Trained Model is not better than the Best Model")
            model_pusher_artifact:ModelPusherArtifact = self.start_model_pusher(model_evaluation_artifact=model_evaluation_artifact)
            TrainPipeline.is_pipeline_running = False
            self.sync_artifact_dir_to_s3()
            self.sync_saved_model_dir_to_s3()
        except Exception as e:
            self.sync_artifact_dir_to_s3()
            TrainPipeline.is_pipeline_running = False
            raise SensorException(e,sys)
