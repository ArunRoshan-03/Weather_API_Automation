import requests

from lib.data.sport_datatype import sport_datatype
from lib.util.constants import *
from lib.util.utilities import *


class TestSport:

    def test_sports_datas_and_data_type(self):
        response = requests.get(sport_url, headers=headers, params=params)
        if response.status_code == 200:
            json_data = response.json()
            for sport_name in sports_game_name:
                current_data = json_data[sport_name]
                sport_data = current_data[1]
                print(f'\nsport game name : {sport_name}')
                print(response.content)
                for key, expected_type in sport_datatype.items():
                    value = sport_data.get(key)
                    actual_type = type(value).__name__
                    if actual_type == expected_type.__name__:
                        print(f"{key}: Data type is as expected ({actual_type})")
                    else:
                        print(f"{key}: Data type is not as expected ({actual_type})")
        else:
            print("Your Url didn't fetch any data", response.status_code)
