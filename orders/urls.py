from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("cart", views.cart, name="cart"),
]
