# Generated by Django 3.2.7 on 2021-09-19 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210919_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 17, 52, 42, 769787), verbose_name='When was this book published?'),
        ),
    ]