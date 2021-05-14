from django.contrib import admin
from .models import Pizza_type,Pasta,Drinks


class Pizza_typeAdmin(admin.ModelAdmin):
    model = Pizza_type
    list_display = ['name', 'categery','veg', 'size', 'price']

class PastaAdmin(admin.ModelAdmin):
    model = Pasta
    list_display = ['name', 'volume','price']

class DrinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'volume','price']

admin.site.register(Pizza_type,Pizza_typeAdmin)
admin.site.register(Pasta,PastaAdmin)
admin.site.register(Drinks,DrinksAdmin)
