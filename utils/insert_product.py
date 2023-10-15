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
list_copia = []

#print(datetime.now())
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
        _product_exist = Product.objects.filter(product_name__exact=product.product_name).exists()
        if _product_exist:
            list_copia.append(product)

    for prod_copia in list_copia:
        if prod_copia in list_products:
            list_products.remove(prod_copia)

    if (len(list_products) > 0 and len(list_products) < 100) or (len(list_products) == 0):
        number_page += 1
        number_products = 100 - len(list_products)
        print()
        print('sabino')
        print('produtos', len(list_products))
    else:
        print('oi')
        print(len(list_products))
        print()
        Product.objects.bulk_create(list_products)
        break
        

#print(datetime.now() - time1)
