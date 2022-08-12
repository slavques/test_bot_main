from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_faq_callback = CallbackData("set", "faq_id")


def faq_kb(all_faq):
    faq_kb = InlineKeyboardMarkup(row_width=1)
    for faq in all_faq:
        btn = InlineKeyboardButton(text=faq.question, callback_data=menu_faq_callback.new(faq_id=faq.id))
        faq_kb.insert(btn)
    return faq_kb
