# type: ignore

def get_nutrients(id):
    """
        Essa função define um dicionário com todos os nutrientes de um produto
        Nutrientes com valres "Null" são deletados do dicionário
    """
    from food_fact.models import Nutrient

    dict_nutrients = dict()
    copy_dictionario = dict()

    nutri = Nutrient.objects.get(id_product=id)
    dict_nutrients['energy'] = nutri.energy
    dict_nutrients['fat'] = nutri.fat
    dict_nutrients['saturated fat'] = nutri.saturated_fat
    dict_nutrients['carbohydrates'] = nutri.carbohydrates
    dict_nutrients['sugars'] = nutri.sugars
    dict_nutrients['lactose'] = nutri.lactose
    dict_nutrients['fiber'] = nutri.fiber
    dict_nutrients['proteins'] = nutri.proteins
    dict_nutrients['salt'] = nutri.salt
    dict_nutrients['alcohol'] = nutri.alcohol
    dict_nutrients['vitamina A'] = nutri.vitamina_a
    dict_nutrients['vitamina B'] = nutri.vitamina_b
    dict_nutrients['vitamina C'] = nutri.vitamina_c
    dict_nutrients['vitamina D'] = nutri.vitamina_d
    dict_nutrients['vitamina E'] = nutri.vitamina_e
    dict_nutrients['calcium'] = nutri.calcium

    for _key, value in dict_nutrients.items():
        if value == "Null":
            copy_dictionario[_key] = value

    for _key, value in copy_dictionario.items():
        dict_nutrients.pop(_key)
    
    return dict_nutrients


def products_iterables(data, current_page, quantity_page, search_value=None):
    """
        Essa função tranforma o objeto product em iterável.

    """
    dict_product = dict()
    lista_products = list()
    data_list = list()

    if search_value != None:
        """
            O valor de serach é enviada pela função serch da views. 
            
            - Search é o valor a ser filtrado (nome ou marca do produto)
        """
        data_list.append({'seach_value': search_value})

    if current_page is None:
        current_page = 1

    dict_info = {
        "info_page": 
            {"current_page": int(current_page),
             "quantity_page" : int(quantity_page)}
             }

    data_list.append(dict_info)
    
    for value in data:
        dict_product['code'] = value.code
        dict_product['barcode'] = value.barcode
        dict_product['status'] = value.status
        dict_product['imported_t'] = str(value.imported_t.strftime("%d/%m/%Y %H:%M:%S"))
        dict_product['url'] = value.url
        dict_product['product_name'] = value.product_name
        dict_product['quantity'] = value.quantity
        dict_product['ingredients'] = value.ingredients
        dict_product['labels'] = value.labels
        dict_product['categories'] = value.categories
        dict_product['packaging'] = value.packaging
        dict_product['brands'] = value.brands
        dict_product['processed_foods'] = value.processed_foods
        dict_product['country_or_region_of_manufacture'] = value.country_of_manufacture
        dict_product['image_url'] = value.image_url

        nutri = get_nutrients(value.id)
        dict_product['nutrients'] = nutri

        lista_products.append(dict_product.copy())

    products = {'products': lista_products}
    
    data_list.append(products)
    return data_list


def product_iterable(data):
    """
        Essa função tranforma o objeto product em iterável.
        Retorna uma lista com um dicioário
    """
    dict_product = dict()

    dict_product['code'] = data.code
    dict_product['barcode'] = data.barcode
    dict_product['status'] = data.status
    dict_product['imported_t'] = str(data.imported_t.strftime("%d/%m/%Y %H:%M:%S"))
    dict_product['url'] = data.url
    dict_product['product_name'] = data.product_name
    dict_product['quantity'] = data.quantity
    dict_product['ingredients'] = data.ingredient
    dict_product['labels'] = data.labels
    dict_product['categories'] = data.categories
    dict_product['packaging'] = data.packaging
    dict_product['brands'] = data.brands
    dict_product['processed_foods'] = data.processed_foods
    dict_product['country_of_manufacture'] = data.country_of_manufacture
    dict_product['image_url'] = data.image_url

    nutri = get_nutrients(data.id)
    dict_product['nutrients'] = nutri

    lista_products = [(dict_product.copy())]
    return lista_products

