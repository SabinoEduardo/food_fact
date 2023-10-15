from django.shortcuts import render
from food_fact.models import Product

# Create your views here.

def show_products(request):

    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'index.html', context)
