from django.shortcuts import render
from django.http import HttpResponse, Http404


def HomeView(request):
    return HttpResponse("<h1>This is tarun saini</h1>")