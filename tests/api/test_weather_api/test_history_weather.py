import requests

from lib.util.utilities import *


# Per condition
# For history API 'dt' should be on or after 1st Jan, 2010 in yyyy-MM-dd format (i.e. dt=2010-01-01)
class TestHistoryWeather:

    def test_history_weather_with_data(self):
        response = requests.get(history_url, headers=headers, params=history_params)
        if response.status_code == 200:
            try:
                json_data = response.json()
                history_data = json_data["forecast"]["forecastday"]
                history_date = []
                for history_day in history_data:
                    history_date.append(history_day["date"])
                for date in history_date:
                    if history_dates == date:
                        print(f'actual result : {history_dates} and expected result : {date}')
                    else:
                        print("both date are not matched")
            except KeyError:
                print("History data not available or unexpected response structure")
        else:
            print("Request failed. Status code:", response.status_code)
