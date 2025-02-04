import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from src.data_science_project.utils.common import save_json
from src.data_science_project.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self,
                 config: ModelEvaluationConfig):
        self.config = config
    
    def evaluate_model(self):
        test_data = pd.read_csv(self.config.test_data_path)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        model = joblib.load(self.config.model_path)
        
        predicted_qualities = model.predict(test_x)
        
        rmse = np.sqrt(mean_squared_error(predicted_qualities, test_y))
        mae = mean_absolute_error(predicted_qualities, test_y)
        r2 = r2_score(predicted_qualities, test_y)
        
        #Save metrics locally
        scores = {
            "rmse": rmse, "mae": mae, "r2": r2
        }
        save_json(path=Path(self.config.metric_file_path), data=scores)
        
        