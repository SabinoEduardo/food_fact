import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_link_products(page):
    """
    :param page: the number page of site open food.
    :return: The list with links the products or error message if the site open food is out.
    """
    list_links_product = list()
    try:
        url = 'https://world.openfoodfacts.org/'
        page_html = requests.get(url+str(page))
        content_html = BeautifulSoup(page_html.text, "html.parser")
        for product in content_html.select('ul.products'):
            for p in product.select('a'):
                if 'href' in p.attrs:
                    list_links_product.append(url + str(p.attrs['href']))
        return list_links_product
    
    except requests.exceptions.ConnectionError as error:
        with open('log.txt', 'a') as f:
            date = datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
            f.write(f'{str(date)}\n')
            f.write(f'ERROR: {str(error)}\n')
            f.write('\n')
        return list_links_product

d1 = datetime.now()
if __name__ == '__main__':
    links = get_link_products(2)
    if isinstance(links, list):
        for number, link in enumerate(links):
            print(f'Produto {number+1}: {link}')
    else:
        print(links)
print(datetime.now() - d1)