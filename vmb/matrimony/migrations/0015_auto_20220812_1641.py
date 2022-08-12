# Generated by Django 2.2.7 on 2022-08-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0014_auto_20220811_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='languages_can_read_write',
            field=models.ManyToManyField(blank=True, related_name='readers_and_writers', to='matrimony.Language', verbose_name='Languages you can read and write'),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='languages_can_speak',
            field=models.ManyToManyField(blank=True, help_text='Languages you know', related_name='speakers', to='matrimony.Language'),
        ),
    ]
