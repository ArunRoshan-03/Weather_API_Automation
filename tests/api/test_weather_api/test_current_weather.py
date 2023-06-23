import requests

from lib.data.current_datatype import data_types
from lib.util.utilities import *


class TestCurrentWeather:

    def test_current_weather_data_type(self):
        response = requests.get(current_url, headers=headers, params=params)
        json_data = response.json()
        current_data = json_data["current"]

        for key, expected_type in data_types.items():
            value = current_data.get(key)
            actual_type = type(value).__name__
            if actual_type == expected_type.__name__:
                print(f"{key}: Data type is as expected ({actual_type})")
            else:
                print(f"{key}: Data type is not as expected ({actual_type})")
