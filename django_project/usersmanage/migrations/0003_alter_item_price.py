# Generated by Django 4.0.6 on 2022-08-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0002_alter_referral_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена123'),
        ),
    ]
