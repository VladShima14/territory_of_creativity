# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativity_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativity',
            name='main_photo',
            field=models.ImageField(upload_to='', verbose_name='Основное фото'),
        ),
    ]
