import requests

from lib.util.utilities import *


class TestCityWeather:

    def test_search_city_weather(self):
        response = requests.get(search_url, headers=headers, params=params)
        if response.status_code == 200:
            json_data = response.json()
            for item in json_data:
                city_name = item['name']
                expected_city_name = city_name.lower()
                actual_city_name = current_location.lower()
                if actual_city_name == expected_city_name:
                    print(f"actual result : {current_location} and expected result : {expected_city_name} are same")
                else:
                    print(f"actual result : {current_location} and expected result : {expected_city_name} are not same")
        else:
            print("Your Url didn't fetch any data", response.status_code)
