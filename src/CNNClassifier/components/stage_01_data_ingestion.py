import os
import urllib.request as request
from zipfile import ZipFile
from CNNClassifier import logger
from pathlib import Path
from tqdm import tqdm
from CNNClassifier.entity import DataIngestionConfig
from CNNClassifier.utils import utils

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        pass

    def download_file(self):
        pass
            
    def _get_updated_list_of_files(self):
        pass
    
    def _preprocess(self):
        pass

    def unzip_and_clean(self):
        pass