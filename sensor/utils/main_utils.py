from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
import yaml


def read_yaml_file(filepath:str)->dict:
    try:
        with open(filepath,'r') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise SensorException(e,sys)
    
def write_yaml_file(filepath:str, content:object, replace:bool=False):
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath, 'w') as file:
            yaml.dump(content,file)
    except Exception as e:
        raise SensorException(e,sys)