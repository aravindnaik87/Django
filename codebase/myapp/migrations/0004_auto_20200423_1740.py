# Generated by Django 2.2.2 on 2020-04-23 12:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_auto_20200423_1641'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addpost',
            new_name='PostData',
        ),
    ]