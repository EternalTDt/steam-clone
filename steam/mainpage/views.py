from django.shortcuts import render, get_list_or_404
from .models import Product

def home(request):
    products = Product.objects.all().order_by('name')

    context = {
        'products': products
    }
    return render(request, 'mainpage/home.html', context)
