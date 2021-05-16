from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.utils.translation import ugettext_lazy as _
from account.models import User

size = [
    ('Small',_('Small')),
    ('Medium',_('Medium')),
    ('Large',_('Large')),
    ('Half',_('Half')),
    ('Full',_('Large')),
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

product_categery = [
    ('Pizza',_('Pizza')),
    ('Sides',_('Sides')),
    ('Drinks',_('Drinks')),

]

class ProductSize(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return "Categary of Product is {0}".format(self.name)


class Categary(models.Model):
    name = models.CharField(max_length=128,choices=product_categery)
    def __str__(self) -> str:
        return "Categary of Product is {0}".format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=50,blank=False)
    categary = models.ForeignKey(Categary,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/product', default='static/images/bg_1.png')
    short_description   = models.CharField(max_length=200,blank=True)
    description = models.CharField(max_length=128)
    size = models.ForeignKey(ProductSize,on_delete=models.CASCADE,default=1)
    price = models.IntegerField(verbose_name="Price", blank=False)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_by_id(id):
        product = Product.objects.get(id)
        return product
    
    # @staticmethod
    # def get_veg_pizza():
    #     return Product.objects.filter(veg=True).all()
    
    # def get_by_size(size):
    #     return Pizza_type.objects.filter(size=size).all()

# class Pasta(models.Model):
#     name = models.CharField(max_length=64)
#     description = models.TextField(default="", blank=True)
#     volume = models.CharField(choices=Pasta_size,max_length=10)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
    
#     def __str__(self):
#         return self.name

# class Salad(models.Model):
# 	name = models.CharField(max_length=64)
# 	description = models.TextField(default="", blank=True)
# 	price = models.DecimalField(max_digits=6, decimal_places=2)
	
# 	def __str__(self):
# 		return f"{self.name} - {self.price} U$"

# class Drinks(models.Model):
#     name = models.CharField(max_length=64)
#     description = models.TextField(default="", blank=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     volume = models.DecimalField(max_digits=6, decimal_places=2)
	
#     def __str__(self):
#         return f"{self.name} - {self.price} U$"



product_status = [
    ('incart',_('incart')),
    ('placed',_('placed')),
    ('ontheway',_('ontheway')),
    ('delevered',_('delevered')),
]

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,max_length=32,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,blank=False)
    status = models.CharField(choices=product_status,max_length=20)
    
    def __str__(self):
        return "Username {0} and Product {1}".format(self.user.name,self.user.name)


class Bestdeal(models.Model):
    name = models.CharField(verbose_name= "Deal Offer",max_length=100)
    image = models.ImageField(upload_to='static/images/bestdeals', default='static/images/bg_1.png')
    items = models.ManyToManyField(Product)
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(verbose_name="Price")
    
    def __str__(self):
        return self.name

