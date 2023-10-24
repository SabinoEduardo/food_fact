# type: ignore

import asyncio
from datetime import datetime
from product import _product
from insert_product import insert_in_to_db

async def main(page, qtde_product):
    products = await _product(page, qtde_product)
    await insert_in_to_db(products)
    return


if __name__ == '__main__':
    a = datetime.now()
    asyncio.run(main(1, 100))
    print(datetime.now()-a)

 