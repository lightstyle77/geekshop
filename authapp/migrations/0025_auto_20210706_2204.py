# Generated by Django 3.2.4 on 2021-07-06 17:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0024_auto_20180110_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 17, 4, 8, 767741, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
