# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название альбома')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Creativity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название творчества')),
                ('main_photo', models.ImageField(upload_to='images/creativity/', verbose_name='Основное фото')),
                ('text', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Творчество',
                'verbose_name_plural': 'Творчество',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название фото')),
                ('image', models.ImageField(upload_to='images/album/', verbose_name='Фото')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='creativity_app.Album', verbose_name='Альбом')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название подкатегории')),
                ('slug', models.SlugField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='creativity_app.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='creativity',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creativity', to='creativity_app.SubCategory', verbose_name='Подкатегория'),
        ),
        migrations.AddField(
            model_name='album',
            name='creativity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='creativity_app.Creativity', verbose_name='Творчество'),
        ),
    ]
