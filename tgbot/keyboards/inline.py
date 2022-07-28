from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from tgbot.utils.db_api.db_commands import get_categories, count_items, get_subcategories

menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id)


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()

    categories = await get_categories()
    for category in categories:
        number_of_items = await count_items(category.category_code)
        button_text = f"{category.category_name} ({number_of_items} шт)"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category.category_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
        return markup

async def subcategories_keyboard(category):
        CURRENT_LEVEL = 1
        markup = InlineKeyboardMarkup()

        subcategories = await get_subcategories(category)
        for subcategory in subcategories:
            number_of_items = await count_items(category_code=category, subcategory_code=subcategory)

            button_text = f"{subcategory.subcategory_code} ({number_of_items} шт)"
            callback_data = make_callback_data(level=CURRENT_LEVEL + 1, category=category,
                                               subcategory=subcategory.subcategory_code)

            markup.insert(
                InlineKeyboardButton(text=button_text, callback_data=callback_data)
            )

            markup.row(
                InlineKeyboardButton(
                    text="Назад",
                    callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
                )
            )
            return markup

