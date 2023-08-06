import pandas as pd
import os
import sys
from sklearn.linear_model import ElasticNet
import joblib

from ConcreteStrength import logger, CustomException
from ConcreteStrength.entity.config_entity import ModelTrainerConfig
from ConcreteStrength.config.configuration import ConfigurationManager


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        try:
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)


            train_x = train_data.drop([self.config.target_column], axis=1)
            test_x = test_data.drop([self.config.target_column], axis=1)
            train_y = train_data[[self.config.target_column]]
            test_y = test_data[[self.config.target_column]]


            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            lr.fit(train_x, train_y)

            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

        except Exception as e:
            logger.error(CustomException(e, sys))
            raise e
        

if __name__ == "__main__":
    try:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
    except Exception as e:
        raise e