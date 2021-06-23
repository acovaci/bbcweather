import requests
from bs4 import BeautifulSoup

from temperature_logger import TemperatureLogger



class BBCWeatherScraper:
    def __init__(self, location_id: int):
        self._url = f"https://www.bbc.co.uk/weather/{location_id}"
        self._logger = TemperatureLogger("lerwick-temperature", location_id)
    

    def log_current_temperature(self):
        temperature = self.get_todays_temperature()
        self._logger.log_temperature(temperature)


    def get_todays_temperature(self) -> int:
        return BBCWeatherScraper._extract_todays_temperature_from_weather_page_soup(self._get_weather_page_soup())
    

    def _get_weather_page(self) -> requests.models.Response:
        weather_page = requests.get(self._url)
        return weather_page


    def _get_weather_page_soup(self) -> BeautifulSoup:
        weather_page = self._get_weather_page()
        weather_soup = BBCWeatherScraper._extract_soup_from_page(weather_page)
        return weather_soup


    @staticmethod
    def _extract_soup_from_page(page: requests.models.Response) -> BeautifulSoup:
            return BeautifulSoup(page.content, 'html.parser')


    @staticmethod
    def _extract_todays_temperature_from_weather_page_soup(soup: BeautifulSoup) -> int:
        observations = soup.find(class_="wr-c-observations")
        todays_observation = observations.find(class_="wr-value--temperature--c")
        todays_temperature = next(todays_observation.children).string[:-1]
        return int(todays_temperature)



LerwickWeatherScraper = BBCWeatherScraper(2644605)


if __name__ == '__main__':
    print(LerwickWeatherScraper.get_todays_temperature())
    LerwickWeatherScraper.log_current_temperature()