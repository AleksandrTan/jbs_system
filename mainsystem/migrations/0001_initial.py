# Generated by Django 3.2.2 on 2021-05-27 08:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('target_link', models.CharField(blank=True, default='', max_length=500)),
                ('file_mailing', models.FileField(upload_to='files_mailing', validators=[django.core.validators.FileExtensionValidator(['docx', 'doc', 'rtf', 'txt', 'pdf'])])),
                ('all_links', models.SmallIntegerField(default=0)),
                ('send_links', models.SmallIntegerField(default=0)),
                ('fail_links', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
