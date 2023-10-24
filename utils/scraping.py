# type: ignore

class Date:
    """
        class with all methods assincrons to acess the data of products.
        Such method add one date in product dictionary. These date are:

            :url : str
            :Code : int
            :Barcode : str
            :quantity : str
            :name : str
            :categories : str
            :packaging : str
            :brands : str
    """

    def __init__(self, url, content_html, position, products_dict):
        self.url = url
        self.position = position
        self.products_dict = products_dict
        self.content_html = content_html
        

    async def set_url(self):
        """
            Function add the url product in dictionary product
            :return: without return
        """
        self.products_dict[self.position] = {}
        self.products_dict[self.position]['url'] = self.url
        return

    async def get_code(self):
        """
            Function to get the code value of product
            :return: without return
        """
        try:
            code = self.content_html.select_one('span#barcode')
            code = int(code.text)
            self.products_dict[self.position]['code'] = code
        except AttributeError:
            self.products_dict[self.position]['code'] = 0
        return

    async def get_barcode(self):
        """
            Function to get the barcode of product
            :return: without return
        """
        try:
            value_barcode = self.content_html.select_one('#barcode_paragraph')
            barcode = (str(value_barcode.text).replace('Barcode: ', '').strip()).replace(' ', '')
            self.products_dict[self.position]['barcode'] = barcode
        except AttributeError:
            self.products_dict[self.position]['barcode'] = "Null"
        return

    async def get_quantity(self):
        """
            Function to get the quantity of product.
            :return: without return
        """
        try:
            quantity = self.content_html.select_one('#field_quantity_value').text
            self.products_dict[self.position]['quantity'] = quantity
        except AttributeError:
            self.products_dict[self.position]['quantity'] = "Null"
        return


    async def get_brands(self):
        """
            Function to get the brand of product.
            :return: without return
        """
        try:
            brand = self.content_html.select_one('#field_brands a').text
            self.products_dict[self.position]['brand'] = brand
        except AttributeError:
            self.products_dict[self.position]['brand'] = "Null"
        return

    async def config_name(self):
        """
            Function to get the name of product.
            :return: without return
        """
        try:
            name_product = self.content_html.select_one('[itemscope] h1').text
            self.products_dict[self.position]['product_name'] = name_product
        except AttributeError:
            self.products_dict[self.position]['product_name'] = "Null"
        return

    async def get_categories(self):
        """
            Function to get the categories of product.
            :return: without return
        """
        try:
            categories = self.content_html.select_one('.field_value#field_categories_value')
            self.products_dict[self.position]['categories'] = categories.text
        except AttributeError:
            self.products_dict[self.position]['categories'] = "Null"
        return

    async def get_packaging(self):
        """
            Function to get the packaging of product.
            :return: without return
        """
        try:
            packaging = self.content_html.select_one('.field_value#field_packaging_value').text
            self.products_dict[self.position]['packaging'] = packaging
        except AttributeError:
            self.products_dict[self.position]['packaging'] = "Null"
        return

    async def get_image_url(self):
        """
            Function to get the image url of product.
            :return: without return
        """
        try:
            img_url = self.content_html.select_one('#og_image')['src']
            self.products_dict[self.position]['image_url'] = img_url
        except TypeError:
            self.products_dict[self.position]['image_url'] = "Null"
        return


