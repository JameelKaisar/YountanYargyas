# Generated by Django 3.1 on 2021-11-05 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211105_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentcontent',
            old_name='content_date',
            new_name='content_time',
        ),
    ]
