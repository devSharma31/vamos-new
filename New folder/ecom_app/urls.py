from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="Home"),
    path("bag/", views.bag, name="Bag"),
    path("product/", views.productView, name="Products"),
    path("trending/", views.trending, name="Trending"),
    path("whishlist/", views.whishlist, name="Whishlist"),
    path("checkout/", views.checkout, name="Checkout"),

]
