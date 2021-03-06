# Generated by Django 3.1.7 on 2022-05-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicorn', '0002_unicornuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='unicornuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='unicornuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='unicornuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='unicornuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
