import requests.models
import bs4

from src.scraper import BBCWeatherScraper

def test_can_request_weather_page():
    LondonWeatherScraper = BBCWeatherScraper(2643743)
    london_weather_page = LondonWeatherScraper._get_weather_page()
    assert isinstance(london_weather_page, requests.models.Response)


def test_can_get_weather_soup():
    CardiffWeatherScraper = BBCWeatherScraper(2653822)
    cardiff_weather_soup = CardiffWeatherScraper._get_weather_page_soup()
    assert isinstance(cardiff_weather_soup, bs4.BeautifulSoup)


def test_temperature_is_int():
    BelfastWeatherScraper = BBCWeatherScraper(2655984)
    belfast_temperature = BelfastWeatherScraper.get_todays_temperature()
    assert isinstance(belfast_temperature, int)


def test_temperature_is_feasible():
    EdinburghWeatherScraper = BBCWeatherScraper(2650225)
    edinburgh_temperature = EdinburghWeatherScraper.get_todays_temperature()
    assert edinburgh_temperature > -30 and edinburgh_temperature < 50