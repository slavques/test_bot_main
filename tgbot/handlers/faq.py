from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from tgbot.keyboards.faq_kb import faq_kb, menu_faq_callback
from tgbot.utils.db_api.db_commands import get_all_faq, get_answer_id


async def show_faq(call: CallbackQuery):
    all_faq = await get_all_faq()
    await call.message.edit_text("Выберите вопросы", reply_markup=faq_kb(all_faq))


async def show_answer(call: CallbackQuery, callback_data: dict):
    faq_id = callback_data.get('faq_id')
    faq = await get_answer_id(faq_id)
    await call.message.edit_text(f"{faq.answer}")


def faq(dp: Dispatcher):
    dp.register_callback_query_handler(show_faq, text="info_faq")
    dp.register_callback_query_handler(show_answer, menu_faq_callback.filter())
