# Generated by Django 3.2.2 on 2021-06-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsystem', '0009_auto_20210601_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxy',
            name='fail_request_proxy',
            field=models.IntegerField(default=0),
        ),
    ]
