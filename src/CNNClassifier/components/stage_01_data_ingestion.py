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
        if not os.path.exists(self.config.local_data_file):
            logger.info("trying to download file")
            request.urlretrieve(
                url=self.config.Source_URL,
                filename=self.config.local_data_file
            )
            
        else:
            logger.info("file already exists")    
            
    def _get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if f.endswith("jpg")]
        
    
    def _preprocess(self,zf,f,working_dir):
        target_filepath=os.path.join(working_dir,f)
        if not os.path.exists(target_filepath):
            zf.extract(f,working_dir)

    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file,mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files=self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess()
                