import os
import sys

from ConcreteStrength.constants import *
from ConcreteStrength import logger, CustomException
from ConcreteStrength.utils.common import get_size
from ConcreteStrength.config.configuration import ConfigurationManager
from ConcreteStrength.components.data_ingestion import DataIngestion


STAGE_NAME = 'DATA_INGESTION'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass    

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_files()

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(CustomException(e, sys))
        raise e