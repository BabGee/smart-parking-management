# Generated by Django 3.1.6 on 2021-02-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_zones', '0004_auto_20210211_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='plate_number',
            field=models.CharField(max_length=10),
        ),
    ]
