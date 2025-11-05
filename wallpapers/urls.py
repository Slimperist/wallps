from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('rnd/', random_wallps, name='random_wallps'),
    path('cat/<int:category_id>/', get_categories, name='cat'),
    path('wallp/<int:wallp_id>/', view_wallp, name='wallp'),
    path('tags/', tag_list, name='tag_list'),
    path('tag/<int:tag_id>/', wallpapers_by_tag, name='wallpapers_by_tag'),
    path('search/', search, name='search'),
]
