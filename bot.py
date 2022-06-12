import requests
import datetime
from aiogram import Bot, types, dispatcher
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from utils.config import bot_token, openweather_token
from main import get_weather
from utils.utils import timestamp_to_date, get_greeting
import markup as nav

bot = Bot(bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=[ 'start', 'help' ])
async def start_command( message: types.Message ):
    await bot.send_message(
        message.from_user.id,
        'Привет!\nВыбери название города из списка или напиши своё и я пришлю тебе погоду!',
        reply_markup=nav.main_menu
    )


@dp.message_handler(lambda message: message.text and 'Спасибо!' in message.text)
async def send_goodbye( message: types.Message ):
    await bot.send_message(
        message.from_user.id,
        'Не за что!',
        reply_markup=nav.again_menu
    )


@dp.message_handler(lambda message: message.text and 'Еще раз' in message.text)
async def send_again( message: types.Message ):
    await bot.send_message(
        message.from_user.id,
        'Надо снова выбрать город',
        reply_markup=nav.main_menu
    )


@dp.message_handler()
async def send_weather( message: types.Message ):
    try:
        city, current_weather, temp_max, temp_min, wind_speed, sunrise_time, sunset_time, weather_description, humidity = get_weather(
            message.text, openweather_token)

        await bot.send_message(message.from_user.id,
                               f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                               f"Погода: {city}\nТемпература: {current_weather}C°\n{weather_description}\n"
                               f"Влажность: {humidity}%\nВетер: {wind_speed} м/с\n"
                               f"Восход солнца: {sunrise_time}\nЗакат солнца: {sunset_time}\n"
                               f"***{get_greeting(datetime.datetime.now().hour)}***",
                               reply_markup=nav.final_menu
                               )

    except Exception as ex:
        print(ex)
        await message.reply('Я не знаю такого города')


if __name__ == '__main__':
    executor.start_polling(dp)
