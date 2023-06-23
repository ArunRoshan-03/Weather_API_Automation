import requests

from lib.util.utilities import *


class TestMarineWeather:

    def test_marine_weather_with_date(self):
        response = requests.get(marine_url, headers=headers, params=marine_params)
        if response.status_code == 200:
            print(response.content)
        else:
            print("Request failed. Status code:", response.status_code)
