# Generated by Django 2.0.1 on 2018-01-05 16:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_auto_20180105_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='расположение')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='день рождения')),
            ],
        ),
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shopuser',
            name='me',
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 16, 4, 16, 908339, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
        migrations.DeleteModel(
            name='ShopUserProfile',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
