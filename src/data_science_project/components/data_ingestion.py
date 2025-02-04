# Components- Data Ingestion

import os
from urllib import request
import zipfile
from src.data_science_project.entity.config_entity import DataIngestionConfig
from src.data_science_project import logger


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with info: \n{headers}")
        else:
            logger.info(f"File already exists")
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)