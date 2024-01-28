from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about),
    path('mods/', mods),
    path('skins/', skins),
    path('resourcepacks/', resourcepacks),
]

