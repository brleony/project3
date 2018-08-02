from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ObjectDoesNotExist
from .models import Menu, Cart_item, Topping

def menu(request):
    if request.method == 'POST':
        # Save submitted values.
        price = float(request.POST["price"])
        choice = request.POST["choice"]
        item = request.POST["item"]
        size = request.POST["size"]
        extra_cheese = request.POST["extra_cheese"]

        # If large, get price for Large item.
        if size == 'L':
            item_large = Menu.objects.filter(item = item).filter(choice = choice).filter(size = 'L').values()
            price = item_large[0]["price"]
            print(item_large, price)

        # If extra cheese.
        if extra_cheese:
            # Add 0.50 to price.
            price = price + 0.50
            # Add cheese to toppings.
            cheese = Topping.objects.get(id = 22)
            print('yay cheese')

        # Add item to current user's shopping cart.
        i = Cart_item(item = item, choice = choice, price = price, size = size, user = request.user)
        i.save()
        i.toppings.add(cheese)
        #i.save()
        print(i)

    # Query database for menu items and toppings.
    pastas = Menu.objects.filter(item = 'PAST').values()
    subs = Menu.objects.filter(item = 'SUB').filter(size = 'S').values()
    dinner_plates = Menu.objects.filter(item = 'DIPL').filter(size = 'S').values()
    salads = Menu.objects.filter(item = 'SALA').values()
    reg_pizzas = Menu.objects.filter(item = 'REPI').filter(size = 'S').values()
    sic_pizzas = Menu.objects.filter(item = 'SIPI').filter(size = 'S').values()
    toppings = Topping.objects.filter(price = 0.00).values()

    topping_names = ",".join([t["topping"] for t in toppings])
    topping_ids = ",".join([str(t["id"]) for t in toppings])

    context = {
        "pastas": pastas,
        "subs": subs,
        "dinner_plates": dinner_plates,
        "salads": salads,
        "reg_pizzas": reg_pizzas,
        "sic_pizzas": sic_pizzas,
        "toppings": toppings,
        "topping_names": topping_names,
        "topping_ids": topping_ids
    }
    return render(request, "orders/menu.html", context)

def cart(request):
    context = {
        "cart_items": []
    }

    # Query database for items in current user's cart.
    cart_items = Cart_item.objects.filter
    for cart_item in cart_items:
        context["cart_items"].append(
            {"choice":cart_item.choice,
             "item":cart_item.item,
             "size":cart_item.size,
             "price":cart_item.price,
             "toppings": cart_item.toppings.all()}
        )

    return render(request, "orders/cart.html", context)