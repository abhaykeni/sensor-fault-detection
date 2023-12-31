from sensor.entity.artifact_entity import ModelTrainerArtifact,DataValidationArtifact,ModelEvaluationArtifact
from sensor.entity.config_entity import ModelEvaluationConfig
from sensor.ml.model.estimator import TargetValueMapping
from sensor.utils.main_utils import save_object, load_object,write_yaml_file
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.exception import SensorException
from sensor.ml.model.estimator import SensorModel, ModelResolver
from sensor.logger import logging
from sensor.constant.training_pipeline import TARGET_COLUMN
import pandas as pd
import sys, os


class ModelEvaluation:

    def __init__(self,model_evaluation_config:ModelEvaluationConfig, data_validation_artifact:DataValidationArtifact,
                 model_trainer_artifact:ModelTrainerArtifact) -> None:
        try:
            self.model_evaluation_config = model_evaluation_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    
    def initiate_model_evaluation(self)->ModelEvaluationArtifact:
        try:
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path

            train_df = pd.read_csv(filepath_or_buffer=valid_train_file_path)
            test_df = pd.read_csv(filepath_or_buffer=valid_test_file_path)

            df = pd.concat([train_df,test_df],axis=0)
            y_true = df[TARGET_COLUMN]
            y_true.replace(TargetValueMapping().to_dict(),inplace=True)
            df.drop(TARGET_COLUMN,axis=1,inplace=True)

            train_model_file_path = self.model_trainer_artifact.trained_model_file_path
            model_resolver = ModelResolver()
            is_model_accepted = True

            if not model_resolver.is_model_exist():
                model_evaluation_artifact = ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted,
                    changed_accuracy= None,
                    best_model_path= None,
                    trained_model_path= train_model_file_path,
                    train_model_metric_artifact= self.model_trainer_artifact.test_metric_artifact,
                    best_model_metric_artifact= None
                                                                    )
                logging.info(f"Model Evaluation Artifact:{model_evaluation_artifact}")
                return model_evaluation_artifact

            logging.info(f"{df.head}")

            latest_model_path = model_resolver.get_best_model_path()
            latest_model = load_object(filepath=latest_model_path)
            logging.info(f"Latest_model:{latest_model}")
            trained_model = load_object(filepath=train_model_file_path)
            logging.info(f"Trained_model:{trained_model}")

            y_trained_pred = trained_model.predict(df)
            logging.info(f"y_trained_pred:{y_trained_pred}")
            y_latest_pred = latest_model.predict(df)
            logging.info(f"y_latest_pred:{y_latest_pred}")

            trained_metric = get_classification_score(y_pred=y_trained_pred,y_true=y_true)
            latest_metric = get_classification_score(y_pred=y_latest_pred,y_true=y_true)

            improved_accuracy = trained_metric.f1_score - latest_metric.f1_score

            if improved_accuracy > self.model_evaluation_config.changed_threshold:
                is_model_accepted = True
            else:
                is_model_accepted = False

            model_evaluation_artifact = ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted,
                    changed_accuracy= improved_accuracy,
                    best_model_path= latest_model_path,
                    trained_model_path= train_model_file_path,
                    train_model_metric_artifact= trained_metric,
                    best_model_metric_artifact= latest_metric
                                                                    )
            
            model_eval_report = model_evaluation_artifact.__dict__

            write_yaml_file(filepath=self.model_evaluation_config.report_file_path,content=model_eval_report)

            logging.info(f"Model Evaluation Artifact: {model_evaluation_artifact}")
            return model_evaluation_artifact
        
        except Exception as e:
            raise SensorException(e,sys)
        
    