# Generated by Django 5.2.1 on 2025-06-03 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuerySort', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lectors',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(6, message='The event lectors must be at least 6 characters long.')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1, message='The event name must be at least 1 characters long.'), django.core.validators.RegexValidator("^[A-Za-zА-Яа-яЁё0-9 _\\-'&]+$")]),
        ),
        migrations.AlterField(
            model_name='event',
            name='town',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1, message='The town name must be at least 1 characters long.'), django.core.validators.RegexValidator("^[A-Za-zА-Яа-яЁё0-9 _\\-'&]+$")]),
        ),
    ]
