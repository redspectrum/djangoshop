from django.contrib import admin
from pizzashop.models import PizzaShop, Pizza, Client
# Register your models here.

admin.site.register(PizzaShop)
admin.site.register(Pizza)
admin.site.register(Client)