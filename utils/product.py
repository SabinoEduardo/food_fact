# type: ignore

import asyncio
import httpx
from utils.valida import valida_product
from asgiref.sync import sync_to_async
from utils.request import get_urls_of_products
from utils.insert_product import insert_in_to_db
from utils.scraping import Date
from bs4 import BeautifulSoup
from datetime import datetime


async def _product(page, qtde_product, dict_products, nutrition_dict):
    """
        This function receive one list with one or many links of very products. Acess one link at a time e take the information about the product.

        The function call insert_in_to_db function for to save the all products in database.
        If list is empty, the function return None.
    """

    list_urls = await get_urls_of_products(page, qtde_product)

    if list_urls:
        for position, url in enumerate(list_urls):

            if position in dict_products:
                position += 1
                
            try:
                with httpx.Client() as client:
                    response = client.get(url)
                    #content_html = BeautifulSoup(response.text, 'html.parser')
                    content_html = BeautifulSoup(
                        response, features="lxml", from_encoding="utf-8"
                        )
                    
                    date = Date(url, content_html, position, dict_products, nutrition_dict)

                    await asyncio.gather(date.set_url(),
                        date.config_name(), date.get_code(), 
                        date.get_barcode(), date.get_quantity(), 
                        date.get_ingredients(), date.get_labels(),
                        date.get_brands(), date.get_categories(),
                        date.get_packaging(), date.get_processed_foods(), 
                        date.get_manufactured(), date.get_image_url(),
                        date.get_nutrition_facts() 
                        )
                    dict_products, nutrition_dict = await sync_to_async(
                        valida_product, thread_sensitive=True
                        )(dict_products, nutrition_dict)
                    
            except httpx.RequestError as exc:
                """
                    Caso aconteja um erro durante a requisição da página web, será passado uma mensagem de erro no arquivo log.txt
                """

                with open('arquivo_de_log\log.txt', 'a', encoding='utf-8') as f:
                    f.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                    f.write(
                        f"\nOcorreu um erro no arquivo {__file__} ao tentar acessar a {exc.request.url!r}\nEste produto foi encontrado na página {page}"
                        )
                    f.write(
                        f"\nA página {exc.request.url!r} demorou para responder. Verifica se a página esta funcionando."
                        )
                    f.write("\n")
                    f.write("\n")
                return 

    if len(dict_products) < qtde_product:
        # Essa condição compara o tamanho do dicionário com a quantidade de produtos requisitados.
        page += 1
        qtde_product = qtde_product - len(dict_products)
        await _product(page, qtde_product, dict_products, nutrition_dict)

    else:
        # Se a tamanho do dicionário é igual a quantidade de produtos requisitado, a função insert_into_db # é chamada.
        await sync_to_async(insert_in_to_db, thread_sensitive=True)(dict_products, nutrition_dict)
        return dict_products, nutrition_dict


if __name__ == '__main__':
    a = datetime.now()
    dict_products = dict()
    nutrition_dict = dict()
    
    products, nutrients = asyncio.run(_product(4, 1, dict_products, nutrition_dict))
    if products:
        for id_product, product in products.items():
            print(f'Produto {int(id_product) + 1}')
            for key, value in product.items():
                print(f'{key}: {value}')
            print("Nutrientes:")
            for key_nutri, value_nutri in nutrients[id_product].items():
                print(f'    {key_nutri}: {value_nutri}')
            print()
    else:
        print(products)
    print(datetime.now()-a)
        