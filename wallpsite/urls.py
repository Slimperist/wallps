from django.contrib import admin
from django.urls import include, path
# from wallpapers.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wallpapers.urls')),
    ]
