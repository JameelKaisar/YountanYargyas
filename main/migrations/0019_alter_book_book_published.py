# Generated by Django 3.2.7 on 2021-09-18 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_book_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 18, 15, 15, 3, 393469), verbose_name='When was this book published?'),
        ),
    ]
