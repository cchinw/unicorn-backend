# Generated by Django 3.2 on 2022-05-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicorn', '0003_auto_20220512_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='resource_title',
            field=models.CharField(default='Grief Handling Resource', max_length=500),
        ),
    ]