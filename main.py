from src.data_science_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from src.data_science_project.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.data_science_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.data_science_project.pipeline.data_validation_pipeline import DataValidationPipeline
from src.data_science_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.data_science_project import logger


try: 
    logger.info(f"================ Data Ingestion Stage Starts ================")   
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info("================ Data Ingestion Stage Completed ================")
except Exception as e:
    raise e

try: 
    logger.info(f"================ Data Validation Stage Starts ================")   
    data_ingestion_pipeline = DataValidationPipeline()
    data_ingestion_pipeline.initiate_data_validation()
    logger.info("================ Data Validation Stage Completed ================")
except Exception as e:
    raise e

try: 
    logger.info(f"================ Data Transformation Stage Starts ================")   
    data_ingestion_pipeline = DataTransformationPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info("================ Data Transformation Stage Completed ================")
except Exception as e:
    raise e

try:
    logger.info(f"================ Model Training Stage Starts ================")   
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info("================ Model Training Stage Completed ================")
except Exception as e:
    raise e

try:
    logger.info(f"================ Model Evaluation Stage Starts ================")   
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info("================ Model Evaluation Stage Completed ================")
except Exception as e:
    raise e