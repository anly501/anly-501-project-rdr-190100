import os
os.environ['KAGGLE_USERNAME'] = "ramdayalrewaria"
os.environ['KAGGLE_KEY'] = "6e978bf33cc1de47788eace91b812132"

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_download_files('fedesoriano/traffic-prediction-dataset', path=".")
