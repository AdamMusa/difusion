# Generated by Django 2.2.1 on 2019-08-07 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projet', '0007_auto_20190807_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_complet', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=14)),
                ('repertoire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projet.Repertoire')),
            ],
        ),
    ]
