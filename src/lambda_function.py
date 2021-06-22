from bbc_weather_scraper import LerwickWeatherScraper
import temperature_logger

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "message": LerwickWeatherScraper.get_todays_temperature()
    }