from django.test import TestCase
from food_fact.models import Product
import json

class SimpleTest(TestCase):
    """
        class contendo todos o métodos para teste da aplicação.
    """
    def model_product(self):
        """
            Esse método testa a minha classe Products do models.py
        """
        Product.objects.create(
                                code=3274080005003, 
                                barcode='123456767/abcd', 
                                status='draft'
                            )
    def viewstest_msg(self):
        """
            Este método testa o status code do response do endpoint '/'
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def viewstest_list_products(self):
        """
            Este método testa o status code do response do endpoint '/products/'
        """
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

    def viewstest_get_product(self):
        """
            Este método testa o status code do response do endpoint '/products/{code}'

            O code é o código do produto
        """
        response = self.client.get(f"/products/{3274080005003}/")
        self.assertEqual(response.status_code, 200)

    def list_products_is_isntace(self):
        """
            Este método testa o tipo de dados (json) do conteudo do response do 
            endpoint '/products/'
        """
        response = self.client.get("/products/")
        self.assertIsInstance(response.content, json)

    def products_is_isntace(self):
        """
            Este método testa o tipo de dados (json) do conteudo do response do 
            endpoint '/products/{code}'

            O code é o código do produto
        """
        response = self.client.get("/products/{3274080005003}/")
        self.assertIsInstance(response.content, json)
        