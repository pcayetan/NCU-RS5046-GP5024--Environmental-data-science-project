from kaggle.api.kaggle_api_extended import KaggleApi
import kaggle

api = KaggleApi()
api.authenticate()

print(api.competition_download_cli(search='GeoLifeCLEF25'))
