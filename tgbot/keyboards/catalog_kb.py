from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sub_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Каталог', callback_data="catalog"),
        InlineKeyboardButton(text='Корзина', callback_data="cart"),
        InlineKeyboardButton(text='FAQ', callback_data="info_faq")
    ]
])
notsub_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='ПОДПИСАТЬСЯ', url='https://t.me/slavquestest'),
        InlineKeyboardButton(text='НАЧАТЬ РАБОТУ', callback_data="subchanneldone")
    ]
])
# channel_URL = InlineKeyboardButton(text='ПОДПИСАТЬСЯ', url='https://t.me/slavquestest')
# sub_channel_done = InlineKeyboardButton(text='ПОДПИСАН', callback_data="sub_channel_done")
