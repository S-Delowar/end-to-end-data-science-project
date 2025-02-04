import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_science_project import logger

import os
from src.data_science_project.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
    
    def transform_data(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Splitted data into train and test sets")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")
