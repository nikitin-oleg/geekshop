# Generated by Django 3.1.4 on 2020-12-27 16:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20201227_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 29, 16, 24, 52, 449256, tzinfo=utc)),
        ),
    ]
