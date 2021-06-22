from scraper import LerwickWeatherScraper

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "message": LerwickWeatherScraper.get_todays_temperature()
    }