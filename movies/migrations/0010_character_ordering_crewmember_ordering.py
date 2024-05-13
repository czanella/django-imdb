# Generated by Django 5.0.6 on 2024-05-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='ordering',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crewmember',
            name='ordering',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]