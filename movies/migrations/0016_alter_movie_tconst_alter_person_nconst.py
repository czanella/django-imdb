# Generated by Django 5.0.6 on 2024-05-14 01:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_character_is_self'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tconst',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Value must be "tt" followed by 7 digits', regex='tt\\d{7}')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='nconst',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Value must be "nm" followed by 7 digits', regex='nm\\d{7}')]),
        ),
    ]
