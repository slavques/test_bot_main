from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # InlineKeyboardMarkup, InlineKeyboardButton

btnProfile = KeyboardButton("Profile")
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProfile)
