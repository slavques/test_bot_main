from typing import List

from django_project.usersmanage.models import Item, User
from asgiref.sync import sync_to_async


@sync_to_async
def select_user(user_id: int):
    user = User.objects.filter(user_id=user_id).first()
    return user


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        User(user_id=int(user_id), name=full_name, username=username).save()
    except Exception:
        return select_user()


@sync_to_async
def select_all_users():
    users = User.objects.all()
    return users


@sync_to_async()
def dolbaeb(user_id):
    user = User.objects.get(id=user_id)
    referral = user.referral


@sync_to_async
def count_users():
    return User.objects.all().count()


@sync_to_async
def add_item(**kwargs):
    newitem = Item(**kwargs).save()
    return newitem


@sync_to_async
def get_categories() -> List[Item]:
    return Item.objects.distinct("category_name").all()


@sync_to_async
def get_subcategories(category_code=None) -> List[Item]:
    return Item.objects.distinct("subcategory_name").filter(category_code=category_code).all()


@sync_to_async
def count_items(category_code, subcategory_code=None) -> int:
    conditions = dict(category_code=category_code)
    if subcategory_code:
        conditions.update(subcategory_code=subcategory_code)

    return Item.objects.filter(**conditions).count()


@sync_to_async
def get_item(item_id) -> Item:
    return Item.objects.filter(id=int(item_id)).count()
