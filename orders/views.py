from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu

def menu(request):

    pastas = Menu.objects.filter(item = 'PAST').values()
    subs = Menu.objects.filter(item = 'SUB').filter(size = 'S').values()
    dinner_plates = Menu.objects.filter(item = 'DIPL').filter(size = 'S').values()
    salads = Menu.objects.filter(item = 'SALA').values()
    reg_pizzas = Menu.objects.filter(item = 'REPI').filter(size = 'S').values()
    sic_pizzas = Menu.objects.filter(item = 'SIPI').filter(size = 'S').values()

    context = {
        "pastas": pastas,
        "subs": subs,
        "dinner_plates": dinner_plates,
        "salads": salads,
        "reg_pizzas": reg_pizzas,
        "sic_pizzas": sic_pizzas,
    }
    return render(request, "orders/menu.html", context)

def cart(request):
    return render(request, "orders/cart.html")