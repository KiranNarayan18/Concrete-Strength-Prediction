import sys
import os

from ConcreteStrength.constants import *
from ConcreteStrength.config.configuration import ConfigurationManager
from ConcreteStrength.components.data_transformation import DataTransformation
from ConcreteStrength import logger, CustomException

STAGE_NAME = 'Data Transformation'

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(CustomException(e, sys))
        raise e