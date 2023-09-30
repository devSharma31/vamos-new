from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.



def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil(n / 4)
    
    # Group products into sets of 4 for each slide
    products_grouped = [products[i:i+4] for i in range(0, len(products), 4)]
    
    params = {'no_of_slides': nSlides, 'range': range(nSlides), 'products_grouped': products_grouped}
    return render(request, "ecom_app/index.html", params)

def bag(request):
    return HttpResponse ("THIS IS SHOPPING BAG")

def whishlist(request):
    return HttpResponse ("THIS IS Whishlist")

def productView(request):
    return HttpResponse ("THIS IS PRODUCT VIEW")

def trending(request):
    return HttpResponse ("THIS IS trending page")


def checkout(request):
    return HttpResponse ("THIS IS CHECKOUT")