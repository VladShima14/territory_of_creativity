from django.contrib import admin
from .models import Category, SubCategory, Creativity, Album, Photo
# Register your models here.


class CreativityInLine(admin.TabularInline):
    model = Creativity


class PhotoInLine(admin.TabularInline):
    model = Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    search_fields = ['name']

    inlines = [CreativityInLine]


@admin.register(Creativity)
class CreativityAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'price']
    search_fields = ['name', 'price']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    inlines = [PhotoInLine]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
