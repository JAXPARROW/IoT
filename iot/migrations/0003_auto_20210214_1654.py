# Generated by Django 2.2.18 on 2021-02-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0002_auto_20210213_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='device_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]