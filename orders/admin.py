from django.contrib import admin
from .models import Menu, Ordered_item, Order, Topping

# Register your models here.
admin.site.register(Menu)
admin.site.register(Ordered_item)
admin.site.register(Order)
admin.site.register(Topping)