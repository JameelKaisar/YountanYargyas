# Generated by Django 3.2.7 on 2021-09-16 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_description', models.TextField()),
                ('book_published', models.DateTimeField(default=datetime.datetime(2021, 9, 16, 20, 50, 49, 565616), verbose_name='When was this book published?')),
            ],
        ),
    ]