# Generated by Django 2.1.1 on 2018-09-16 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CinemaCore', '0010_auto_20180916_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='some_boolean',
        ),
    ]
