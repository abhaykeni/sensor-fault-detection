from sensor.exception import SensorException
import numpy as np
from sensor.logger import logging
import os,sys
import yaml
import dill


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
    

def save_numpy_array_data(filepath:str, array: np.array):
    """
    Save numpy array to data file
    filepath: str location of file to save
    array: np.arry data to save
    """
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath,'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise SensorException(e,sys)
    


def load_numpy_array_data(filepath:str)->np.array:
    """
    Load numpy array data from file
    filepath: str location of file to save
    return array: np.arry data laoded
    """
    try:
        with open(filepath,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise SensorException(e,sys)
    

def save_object(filepath:str, obj:object)->None:
    try:
        logging.info('Entered the save_object method of main utils class')
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info('Exited the save_object method of main utils class')
    except Exception as e:
        raise SensorException(e,sys)



