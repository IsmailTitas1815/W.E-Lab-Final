# Generated by Django 3.1.4 on 2021-04-06 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210406_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='tittle',
            new_name='title',
        ),
    ]
