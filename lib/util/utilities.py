from lib.util.constants import *

headers = {
    "Content-Type": "application/json",
    "api_key": "949aae2f0369405593254608232206"
}

params = {
    "key": "949aae2f0369405593254608232206",
    "q": current_location
}

forcast_params = {
    "key": "949aae2f0369405593254608232206",
    "q": current_location,
    "dt": forecast_dates
}

history_params = {
    "key": "949aae2f0369405593254608232206",
    "q": current_location,
    "dt": history_dates
}

marine_params = {
    "key": "949aae2f0369405593254608232206",
    "q": current_location,
    "dt": marine_dates
}

astronomy_params = {
    "key": "949aae2f0369405593254608232206",
    "q": astronomy_location
}
