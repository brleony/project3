from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from .models import Menu, Cart_item, Topping, Ordered_item, Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required(login_url='/user/login')
def menu(request):
    if request.method == 'POST':
        # Save item, choice and price.
        item = request.POST["item"]
        choice = request.POST["choice"]
        price = float(request.POST["price"])

        try:
            size = request.POST["size"]
        except KeyError:
            size = 'S'

        try:
            extra_cheese = request.POST["extra_cheese"]
        except KeyError:
            extra_cheese = None

        num_toppings = 0
        pizza_toppings = []

        # Save all toppings (up to 4).
        for i in range(0, 4):
            try:
                i_str = str(i)
                print(f"topping_select_{i_str}")
                pizza_toppings.append(int(request.POST[f"topping_select_{i_str}"]))
                num_toppings += 1
            except KeyError:
                print('no topping ' + str(i))

        # If large, get price for Large item.
        if size == 'L':
            item_large = Menu.objects.filter(item = item).filter(choice = choice).filter(size = 'L').values()
            price = item_large[0]["price"]
            print(item_large, price)

        # Add item to current user's shopping cart.
        i = Cart_item(
            item = item,
            choice = choice,
            price = price,
            size = size,
            num_toppings = num_toppings,
            user = request.user
        )
        i.save()

        # Add extra cheese.
        if extra_cheese:
            price = float(price) + 0.50
            num_toppings += 1
            # Add cheese to toppings.
            cheese = Topping.objects.get(id = 22)
            i.toppings.add(cheese)
            i.price = price
            i.num_toppings = num_toppings
            i.save()

        # Add pizza toppings.
        if pizza_toppings:
            for pizza_topping in pizza_toppings:
                topping = Topping.objects.get(id = pizza_topping)
                i.toppings.add(topping)

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

@login_required(login_url='/user/login')
def cart(request):
    context = {
        "cart_items": []
    }
    total_price = 0

    # Query database for items in current user's cart.
    cart_items = Cart_item.objects.filter(user = request.user)

    for cart_item in cart_items:
        # Add items to context.
        context["cart_items"].append(
            {"choice": cart_item.choice,
             "item": cart_item.item,
             "size": cart_item.size,
             "price": cart_item.price,
             "toppings": cart_item.toppings.all()}
        )
        # Calculate total price of items in cart.
        total_price += cart_item.price

    context["total_price"] = total_price

    return render(request, "orders/cart.html", context)

@login_required(login_url='/user/login')
def myorders(request):

    if request.method == 'POST':
        # Create new order.
        current_order = Order(user = request.user)
        current_order.save()

        # Get items in cart.
        cart_items = Cart_item.objects.filter(user = request.user)

        # Add items in cart to ordered items.
        for cart_item in cart_items:
            # Make and save item.
            ordered_item = Ordered_item.objects.create(
                    item = cart_item.item,
                    choice = cart_item.choice,
                    size = cart_item.size,
                    num_toppings = cart_item.num_toppings,
                    price = cart_item.price,
                    order = current_order
                )
            ordered_item.save()

            # Add toppings.
            toppings = cart_item.toppings.all().values()
            for topping in toppings:
                ordered_item.toppings.add(topping["id"])

        # Empty cart.
        Cart_item.objects.filter(user = request.user).delete()

    # Get all orders.
    orders = Order.objects.filter(user = request.user)

    # Add items in all orders to list.
    ordered_items = []
    for order in orders:
        ordered_items_queryset = Ordered_item.objects.filter(order = order.id)
        for ordered_item in ordered_items_queryset:
            ordered_items.append(
                {"choice": ordered_item.choice,
                 "item": ordered_item.item,
                 "size": ordered_item.size,
                 "price": ordered_item.price,
                 "num_toppings": ordered_item.num_toppings,
                 "toppings": ordered_item.toppings.all(),
                 "order": order
                }
            )

    context = {
        "ordered_items": ordered_items
    }
    return render(request, "orders/myorders.html", context)

@staff_member_required
def allorders(request):
    # Get all orders.
    orders = Order.objects.all()

    # Add items in all orders to list.
    ordered_items = []
    for order in orders:
        order_dict = model_to_dict(order)

        # Get information about user.
        user = User.objects.get(id = order.user.id)
        order_dict["user"] = {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }

        ordered_items_queryset = Ordered_item.objects.filter(order = order.id)

        for ordered_item in ordered_items_queryset:
            ordered_items.append(
                {"choice": ordered_item.choice,
                 "item": ordered_item.item,
                 "size": ordered_item.size,
                 "price": ordered_item.price,
                 "num_toppings": ordered_item.num_toppings,
                 "toppings": ordered_item.toppings.all(),
                 "order": order_dict
                }
            )

    context = {
        "ordered_items": ordered_items
    }
    return render(request, "orders/allorders.html", context)