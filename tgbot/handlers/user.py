from aiogram import Bot, Dispatcher
from aiogram.types import Message

from bot import check_sub_channel
from tgbot.config import load_config
from tgbot.keyboards import markups

config = load_config(".env")
CHANNEL_ID = '@slavquestest'
NOTSUB_MESSAGE = 'Для доступа к функционалу, подпишитесь на канал.'
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
bot['config'] = config


async def user_status(message: Message):
    if message.chat.type == 'private':
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Привет!", reply_markup=markups.profileKeyboard)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_status, commands=["start"])
