# Generated by Django 2.2.1 on 2019-08-06 10:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projet', '0002_auto_20190806_0921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Repertoire',
            new_name='Repository',
        ),
    ]