from django.core.exceptions import ValidationError
from django.db import models

class Topping(models.Model):
    topping = models.CharField(max_length = 64)
    price = models.DecimalField(
        "What does this topping cost?",
        max_digits = 4,
        decimal_places = 2,
        default = 0.00,
    )

    def __str__(self):
        return f"{self.id} - {self.topping} for ${self.price}."

class Menu(models.Model):
    SUB = 'SUB'
    PASTA = 'PAST'
    SALAD = 'SALA'
    DINNER_PLATE = 'DIPL'
    SICILIAN_PIZZA = 'SIPI'
    REGULAR_PIZZA = 'REPI'
    ITEM_CHOICES = (
        (SUB, 'Sub'),
        (PASTA, 'Pasta'),
        (SALAD, 'Salad'),
        (DINNER_PLATE, 'Dinner Plate'),
        (SICILIAN_PIZZA, 'Sicilian Pizza'),
        (REGULAR_PIZZA, 'Regular Pizza'),
    )
    item = models.CharField(
        "What kind of item is this?",
        choices = ITEM_CHOICES,
        max_length = 4,
    )
    choice = models.CharField(
        "What flavor is it?",
        max_length = 64,
        blank = True,
    )
    SMALL = 'S'
    LARGE = 'L'
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (LARGE, 'Large'),
    )
    size = models.CharField(
        "What size item is this?",
        choices = SIZE_CHOICES,
        max_length = 2,
        blank = True,
    )
    num_toppings = models.IntegerField(default = 0)
    price = models.DecimalField(
        "What does it cost?",
        max_digits = 5,
        decimal_places = 2,
    )

    def __str__(self):
        return f"{self.id} - {self.size} {self.choice} {self.item} with {self.num_toppings} toppings. Price: {self.price}."

class Ordered_item(models.Model):
    SUB = 'SUB'
    PASTA = 'PAST'
    SALAD = 'SALA'
    DINNER_PLATE = 'DIPL'
    SICILIAN_PIZZA = 'SIPI'
    REGULAR_PIZZA = 'REPI'
    ITEM_CHOICES = (
        (SUB, 'Sub'),
        (PASTA, 'Pasta'),
        (SALAD, 'Salad'),
        (DINNER_PLATE, 'Dinner Plate'),
        (SICILIAN_PIZZA, 'Sicilian Pizza'),
        (REGULAR_PIZZA, 'Regular Pizza'),
    )
    item = models.CharField(
        "What kind of item is this?",
        choices = ITEM_CHOICES,
        max_length = 4,
    )
    choice = models.CharField(
        "What flavor is it?",
        max_length = 64,
        blank = True,
    )
    SMALL = 'S'
    LARGE = 'L'
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (LARGE, 'Large'),
    )
    size = models.CharField(
        "What size item is this?",
        choices = SIZE_CHOICES,
        max_length = 2,
        blank = True,
    )
    toppings = models.ManyToManyField(Topping, blank = True)
    num_toppings = models.IntegerField(default = 0)
    price = models.DecimalField(
        "What does it cost?",
        max_digits = 5,
        decimal_places = 2,
    )
    order = models.ForeignKey(
        'Order',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return f"{self.id} - {self.size} {self.choice} {self.item} with {self.num_toppings}: {self.toppings}. Order: {self.order}. Price: {self.price}."

class Order(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    time = models.DateTimeField(
        'Timestamp',
        auto_now_add = True,
    )

    def __str__(self):
        return f"Order id: {self.id}. By {self.user} on {self.time}."

class Cart_item(models.Model):
    SUB = 'SUB'
    PASTA = 'PAST'
    SALAD = 'SALA'
    DINNER_PLATE = 'DIPL'
    SICILIAN_PIZZA = 'SIPI'
    REGULAR_PIZZA = 'REPI'
    ITEM_CHOICES = (
        (SUB, 'Sub'),
        (PASTA, 'Pasta'),
        (SALAD, 'Salad'),
        (DINNER_PLATE, 'Dinner Plate'),
        (SICILIAN_PIZZA, 'Sicilian Pizza'),
        (REGULAR_PIZZA, 'Regular Pizza'),
    )
    item = models.CharField(
        "What kind of item is this?",
        choices = ITEM_CHOICES,
        max_length = 4,
    )
    choice = models.CharField(
        "What flavor is it?",
        max_length = 64,
        blank = True,
    )
    SMALL = 'S'
    LARGE = 'L'
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (LARGE, 'Large'),
    )
    size = models.CharField(
        "What size item is this?",
        choices = SIZE_CHOICES,
        max_length = 2,
        blank = True,
    )
    toppings = models.ManyToManyField(Topping, blank = True)
    num_toppings = models.IntegerField(default = 0)
    price = models.DecimalField(
        "What does it cost?",
        max_digits = 5,
        decimal_places = 2,
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
        default = 0,
    )

    def __str__(self):
        toppings = ", ".join([t["topping"] for t in self.toppings.all().values()])
        return f"{self.id} - {self.size} {self.choice} {self.item}" \
               f" with {self.num_toppings} toppings: {toppings}." \
               f" User: {self.user}. Price: {self.price}."