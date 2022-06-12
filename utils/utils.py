import datetime


def round_number( num ):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def timestamp_to_date( timestamp ):
    return datetime.datetime.fromtimestamp(
        timestamp).strftime("%X")


def get_greeting( current_hour: int ):
    if current_hour >= 23 & current_hour < 5:
        return 'Доброй ночи!'

    if current_hour >= 5 & current_hour < 17:
        return 'Хорошего дня!'

    if current_hour >= 17 & current_hour < 23:
        return 'Хорошего вечера!'
