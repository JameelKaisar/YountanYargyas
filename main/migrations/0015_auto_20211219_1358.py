# Generated by Django 3.1 on 2021-12-19 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20211219_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsection',
            old_name='section_video',
            new_name='section_file',
        ),
        migrations.RenameField(
            model_name='studentsection',
            old_name='section_video_base',
            new_name='section_file_base',
        ),
    ]