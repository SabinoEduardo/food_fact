# type: ignore
import os
import sys
import asyncio
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


async def insert_in_to_db(*args, **kwargs):

    list_products = list()
    status = ['Imported', 'Draft']
    products = kwargs

    from food_fact.models import Product

    for _ , value in products.items():

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
    Product.objects.bulk_create(list_products)
    return
