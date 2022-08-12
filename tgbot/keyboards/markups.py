from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # InlineKeyboardMarkup, InlineKeyboardButton

btnMenu = KeyboardButton("МЕНЮ")
menuBtn = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMenu)
