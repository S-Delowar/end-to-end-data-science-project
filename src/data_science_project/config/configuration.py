from src.data_science_project.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelEvaluationConfig, ModelTrainerConfig
from src.data_science_project.constant import *
from src.data_science_project.utils.common import read_yaml, create_directories



class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        
        create_directories([self.config.artifacts_root])
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        create_directories([self.config.data_ingestion.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= self.config.data_ingestion.root_dir,
            source_url=self.config.data_ingestion.source_url,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )        
        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_file_dir=config.unzip_file_dir,
            status_file_dir=config.status_file_dir,
            schema=schema,
        )
        return data_validation_config
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )
        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
        )
        return model_trainer_config
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path = config.test_data_path,
            model_path = config.model_path,
            metric_file_path = config.metric_file_path,
            params = params,
            target_column = schema.name
        )
        return model_evaluation_config