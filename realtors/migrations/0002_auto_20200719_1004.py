# Generated by Django 3.0.8 on 2020-07-19 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 19, 10, 4, 15, 221276)),
        ),
    ]
