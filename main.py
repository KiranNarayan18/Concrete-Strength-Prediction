import sys
from ConcreteStrength.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ConcreteStrength import logger, CustomException

STAGE_NAME = 'DATA_INGESTION'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(CustomException(e, sys))
        raise e