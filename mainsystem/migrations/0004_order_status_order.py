# Generated by Django 3.2.2 on 2021-05-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsystem', '0003_order_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_order',
            field=models.CharField(default='create', max_length=500),
        ),
    ]
