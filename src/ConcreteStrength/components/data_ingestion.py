import os
import sys
from urllib import request
import zipfile

from ConcreteStrength import logger, CustomException
from ConcreteStrength.utils.common import get_size
from ConcreteStrength.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url =self.config.source_URL,
                filename = self.config.local_data_file
            
            )

            logger.info(f"{filename} downloaded")

        else:
            logger.info(f"already exists")


    def extract_zip_files(self) -> None:
        """
        extraxts the zip files into a directory

        returns None
        """        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_path)
