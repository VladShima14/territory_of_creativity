from django.utils import timezone
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=250, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey('Category', related_name='subcategory', verbose_name='Категория')
    name = models.CharField(max_length=100, unique=True, verbose_name='Название подкатегории')
    slug = models.SlugField(max_length=250, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Creativity(models.Model):
    subcategory = models.ForeignKey('SubCategory', related_name='creativity', verbose_name='Подкатегория')
    name = models.CharField(max_length=250, unique=True, verbose_name='Название творчества')
    main_photo = models.ImageField(upload_to='media/images/creativity/', verbose_name='Основное фото')
    text = models.TextField(verbose_name='Описание')
    create = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Творчество'
        verbose_name_plural = 'Творчество'


class Album(models.Model):
    creativity = models.ForeignKey('Creativity', related_name='album', verbose_name='Творчество')
    name = models.CharField(max_length=100, verbose_name='Название альбома')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Photo(models.Model):
    album = models.ForeignKey('Album', related_name='photo', verbose_name='Альбом')
    name = models.CharField(max_length=100, verbose_name='Название фото')
    image = models.ImageField(upload_to='media/images/album/', verbose_name='Фото')

    def __str__(self):
        return self.name
