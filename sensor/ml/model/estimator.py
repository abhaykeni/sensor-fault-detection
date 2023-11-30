class TargetValueMapping:

    def __init__(self) -> None:
        self.neg:int = 0
        self.pos:int = 1

    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))
    

class SensorModel:

    def __init__(self,preprocessor, model) -> None:
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise e
        
    def predict(self,x):
        try:
            x_transform = self.preprocessor.transformer(x)
            y_hat =  self.model.predict(x_transform)
        except Exception as e:
            raise e