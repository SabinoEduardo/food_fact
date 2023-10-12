from django.db import models
from django.utils import timezone

# Create your models here.

STATUS_CHOICES = [
    ("Draft", "draft"),
    ("Imported", "imported"),
]

class Product(models.Model):
    code = models.BigIntegerField(null=True)
    barcode = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, blank=False)
    imported_t = models.DateTimeField(default=timezone.now)
    url = models.URLField(null=True, blank=True)
    product_name = models.CharField(max_length=80, null=True, blank=True)
    quantity = models.CharField(max_length=10)
    categories = models.CharField(max_length=80, null=True, blank=True)
    packaging = models.CharField(max_length=80, null=True, blank=True)
    brands = models.CharField(max_length=60, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
