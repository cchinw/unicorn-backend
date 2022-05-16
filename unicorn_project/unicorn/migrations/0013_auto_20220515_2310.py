# Generated by Django 3.2 on 2022-05-15 23:10

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicorn', '0012_auto_20220514_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='unicornuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='unicornuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
