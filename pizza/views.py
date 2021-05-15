from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from .models import Product

def HomeView(request):
    return render(request,'pizza/home.html')


class Menushow(ListView):
    model = Product
    template_name  = "pizza/menu.html"

    def get_context_data(self, **kwargs):
        context = super(Menushow,self).get_context_data(**kwargs)
        return context



