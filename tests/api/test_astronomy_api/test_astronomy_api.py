import requests

from lib.data.astronomy_datatype import astro_data
from lib.util.utilities import *


class TestAstronomy:

    def test_astronomy_datas_and_data_type(self):
        response = requests.get(astronomy_url, headers=headers, params=astronomy_params)
        if response.status_code == 200:
            json_data = response.json()
            location_data = json_data["location"]["name"]
            astronomy_data = json_data['astronomy']['astro']
            expected_result = location_data.lower()
            actual_result = astronomy_location.lower()
            if actual_result == expected_result:
                print(astronomy_data)
            for key, expected_type in astro_data.items():
                value = astronomy_data.get(key)
                actual_type = type(value).__name__
                if actual_type == expected_type.__name__:
                    print(f"{key}: Data type is as expected ({actual_type})")
                else:
                    print(f"{key}: Data type is not as expected ({actual_type})")
                    break
            else:
                print(f"Location data is not matched with actual: {actual_result},expected:{expected_result}")
        else:
            print("Your Url didn't fetch any data", response.status_code)
