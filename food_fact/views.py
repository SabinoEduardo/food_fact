from django.shortcuts import render
from food_fact.models import Product
from food_fact.serializer import turn_dict
import json

# Create your views here.


def show_products(request):

    products = Product.objects.all()
    products = json.dumps(
            turn_dict(products), 
            ensure_ascii=False,
            indent=4
        )
    context = {'products': products}
    print(products)
    return render(request, 'index.html', context)
