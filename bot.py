import logging
import os

import django
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config


config = load_config(".env")
storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
logger = logging.getLogger(__name__)


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        'django_project.bottest.settings'
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()


async def on_startup(dp):
    from tgbot.handlers.faq import faq
    from tgbot.filters.admin import AdminFilter
    # from tgbot.handlers.echo import register_echo
    from tgbot.handlers.menu import menu_main
    from tgbot.handlers.user import register_user
    # from tgbot.handlers.user import register_admin
    from tgbot.middlewares.db import DbMiddleware
    dp.setup_middleware(DbMiddleware())
    dp.filters_factory.bind(AdminFilter)
    menu_main(dp)
    register_user(dp)
    faq(dp)

    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")


if __name__ == '__main__':
    setup_django()
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup)
