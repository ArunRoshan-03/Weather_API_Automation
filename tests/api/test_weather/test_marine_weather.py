import requests

from lib.util.constants import *
from lib.util.utilities import headers


class TestMarineWeather:

    def test_marine_weather_with_date(self):
        params = {
            "key": "949aae2f0369405593254608232206",
            "q": current_location,
            "dt": marine_dates
        }

        response = requests.get(marine_url, headers=headers, params=params)
        if response.status_code == 200:
            print(response.content)
        else:
            print("Request failed. Status code:", response.status_code)
