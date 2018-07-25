from django.core.exceptions import ValidationError
from django.db import models

class Toppings(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - {self.topping}"


class Pizza(models.Model):
    sicilian = models.BooleanField("Is it a Sicilian pizza?")
    num_toppings = models.IntegerField("Number of toppings")
    toppings = models.ManyToManyField(Toppings, blank=True, on_delete=models.CASCADE)
    large = models.BooleanField("Is it a large pizza?")

    def clean(self):
        if 0 <= self.num_toppings <= 5:
            raise ValidationError("Number of toppings must be between 0 and 5.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - Pizza with {self.num_toppings} toppings: {self.topping}. Large: {self.large}. Sicilian: {self.sicilian}."


class Subs(models.Model):
    name = models.CharField("What is on the sub?", max_length=64)
    large = models.BooleanField("Is it a large sub?")
    extra_cheese = models.BooleanField("Is extra cheese added?")

    def __str__(self):
        return f"{self.id} - {self.name} sub. Large: {self.large}. Extra cheese: {self.extra_cheese}."


class Pasta(models.Model):
    name = models.CharField("Mozzarella, meatballs or chicken?", max_length=64)

    def __str__(self):
        return f"{self.id} - Baked ziti with {self.name}"


class Salad(models.Model):
    name = models.CharField("Type of salad?", max_length=64)

    def __str__(self):
        return f"{self.id} - {self.name} salad"


class Dinner_Platter(models.Model):
    name = models.CharField("Type of salad?", max_length=64)
    large = models.BooleanField("Is it a large dinner platter?")

    def __str__(self):
        return f"{self.id} - {self.name} dinner platter. Large: {self.large}."