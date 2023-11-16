# type: ignore

import os
import sys
from pathlib import Path
import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()


def valida_product(prod, nutri):
    """
        This function verify if one product exist in database or not. If exist in database the product is delete of dictionary of product.
    """

    from food_fact.models import Product

    copy_dictionario = dict()

    for key, value in prod.items():
        _product_exist = Product.objects.filter(
                product_name__exact=value['product_name']
            ).exists()
        if _product_exist:
            copy_dictionario[key] = value

    for key, value in copy_dictionario.items():
        if key in prod:
            prod.pop(key)
            nutri.pop(key)
            
    return prod, nutri
   
