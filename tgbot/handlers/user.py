from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hlink

from tgbot.keyboards import markups
from tgbot.keyboards.catalog_kb import notsub_menu
from tgbot.misc.check_sub import check_sub_channel
from tgbot.utils.db_api import db_commands as commands

CHANNEL_ID = '@slavquestest'
NOTSUB_MESSAGE = f'Для доступа к функционалу, подпишитесь на {hlink("канал", "https://t.me/slavquestest")}.'


async def check_sub(message: Message):
    if message.chat.type == 'private':
        if await check_sub_channel(await message.bot.get_chat_member(chat_id=CHANNEL_ID,
                                                                     user_id=message.from_user.id)):
            await message.bot.send_message(message.from_user.id,
                                           'Привет! Ознакомиться с функционалом можно по команде \n/menu',
                                           reply_markup=markups.profileKeyboard)
        else:
            await message.bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=notsub_menu)


async def subchanneldone(message: Message):
    await message.bot.delete_message(message.from_user.id, message.message.message_id)
    if await check_sub_channel(await message.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await message.bot.send_message(message.from_user.id,
                                       'Привет! Ознакомиться с функционалом можно по команде \n/menu',
                                       reply_markup=markups.profileKeyboard)
    else:
        await message.bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=notsub_menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(check_sub, commands=["start"])
    dp.register_callback_query_handler(subchanneldone, text='subchanneldone')
