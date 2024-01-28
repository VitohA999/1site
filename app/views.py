from django.shortcuts import render
from app.models import *

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mods(request):
    return render(request, 'mods.html')

def resourcepacks(request):
    resourcepacks = Resourcepacks.objects.all()
    return render(request, 'resourcepacks.html', {'resourcepacks': resourcepacks})

def skins(request):
    return render(request, 'skins.html')