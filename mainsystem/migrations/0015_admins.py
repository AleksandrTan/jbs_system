# Generated by Django 3.2.2 on 2021-08-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsystem', '0014_order_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.BooleanField(default=False)),
                ('firstname', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
