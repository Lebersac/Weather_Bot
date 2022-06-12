from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Здесь создаем меню для бота

# ---Main menu--- #
btn_moscow = KeyboardButton('Москва')
btn_spb = KeyboardButton('Санкт-Петербург')
btn_berlin = KeyboardButton('Берлин')
btn_london = KeyboardButton('Лондон')
btn_dubai = KeyboardButton('Дубай')
btn_ny = KeyboardButton('Нью-Йорк')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_moscow,
                                                          btn_spb,
                                                          btn_berlin,
                                                          btn_london,
                                                          btn_dubai,
                                                          btn_ny)

# ---Final menu--- #
btn_thx = KeyboardButton('Спасибо!')
btn_again = KeyboardButton('Еще раз')

final_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_thx, btn_again)

again_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_again)
