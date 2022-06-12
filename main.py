import requests
import datetime
from utils.const import CODE_TO_EMOJI
from utils.utils import round_number, timestamp_to_date


# Функция делает запрос на сторонний API openweather в зависимости от
# выбранного города, возвращает запрошенный город в формате JSON На входе
# принимает нужный город и токен для openweather
def request_weather(city: str, openweather_token: str):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_token}&units=metric '
        )
        return r.json()

    except Exception as ex:
        return ex


# Внутри себя вызывает функцию, которая делает запрос на API, получает JSON и
# преобразует его в нужный формат Возвращает обработанные данные(типа указаны
# в коде) На входе принимает нужный город и токен для openweather
def get_weather(city: str, openweather_token: str) -> (
        str, int, int, int, float, datetime, datetime, str, float):
    try:
        weather_data = request_weather(city, openweather_token)

        city = city
        current_weather = round_number(weather_data['main']['temp'])
        temp_max = round_number(weather_data['main']['temp_max'])
        temp_min = round_number(weather_data['main']['temp_min'])
        wind_speed = weather_data['wind']['speed']
        sunrise_time = timestamp_to_date(
            int(weather_data['sys']['sunrise']))
        sunset_time = timestamp_to_date(int(weather_data['sys']['sunset']))
        humidity = weather_data['main']['humidity']
        initial_weather_description = weather_data['weather'][0]['main']

        if initial_weather_description in CODE_TO_EMOJI:
            weather_description = CODE_TO_EMOJI[initial_weather_description]
        else:
            weather_description = 'Погодные условия мне не совсем ясны, лучше'\
                                  'посмотри сам \U00002639 '

    except Exception as ex:
        return ex

    else:
        return city,\
               current_weather,\
               temp_max,\
               temp_min,\
               wind_speed,\
               sunrise_time,\
               sunset_time,\
               weather_description,\
               humidity
