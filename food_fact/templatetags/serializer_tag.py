from django import template
import json

register = template.Library()

@register.simple_tag
def json_dumps(data):
    dict_product = dict()
    lista_products = list()
    for value in data:
        dict_product['code'] = int(value.code)
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