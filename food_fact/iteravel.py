# type: ignore

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
            
            - Seach é o valor a ser filtrado (nome ou marca do produto)
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
        dict_product['categories'] = value.categories
        dict_product['packaging'] = value.packaging
        dict_product['brands'] = value.brands
        dict_product['image_url'] = value.image_url

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
    dict_product['categories'] = data.categories
    dict_product['packaging'] = data.packaging
    dict_product['brands'] = data.brands
    dict_product['image_url'] = data.image_url

    lista_products = [(dict_product.copy())]
    return lista_products

