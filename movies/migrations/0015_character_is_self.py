# Generated by Django 5.0.6 on 2024-05-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_alter_character_person_alter_crewmember_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='is_self',
            field=models.BooleanField(default=False),
        ),
    ]
