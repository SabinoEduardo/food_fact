# type : ignore

from django.db import models
from django.utils import timezone

# Create your models here.

STATUS_CHOICES = [
    ("Draft", "draft"),
    ("Imported", "imported"),
]

class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    code = models.BigIntegerField(null=True, blank=True)
    barcode = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, blank=False)
    imported_t = models.DateTimeField(default=timezone.now)
    url = models.URLField(null=True, blank=True)
    product_name = models.CharField(max_length=80, null=True, blank=True)
    quantity = models.CharField(max_length=10, null=True, blank=True)
    ingredients = models.CharField(max_length=80, null=True, blank=True)
    labels = models.CharField(max_length=80, null=True, blank=True)
    categories = models.CharField(max_length=80, null=True, blank=True)
    packaging = models.CharField(max_length=80, null=True, blank=True)
    brands = models.CharField(max_length=60, null=True, blank=True)
    processed_foods = models.CharField(max_length=60, null=True, blank=True)
    country_of_manufacture = models.CharField(max_length=80, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Nutrient(models.Model):
    
    energy  = models.CharField(max_length=15, blank=True, null=True)
    fat = models.CharField(max_length=15, blank=True, null=True)
    saturated_fat = models.CharField(max_length=15, blank=True, null=True)
    carbohydrates = models.CharField(max_length=15, blank=True, null=True)
    sugars = models.CharField(max_length=15, blank=True, null=True)
    lactose = models.CharField(max_length=15, blank=True, null=True)
    fiber = models.CharField(max_length=15, blank=True, null=True)
    proteins = models.CharField(max_length=15, blank=True, null=True)
    salt = models.CharField(max_length=15, blank=True, null=True)
    alcohol = models.CharField(max_length=15, blank=True, null=True)
    vitamina_a = models.CharField(max_length=15, blank=True, null=True)
    vitamina_b = models.CharField(max_length=15, blank=True, null=True)
    vitamina_c = models.CharField(max_length=15, blank=True, null=True)
    vitamina_d = models.CharField(max_length=15, blank=True, null=True)
    vitamina_e = models.CharField(max_length=15, blank=True, null=True)
    calcium = models.CharField(max_length=15, blank=True, null=True)
    
    id_product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        blank=False, 
        null=False
        )

    class Meta:
        verbose_name = 'Nutriente'