# Generated by Django 3.2.2 on 2021-06-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsystem', '0011_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='password',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]