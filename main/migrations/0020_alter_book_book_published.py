# Generated by Django 3.2.7 on 2021-09-18 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_book_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 18, 15, 48, 35, 251858), verbose_name='When was this book published?'),
        ),
    ]
