from urllib.parse import urlparse
import os
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from src.data_science_project.utils.common import save_json
from src.data_science_project.entity.config_entity import ModelEvaluationConfig
from src.data_science_project import logger

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

from dotenv import load_dotenv
load_dotenv()

os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLFLOW_TRACKING_URI")
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")


# mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
mlflow.set_experiment("data-science-project")



class ModelEvaluation:
    def __init__(self,
                 config: ModelEvaluationConfig):
        self.config = config
    
    def evaluate_model(self):
        test_data = pd.read_csv(self.config.test_data_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        model = joblib.load(self.config.model_path)
        
        logger.info("Data and Model Loaded")
        
        predicted_qualities = model.predict(test_x)
        
        rmse = np.sqrt(mean_squared_error(predicted_qualities, test_y))
        mae = mean_absolute_error(predicted_qualities, test_y)
        r2 = r2_score(predicted_qualities, test_y)
        
        #Save metrics locally
        scores = {
            "rmse": rmse, "mae": mae, "r2": r2
        }
        save_json(path=Path(self.config.metric_file_path), data=scores)
        
        
        with mlflow.start_run():
            # log metrics
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            
            logger.info("Evaluation metrics are logged to MLFlow")
            
            # log model
            tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            signature = infer_signature(test_x, test_y)
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "ElasticNetModel", signature=signature, input_example=test_x)
                logger.info("Model is logged to MLFlow")
            else:
                mlflow.sklearn.log_model(model, "ElasticNetModel", signature=signature)
                
            
        
        