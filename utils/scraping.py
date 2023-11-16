# type: ignore

class Date:
    """
        This class create one object of products with the following datas:

            :url : str
            :Code : int
            :Barcode : str
            :quantity : str
            :name : str
            :categories : str
            :packaging : str
            :brands : str
            :image_url :str

        The functions this class return None

        Será adicionado funções para adicionar os seguintes campos:
            - labels (rótulos: com glutem, sem conservantes etc)
            - ingredientes
            - tipo de processamento: (ultraprocessado por exemplo)
            - Nutrition facts (em 15g)

    """

    def __init__(self, url, content_html, position, products_dict, nutrition_dict):
        self.url = url
        self.position = position
        self.products_dict = products_dict
        self.nutrition_dict = nutrition_dict
        self.content_html = content_html
        self.name_product = ""
        self.quantity = ""
        self.brand = ""
        

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
            self.quantity = self.content_html.select_one('#field_quantity_value').text
            self.products_dict[self.position]['quantity'] = self.quantity
        except AttributeError:
            self.products_dict[self.position]['quantity'] = "Null"
        return
    
    async def get_ingredients(self):
        try:
            ingredient = self.content_html.select_one('#panel_ingredients_content > div > div > div').text.strip()
            self.products_dict[self.position]['ingredient'] = ingredient
        except AttributeError:
            self.products_dict[self.position]['ingredient'] = "Null"
        return
    
    async def get_processed_foods(self):
        try:
            processed_foods = self.content_html.select_one('#panel_nova > li > a > h4').string
            self.products_dict[self.position]['processed_foods'] = processed_foods.strip()
        except AttributeError:
            self.products_dict[self.position]['processed_foods'] = "Null"
        return
    
    async def get_manufactured(self):
        try:
            country_of_manufacture = self.content_html.select_one('#field_manufacturing_places_value > a:nth-child(2)').string
            self.products_dict[self.position]['country_of_manufacture'] = country_of_manufacture.strip()
        except AttributeError:
            self.products_dict[self.position]['country_of_manufacture'] = "Null"
        return
    
    async def get_labels(self):
        try:
            labels = ""
            labels_values = self.content_html.select('a[href^="/label/"]')
            for i, texto in enumerate(labels_values):
                labels = labels + texto.text.strip()
                if i < len(labels_values)-1:
                    labels += ", "
            self.products_dict[self.position]['labels'] = labels
        except AttributeError:
            self.products_dict[self.position]['labels'] = "Null"
        return


    async def get_brands(self):
        """
            Function to get the brand of product.
            :return: without return
        """
        try:
            self.brand = self.content_html.select_one('#field_brands a').text
            self.products_dict[self.position]['brand'] = self.brand
        except AttributeError:
            self.products_dict[self.position]['brand'] = "Null"
        return

    async def config_name(self):
        """
            Function to get the name of product.
            :return: without return
        """
        try:
            self.name_product = self.content_html.select_one('[itemscope] h1').text
            self.products_dict[self.position]['product_name'] = self.name_product
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
    

    async def get_nutrition_facts(self):
        """
            Essa função define os valores dos nutrientes dos produtos.
            Os nutriente são os da lista abaixo
        """
        
        # lista contendo todos os nutriente de acordo com a tabela de nutrientes do DB
        nutrients_of_db = ['Energy', 'Fat', 'Saturated fat', 'Carbohydrates', 
                               'Sugars', 'Lactose', 'Fiber', 'Proteins', 'Salt', 
                               'Alcohol', 'Vitamina A', 'Vitamina B', 'Vitamina C', 
                               'Vitamina D', 'Vitamina E', 'Calcium']
        
        list_nutrition_names = list()
        list_nutrition_values = list()
        dict_nutri_info = dict()

        self.nutrition_dict[self.position] = {}
        dict_nutri_info['product_name'] = self.name_product

        try:
            # Seleciona todas os nomes dos nutrientes e adicona na lista 
            nutritions_name_tag = self.content_html.select('#panel_nutrition_facts_table_content > div > table > tbody > tr > td:nth-child(1) > span')
            #print(nutritions_name_tag)
            for nutrition_name in nutritions_name_tag:
                list_nutrition_names.append(nutrition_name.text.strip())

            # Seleciona todos os valores do nutriente e adiciona em uma lista
            nutritions_value_tag = self.content_html.select('#panel_nutrition_facts_table_content > div > table > tbody > tr > td:nth-child(2) > span')
            
            for nutrition_value in nutritions_value_tag:
                list_nutrition_values.append(nutrition_value.text.strip())

            # Adiciona informações nutricionais para o dicionário dict_nutri_info
            for nutri_db in nutrients_of_db:

                # Verifica se cada nome do nutriente do DB está presente na lista de nutrientes que veio do scraping
                if nutri_db in list_nutrition_names:
                    pos = list_nutrition_names.index(nutri_db)
                    _value = list_nutrition_values[pos].strip()
                else:
                    _value = "Null"

                nutri_db = nutri_db.lower()
                dict_nutri_info[nutri_db] = _value

            self.nutrition_dict[self.position] = dict_nutri_info

        except AttributeError:
            for nutri in nutrients_of_db:
                dict_nutri_info[nutri] = "Null"
            self.nutrition_dict[self.position] = dict_nutri_info
        return
