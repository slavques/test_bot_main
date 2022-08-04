from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.handlers.user import CHANNEL_ID, NOTSUB_MESSAGE
from tgbot.keyboards.catalog_kb import sub_menu, notsub_menu
from tgbot.misc.check_sub import check_sub_channel


async def menu_catalog(message: Message):
    if await check_sub_channel(await message.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await message.answer(text="Меню", reply_markup=sub_menu)
    else:
        await message.bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=notsub_menu)


def menu_main(dp: Dispatcher):
    dp.register_message_handler(menu_catalog, commands=["menu"])
