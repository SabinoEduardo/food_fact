# type: ignore

import httpx
import asyncio
from datetime import datetime
from bs4 import BeautifulSoup


async def get_urls_of_products(page, qtde_product):

    list_links_product = list()
    url = 'https://world.openfoodfacts.org/'
    try:
        with httpx.Client() as client:
            response = client.get(url+str(page)).text
            content_html = BeautifulSoup(response, "html.parser")

            for product in content_html.select('ul.products'):
                for p in product.select('a'):
                    if 'href' in p.attrs:
                        list_links_product.append(url + str(p.attrs['href']))
        return list_links_product[:qtde_product]
        
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


if __name__ == '__main__':
    a = datetime.now()
    lista_url = asyncio.run(get_urls_of_products(2, 2))

    if lista_url:
        for i, p in enumerate(lista_url):
            print(i, p)
    else:
        print(lista_url)
    print(datetime.now() - a)