# type: ignore

import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice
from django.db.models import Q

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()


def insert_in_to_db(dict_products, nutrition_dict):

    """
        This function insert in to database all objects created in scraping.py file that was falidated in valide.py file.
    
    """
    list_products = list()
    list_nutrients = list()
    status = ['Imported', 'Draft']

    from food_fact.models import Product, Nutrient

    for _ , value in dict_products.items():

        list_products.append(
            Product(
                code = value['code'],
                barcode = value['barcode'],
                status = choice(status),
                imported_t = datetime.now(),
                url = value['url'],
                product_name = value['product_name'],
                quantity = value['quantity'],
                ingredients = value['ingredient'],
                labels = value['labels'],
                categories = value['categories'],
                packaging = value['packaging'],
                brands = value['brand'],
                processed_foods = value['processed_foods'],
                country_of_manufacture = value['country_of_manufacture'],
                image_url = value['image_url'],
            )
            )
    Product.objects.bulk_create(list_products)
    # Itero sobre a lista de produtos inseridos no banco de dados
    for product in list_products:

        # Faz uma query o banco de dados buscando o produto com o nome 
        # e o código igual ao produto atual da iteração
        p = Product.objects.get(
            Q(product_name__exact=product.product_name) &
            Q(code=product.code)
            )
        
        # Itero sobre o dicionário de nutrientes
        for _, nutri in nutrition_dict.items():
            
            # Verifico se o nome do produto retornado da query no banco 
            # é igual ao nome do produto atual da iteração do dicionário de nutrientes.
            if p.product_name == nutri['product_name']:
                list_nutrients.append(
                    Nutrient(
                        id_product=p,
                        energy = nutri['energy'],
                        fat = nutri['fat'],
                        saturated_fat = nutri['saturated fat'],
                        carbohydrates = nutri['carbohydrates'],
                        sugars = nutri['sugars'],
                        lactose = nutri['lactose'],
                        fiber = nutri['fiber'],
                        proteins = nutri['proteins'],
                        salt = nutri['salt'],
                        alcohol = nutri['alcohol'],
                        vitamina_a = nutri['vitamina a'],
                        vitamina_b = nutri['vitamina b'],
                        vitamina_c = nutri['vitamina c'],
                        vitamina_d = nutri['vitamina d'],
                        vitamina_e = nutri['vitamina e'],
                        calcium = nutri['calcium'],
                        )
                    )
    Nutrient.objects.bulk_create(list_nutrients)
    return


