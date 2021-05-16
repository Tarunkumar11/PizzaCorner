from django.contrib import admin
from .models import Product,Categary,ProductSize,Bestdeal


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name','price','short_description', 'description']


class CategaryAdmin(admin.ModelAdmin):
    model = Categary
    list_display = ['name']

class ProductSizeAdmin(admin.ModelAdmin):
    model = ProductSize
    list_display = ['name']


class BestdealAdmin(admin.ModelAdmin):
    model = Bestdeal
    list_display = ['name','price']





# class PastaAdmin(admin.ModelAdmin):
#     model = Pasta
#     list_display = ['name', 'volume','price']

# class DrinksAdmin(admin.ModelAdmin):
#     list_display = ['name', 'volume','price']

admin.site.register(Product,ProductAdmin)
admin.site.register(Categary,CategaryAdmin)
admin.site.register(ProductSize,ProductSizeAdmin)
admin.site.register(Bestdeal,BestdealAdmin)
