import datetime

import requests

from lib.util.utilities import *


# Per condition
# For forecast API 'dt' should be between today and next 14 day in yyyy-MM-dd format (i.e. dt=2010-01-01)
class TestForecastWeather:

    def test_forecast_weather_with_data(self):
        today = datetime.date.today()
        future_date = today + datetime.timedelta(days=14)

        response = requests.get(forecast_url, headers=headers, params=forcast_params)
        if response.status_code == 200:
            try:
                json_data = response.json()
                forecast_data = json_data["forecast"]["forecastday"]
                forecastday_data = []
                for forecast_day in forecast_data:
                    forecastday_data.append(forecast_day["date"])
                for date in forecastday_data:
                    if forecast_dates == date:
                        print(f'actual result : {forecast_dates} and expected result : {date}')
                    elif future_date > today + datetime.timedelta(days=15) or future_date < today:
                        print("The future date is more than 15 days or in the past.")
                    else:
                        print("The future date is within the allowed range.")
            except KeyError:
                print("Forecast data not available or unexpected response structure")
        else:
            print("Request failed. Status code:", response.status_code)
