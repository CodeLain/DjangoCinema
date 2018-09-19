# Generated by Django 2.1.1 on 2018-09-19 15:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CinemaCore', '0015_user_activation_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('expiry_date', models.DateTimeField(default=datetime.timedelta(days=7), editable=False)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='moviedb_id',
            field=models.IntegerField(db_index=True, default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]