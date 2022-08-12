from django.db import models


# Create your models here.

class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class User(TimeBasedModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, default=1, verbose_name="ID Пользователя")
    name = models.CharField(max_length=100, verbose_name="Имя Пользователя")
    username = models.CharField(max_length=100, verbose_name="Username Пользователя")
    email = models.CharField(max_length=100, verbose_name="Email", null=True)

    def __str__(self):
        return f"№{self.id} ({self.user_id} - {self.name})"


class Referral(TimeBasedModel):
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"

    id = models.ForeignKey(User, verbose_name="Пользователь", unique=True, primary_key=True, on_delete=models.CASCADE,
                           related_name='referral')
    referrer_id = models.BigIntegerField()

    def __str__(self):
        return f"№{self.id} = от {self.referrer_id}"


class Item(TimeBasedModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Название Товара", max_length=50)
    photo = models.CharField(verbose_name="Фото file_id", max_length=200)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Описание", max_length=3000, null=True)

    category_code = models.CharField(verbose_name="Код категории", max_length=30)
    category_name = models.CharField(verbose_name="Название категории", max_length=30)
    subcategory_code = models.CharField(verbose_name="Код подкатегории", max_length=30)
    subcategory_name = models.CharField(verbose_name="Название подкатегории", max_length=30)

    def __str__(self):
        return f"№{self.id} - {self.name}"


class Purchase(TimeBasedModel):
    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.SET(0))
    item_id = models.ForeignKey(Item, verbose_name="Идентификатор Товара", on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name="Стоимость", decimal_places=2, max_digits=8)
    quantity = models.IntegerField(verbose_name="Количество")
    purchase_time = models.DateTimeField(verbose_name="Время Покупки", auto_now_add=True)
    shipping_address = models.JSONField(verbose_name="Адрес Доставки", null=True)
    phone_number = models.CharField(verbose_name="Номер Телефона", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=100, null=True)
    receiver = models.CharField(verbose_name="Имя Получателя", max_length=100)
    successful = models.BooleanField(verbose_name="Оплачено", default=False)

    def __str__(self):
        return f"№{self.id} = {self.item_id} ({self.quantity})"


class FAQ(models.Model):
    question = models.CharField(verbose_name="Вопрос", max_length=50)
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Частозадаваемые вопросы"
        verbose_name_plural = "Частозадаваемые вопросы"

    def __str__(self):
        return self.question[:30]


class Catalog(models.Model):
    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

