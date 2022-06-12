import datetime
from aiogram import Bot, types, dispatcher
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from utils.config import bot_token, openweather_token
from main import get_weather
from utils.utils import timestamp_to_date, get_greeting
import markup as nav

# Создаем инстанс бота
bot = Bot(bot_token)

# Создаем инстанс диспатчера
dp = Dispatcher(bot)


# Обрабатываем команды /start и /help
@dp.message_handler(commands=['start', 'help'])
# На указанные выше команды здоровается с пользователем и отображает меню бота
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Привет!\nВыбери название города из списка или напиши своё и я пришлю '
        'тебе погоду!',
        reply_markup=nav.main_menu
    )


# Обрабатываем сообщение 'Спасибо!'
@dp.message_handler(lambda message: message.text and 'Спасибо!' in message.text)
# Отвечаем на указанную выше команду и отображаем еще одно меню
async def send_goodbye(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Не за что!',
        reply_markup=nav.again_menu
    )


# Обрабатываем сообщение 'Еще раз'
@dp.message_handler(lambda message: message.text and 'Еще раз' in message.text)
# Отвечаем на указанную выше команду и отображаем главное меню(запускаем бота
# с начала)
async def send_again(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Надо снова выбрать город',
        reply_markup=nav.main_menu
    )


# Обрабатываем все остальные сообщения, включая города
# Если выбранный пользователем город есть в базе openweather, отправляем погоду
# для этого города, если нет, то сообщаем юзеру об этом
@dp.message_handler()
async def send_weather(message: types.Message):
    try:
        city,\
            current_weather,\
            temp_max,\
            temp_min,\
            wind_speed,\
            sunrise_time,\
            sunset_time,\
            weather_description,\
            humidity = get_weather(
                message.text, openweather_token)

        await bot.send_message(message.from_user.id,
                               f"<b>{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</b>\n"
                               f"Погода: {city}\n"
                               f"Температура: {current_weather}C°"
                               f"\n{weather_description}\n "
                               f"Влажность: {humidity}%\n"
                               f"Ветер: {wind_speed} м/с\n"
                               f"Восход солнца: {sunrise_time}\n"
                               f"Закат солнца: {sunset_time}\n"
                               f"<b>{get_greeting(datetime.datetime.now().hour)}</b>",
                               reply_markup=nav.final_menu,
                               parse_mode="HTML"
                               )

    except Exception as ex:
        await message.reply('Я не знаю такого города')


if __name__ == '__main__':
    executor.start_polling(dp)
