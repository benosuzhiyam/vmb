# Generated by Django 3.0.13 on 2023-11-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0024_auto_20231102_1021'),
    ]

    operations = [
       migrations.AddField(
            model_name='matrimonyprofile',
            name='father_phone',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Father Phone number'),
        ),
    ]
