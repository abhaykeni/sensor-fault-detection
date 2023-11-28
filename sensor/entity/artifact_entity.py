from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:...


@dataclass
class DataTransformationArtifact:...


@dataclass
class ModelTrainerArtifact:...



@dataclass
class ModelEvaluationArtifact:...



@dataclass
class ModelPusherArtifact:...

