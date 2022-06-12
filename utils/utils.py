import datetime


# Функция округления числен(.5 в меньшую сторону, .6 в большую)
# На входе принимает число, которое нужно округлить
def round_number(num: int):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


# Переводит таймштамп в формат Часы.Минуты.Секунды
# На входе принимает таймштамп
def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(
        timestamp).strftime("%X")


# В зависимости от времени возвращает нужное приветствие
# На входе принимает настоящий час
def get_greeting(current_hour: int):
    if current_hour >= 23 & current_hour < 5:
        return 'Доброй ночи!'

    if current_hour >= 5 & current_hour < 17:
        return 'Хорошего дня!'

    if current_hour >= 17 & current_hour < 23:
        return 'Хорошего вечера!'
