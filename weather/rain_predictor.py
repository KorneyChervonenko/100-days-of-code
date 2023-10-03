""" https://www.udemy.com/course/100-days-of-code/ """
from datetime import datetime as dt
import requests

UMBRELLA_WEATHER = {'Thunderstorm', 'Rain', 'Drizzle', 'Snow',}

ZhovtiVody = {'lat': 48.3368467093946, 'lon': 33.5149075387831,}
Rzeszów = {'lat': 50.052039156295365, 'lon': 21.999999999999996,}

NOW = dt.utcnow()

def get_data(coord: dict) -> dict:
    """ return weather data """
    # current_weather = 'https://api.openweathermap.org/data/2.5/weather'
    # one_call = 'https://api.openweathermap.org/data/3.0/onecall'
    one_call = 'https://api.openweathermap.org/data/2.5/onecall'
    API_KEY = '69f04e4613056b159c2761a9d9e664d2'
    request_parameters = coord | {'appid' : API_KEY} | {'units' : 'metric'} | {'exclude': 'current,minutely,daily'}
    response = requests.get(url=one_call, params=request_parameters)
    response.raise_for_status()
    data = response.json()
    return data

def get_actual_data(data):
        today_data = []
        for i, record in enumerate(data.get('hourly')):
            unix_utc_datetime = int(record['dt'])
            utc_datetime = dt.utcfromtimestamp(unix_utc_datetime)
            if utc_datetime >= NOW and utc_datetime.date() == NOW.date():
                today_data.append(record)
        return today_data    

def get_umbrella_hours(actual_data):
    umbrella_date = []
    for data in actual_data:
        atmospheric_precipitation = {item['main'] for item in data['weather']}
        if atmospheric_precipitation & UMBRELLA_WEATHER:
            umbrella_date.append(data)
    return umbrella_date

def main():
    """ main function """
    data = get_data(ZhovtiVody)
    # data = get_data(Rzeszów)
    actual_data = get_actual_data(data)
    umbrella_hours = get_umbrella_hours(actual_data)

    if len(umbrella_hours) > 0:
        print('You will need an umbrella today')
    else:
        print('You will NOT need an umbrella today')


if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()

