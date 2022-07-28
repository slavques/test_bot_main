from tgbot.utils.db_api.db_commands import add_item


async def add_item():
    await add_item(name="123", category_name='Еда', category_code='Eat', subcategory_name='кухня', subcategory_code='kitchen', price=100, photo='-', description='ыфвфывфыв')
