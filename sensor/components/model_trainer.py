from sensor.entity.artifact_entity import ModelTrainerArtifact,DataTransformationArtifact
from sensor.entity.config_entity import ModelTrainerConfig
from sensor.utils.main_utils import load_numpy_array_data
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.exception import SensorException
from sensor.logger import logging
import sys, os
from xgboost import XGBClassifier



class ModelTrainer:

    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifact:DataTransformationArtifact) -> None:
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise SensorException(e,sys)

    def train_model(self, x_train, y_train):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x_train,y_train)
            return xgb_clf
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:

            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            train_arr = load_numpy_array_data(filepath= train_file_path)
            test_arr = load_numpy_array_data(filepath=test_file_path)

            X_train = train_arr[:,:-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:,:-1]
            y_test = test_arr[:,-1]

            model = self.train_model(x_train=X_train,y_train=y_train)
            y_train_pred = model.predict(X_train)



        except Exception as e:
            raise SensorException(e,sys)