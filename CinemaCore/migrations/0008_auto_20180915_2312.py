# Generated by Django 2.1.1 on 2018-09-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CinemaCore', '0007_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_special_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='administrator',
            field=models.BooleanField(default=False),
        ),
    ]
