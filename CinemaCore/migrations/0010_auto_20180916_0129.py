# Generated by Django 2.1.1 on 2018-09-16 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CinemaCore', '0009_auto_20180916_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='administrator',
            new_name='some_boolean',
        ),
    ]