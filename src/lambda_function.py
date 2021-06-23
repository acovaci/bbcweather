from bbc_weather_scraper import LerwickWeatherScraper
from temperature_logger import RAN

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "message": RAN
    }