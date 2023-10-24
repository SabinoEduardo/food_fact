# type: ignore

import asyncio
import httpx
from valida import valida_product
from asgiref.sync import sync_to_async
from request import get_urls_of_products
from scraping import Date
from bs4 import BeautifulSoup
from datetime import datetime


async def _product(page, qtde_product): 
    # return: a dictionary with 100 product

    dict_products = dict()

    list_urls = await get_urls_of_products(page, qtde_product)

    if list_urls:
        for position, url in enumerate(list_urls):
            try:
                with httpx.Client() as client:
                    response = client.get(url)
                    content_html = BeautifulSoup(response.text, 'html.parser')
                    
                    date = Date(url, content_html, position, dict_products)

                    await asyncio.gather(date.set_url(),
                        date.get_code(), date.get_barcode(), 
                        date.get_quantity(), date.get_brands(), 
                        date.config_name(), date.get_categories(),
                        date.get_packaging(), date.get_image_url()
                        )
                    
                    #print(dict_products)
                    dict_products = await sync_to_async(
                        valida_product, thread_sensitive=True
                        )(dict_products)
                    #print()
                    #print(dict_products)

            except httpx.RequestError as exc:
                with open('log.txt', 'a') as f:
                    f.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                    f.write(
                        f"\nOcorreu um erro no arquivo {__file__} ao tentar acessar a {exc.request.url!r}"
                        )
                    f.write(
                        f"\nA página {exc.request.url!r} demorou para responder. Verifica se a página esta funcionando."
                        )
                    f.write("\n")
                    f.write("\n")
                return
                
        if len(dict_products) < 100:
            page += 1
            qtde_product = 100 - len(dict_products)
            await _product(page, qtde_product)

    return dict_products


if __name__ == '__main__':
    a = datetime.now()
    products = asyncio.run(_product(1, 2))
    if products:
        print(products)
        for id_product, product in products.items():
            print(f'Produto {int(id_product) + 1}')
            for key, value in product.items():
                print(f'{key}: {value}')
            print()
    else:
        print(products)
    print(datetime.now()-a)
        
