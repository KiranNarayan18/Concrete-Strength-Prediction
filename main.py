import sys
from ConcreteStrength.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ConcreteStrength.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ConcreteStrength.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from ConcreteStrength import logger, CustomException



if __name__ == '__main__':
    try:
        STAGE_NAME = 'DATA_INGESTION'        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = 'DATA_VALIDATION'
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")


        STAGE_NAME = 'Data Transformation'
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")


    except Exception as e:
        logger.error(CustomException(e, sys))
        raise e