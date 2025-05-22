from kaggle.api.kaggle_api_extended import KaggleApi
import kaggle

api = KaggleApi()
api.authenticate()

kaggle.api.dataset_download_files('picekl/geoplant', path='./data/geoplant', unzip=True)

