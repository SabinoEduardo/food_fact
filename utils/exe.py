"""for product in list_products:
    _product_exist = Product.objects.filter(code=product.code, product_name=product.product_name).exists()
    if _product_exist:
        list_products.remove(product)
        print(product)
        print()

if (len(list_products) > 0 and len(list_products) < 100) or (len(list_products) == 0):
    number_page += 1
    number_products = 100 - len(list_products)
elif len(list_products) == 100:
    Product.objects.bulk_create(list_products)
    for p in list_products:
        print(p)
        print()
    break"""


#if len(list_products) > 0:
#Product.objects.bulk_create(list_products)