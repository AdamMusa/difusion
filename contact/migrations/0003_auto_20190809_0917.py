# Generated by Django 2.2.1 on 2019-08-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190808_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='nom_complet',
            field=models.CharField(max_length=100),
        ),
    ]
