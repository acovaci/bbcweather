from bbc_weather_scraper import LerwickWeatherScraper


def lambda_handler(event, context):
    LerwickWeatherScraper.log_current_temperature()

    return {
        "statusCode": 200,
        "message": str(LerwickWeatherScraper.get_todays_temperature())
    }
