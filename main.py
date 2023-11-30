from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.exception import SensorException
from sensor.utils.main_utils import read_yaml_file
import os,sys

def set_env_variable(env_file_path):
    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL'] = env_config['MONGO_DB_URL']

if __name__== '__main__':
    try:
        env_file_path=os.path.join(os.getcwd(),"env.yaml")
        set_env_variable(env_file_path=env_file_path)
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        raise SensorException(e,sys)
    