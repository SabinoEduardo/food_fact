# type: ignore

import asyncio
from datetime import datetime
from utils.product import _product

"""
    File main of program. This file call the _product function
"""

async def main(page, qtde_product):
    dict_products = dict()
    nutrition_dict = dict()
    await (_product(page, qtde_product, dict_products, nutrition_dict)) 
    return

if __name__ == '__main__':
    a = datetime.now()
    asyncio.run(main(1, 100))
    print(datetime.now()-a)
