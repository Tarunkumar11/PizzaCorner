from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, Http404,JsonResponse
from django.utils.translation import templatize
from django.views.generic import ListView,View
from .models import Product,Bestdeal
from django.core import serializers

def HomeView(request):
    return render(request,'pizza/home.html')


class Menushow(ListView):
    model = Product
    template_name  = "pizza/menu.html"

    def get_context_data(self, **kwargs):
        context = super(Menushow,self).get_context_data(**kwargs)
        context['bestdeal'] = Bestdeal.objects.all()
        return context

class BestdealView(View):
    models = Bestdeal

    def get_context_data(self, **kwargs):
        context = super(Menushow,self).get_context_data(**kwargs)
        context['bestdeal'] = Bestdeal.objects.all()
        return context


    def get(self,request):
        if request.is_ajax():
            mydeals = serializers.serialize('json',Bestdeal.objects.all())
            print("fsd",mydeals)
            result   = {'mybestdeals':mydeals}
            return JsonResponse(result,status = 200)
            #return HttpResponse(mydeals)
        return render(request, "pizza/menu.html")






