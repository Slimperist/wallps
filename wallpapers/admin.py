from django.contrib import admin
from .models import Wallpapers, Categories, Tags, Wallpapers_Tags

@admin.register(Wallpapers)
class WallpapersAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_category', 'width', 'height', 'wallp_size', 'created_up', 'path_preview', 'path_original')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'name_category_ru')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')

@admin.register(Wallpapers_Tags)
class Wallpapers_TagsAdmin(admin.ModelAdmin):
    list_display = ('wallpaper_id', 'tag_id')