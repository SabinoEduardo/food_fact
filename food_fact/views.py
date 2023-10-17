from django.shortcuts import render, get_object_or_404
from food_fact.models import Product
from django.core.paginator import Paginator

# Create your views here.


def list_products(request):

    products = Product.objects.all()
    
    paginator = Paginator(products, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj}
    print(products)
    return render(request, 'index.html', context)

def get_product(request, id_product):
    product = get_object_or_404(Product, pk=id_product)

    return 

