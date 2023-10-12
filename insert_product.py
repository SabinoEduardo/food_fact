# type: ignore
import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice


import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':

    from food_fact.models import Product
    from scraping import Date
    status = ['Imported', 'Draft']

    list_products = []
    product = Date(1, 1)
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

    if len(list_products) > 0:
        Product.objects.bulk_create(list_products)
