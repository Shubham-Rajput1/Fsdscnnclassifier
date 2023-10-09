from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import stage_03_train
from CNNClassifier import logger




config = ConfigurationManager()
    
training_config = config.get_training_config()
training = Training(config=training_config)
training.get_base_model()
training.train_valid_generator()