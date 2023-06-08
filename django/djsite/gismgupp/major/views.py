from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'},
        ]


def index(request):
    posts = building.objects.all()
    return render(request, 'major/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'major/about.html', {'menu': menu, 'title': 'О сайте'})


def show_post(request, map_id):
    posts = building.objects.get(id=map_id)
    return render(request, 'major/index.html', {'menu': menu, 'title': posts})


def contact(request):
    return render(request, 'major/about.html', {'menu': menu, 'title': 'Контакты'})
