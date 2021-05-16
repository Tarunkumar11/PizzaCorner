from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, Http404,JsonResponse
from django.utils.translation import templatize
from django.views.generic import ListView,View
from .models import Product,Bestdeal,CustomerOrder
from django.core import serializers
import json
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView

def HomeView(request):
    return render(request,'pizza/home.html')


class Menushow(ListView):
    model = Product
    template_name  = "pizza/menu.html"
    
    def get_context_data(self, **kwargs):
        context = super(Menushow,self).get_context_data(**kwargs)
        context['bestdeal'] = Bestdeal.objects.all()
        return context


from rest_framework import authentication, permissions
from rest_framework import serializers, status


class BestdealSerializer(ModelSerializer):
    class Meta:
        model = Bestdeal
        fields = '__all__'

class BestdealView(APIView):
    serializer_class = BestdealSerializer
    queryset = Bestdeal.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        Songs = Bestdeal.objects.all()
        serializer = BestdealSerializer(Songs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 





