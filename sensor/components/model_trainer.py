from sensor.entity.artifact_entity import ModelTrainerArtifact,DataTransformationArtifact
from sensor.entity.config_entity import ModelTrainerConfig
from sensor.utils.main_utils import load_numpy_array_data
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.exception import SensorException
from sensor.ml.model.estimator import SensorModel
from sensor.utils.main_utils import load_object,save_object
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
            classification_train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)

            if classification_train_metric < self.model_trainer_config.expected_accuracy:
                raise Exception("Trained model is not good to provide expected accuracy")

            y_test_pred = model.predict(X_test)
            classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            diff =  abs(classification_train_metric.f1_score-classification_test_metric.f1_score)

            if diff > self.model_trainer_config.under_and_over_fitting_threshold:
                raise Exception("Model is not goood.Try to improve with more experimentation.")
            
            preprocessor = load_object(filepath=self.data_transformation_artifact.transformed_object_file_path)
            sensor_model = SensorModel(preprocessor=preprocessor, model=model)

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path,exist_ok=True)
            save_object(filepath=self.model_trainer_config.trained_model_file_path, obj=sensor_model)

            #Model Trainer Artifact

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                                 test_metric_artifact=classification_train_metric,
                                 test_metric_artifact=classification_test_metric)

            return model_trainer_artifact
        
        except Exception as e:
            raise SensorException(e,sys)