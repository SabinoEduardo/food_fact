from django import template
import json

register = template.Library()

@register.simple_tag
def json_products(data):
    dict_product = dict()
    lista_products = list()

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
    json_products = json.dumps(lista_products, indent=4, ensure_ascii=False)
    return json_products

@register.simple_tag
def json_one_product(data):
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
    json_products = json.dumps(lista_products, indent=4, ensure_ascii=False)
    return json_products

