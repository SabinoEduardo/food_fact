# type: ignore
import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice


import django
from django.conf import settings

time1 = datetime.now()

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':

    from food_fact.models import Product
    from scraping import Date

    status = ['Imported', 'Draft']
    number_page = 1
    number_products = 100

list_products = []
while True:
    product = Date(number_page, number_products)
    for key, value in product.products().items():
        list_products.append(
            Product(
                code = value['code'],
                barcode = value['barcode'],
                status = choice(status),
                imported_t = datetime.now(),
                url = value['url'],
                product_name = value['product_name'],
                quantity = value['quantity'],
                categories = value['categories'],
                packaging = value['packaging'],
                brands = value['brand'],
                image_url = value['image_url'],
            )
            )
        
    for product in list_products:
        _product_exist = Product.objects.filter(code=product.code).exists()
        if _product_exist:
            list_products.remove(product)

    if (len(list_products) > 0 and len(list_products) < 100) or (len(list_products) == 0):
        number_page += 1
        number_products = 100 - len(list_products)
    elif len(list_products) == 100:
        Product.objects.bulk_create(list_products)
        break


    #if len(list_products) > 0:
    #Product.objects.bulk_create(list_products)

print(datetime.now() - time1)