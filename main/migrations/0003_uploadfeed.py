# Generated by Django 3.2.7 on 2021-10-12 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_uploadaudio_uploadfile_uploadimage_uploadvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_text', models.CharField(max_length=5000)),
                ('feed_date', models.DateTimeField(auto_now_add=True)),
                ('feed_file', models.FileField(blank=True, null=True, upload_to=main.models.UploadFeed.user_directory_path)),
                ('feed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Feed',
            },
        ),
    ]
