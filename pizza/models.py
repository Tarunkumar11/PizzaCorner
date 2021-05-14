from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import ugettext_lazy as _


size = [
    ('Small',_('Small')),
    ('Medium',_('Medium')),
    ('Large',_('Large')),
]
Pasta_size = [
    ('Half',_('Half')),
    ('Full',_('Full')),
]

pizza_categery = [
    ('Bestsellers',_('Bestsellers')),
    ('Classic',_('Classic')),
    ('Favourite',_('Favourite')),
    ('Delight',_('Delight')),
]
class Pizza_type(models.Model):
    name = models.CharField(max_length=50,blank=False)
    veg = models.BooleanField(default=False)
    size = models.CharField(_("Size"),choices=size,max_length=10)
    categery = models.CharField(_("Categery"),choices=pizza_categery,max_length=20,default="Delight")
    price = models.IntegerField(blank=False)
    description = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_by_id(id):
        pizza = Pizza_type.objects.get(id)
        return pizza
    
    @staticmethod
    def get_veg_pizza():
        return Pizza_type.objects.filter(veg=True).all()
    
    def get_by_size(size):
        return Pizza_type.objects.filter(size=size).all()

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="", blank=True)
    volume = models.CharField(choices=Pasta_size,max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

# class Salad(models.Model):
# 	name = models.CharField(max_length=64)
# 	description = models.TextField(default="", blank=True)
# 	price = models.DecimalField(max_digits=6, decimal_places=2)
	
# 	def __str__(self):
# 		return f"{self.name} - {self.price} U$"

class Drinks(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="", blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
	
    def __str__(self):
        return f"{self.name} - {self.price} U$"

