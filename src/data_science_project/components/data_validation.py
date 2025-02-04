import pandas as pd
from src.data_science_project import logger
from src.data_science_project.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_file_dir)
            all_cols = list(data.columns)
            
            schema = self.config.schema.keys()

            for col in all_cols:
                if col not in schema:
                    validation_status = False
                    with open(self.config.status_file_dir, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                        
                else:
                    validation_status = True
                    with open(self.config.status_file_dir, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                        
            return validation_status
        
        except Exception as e:
            raise e