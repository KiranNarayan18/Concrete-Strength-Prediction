import os
import sys

from ConcreteStrength.constants import *
from ConcreteStrength import logger, CustomException
from ConcreteStrength.utils.common import get_size
from ConcreteStrength.config.configuration import ConfigurationManager
from ConcreteStrength.components.data_validation import DataValiadtion


STAGE_NAME = 'DATA_VALIDATION'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass    

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            logger.error(CustomException(e, sys))
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(CustomException(e, sys))
        raise e