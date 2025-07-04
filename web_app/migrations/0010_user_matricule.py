# Generated by Django 5.2 on 2025-05-22 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_modalinfocategory_modalinfo_modalinfooption'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='matricule',
            field=models.CharField(blank=True, help_text='Matricule à 7 chiffres', max_length=7, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(7, message='Le matricule doit contenir exactement 7 chiffres'), django.core.validators.RegexValidator(message='Le matricule doit contenir uniquement des chiffres', regex='^\\d{7}$')]),
        ),
    ]
