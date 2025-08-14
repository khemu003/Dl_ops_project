from src.CnnClassifer import logger
from src.CnnClassifer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CnnClassifer.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

logger.info("\n\n=================================================")

logger.info(">>>>>> Welcome to my personal Log <<<<<<")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model" 
try: 
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
    prepare_base_model = PrepareBaseModelTrainingPipeline() 
    prepare_base_model.main() 
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n") 
except Exception as e:
    logger.exception(e)
    raise e
