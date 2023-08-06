import sys
import pandas as pd
from ConcreteStrength import logger, CustomException
from ConcreteStrength.entity.config_entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            all_dtypes = data.dtypes
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    if str(all_dtypes[col]) == self.config.all_schema[col]:
                        
                        validation_status = True
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            logger.error(CustomException(e, sys))
            raise e