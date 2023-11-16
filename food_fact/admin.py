from django.contrib import admin
from food_fact import models

# Register your models here.

@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["id", "code", "barcode", "status",
              "imported_t", "url", "product_name",
              "quantity", "categories", "packaging",
              "brands", "image_url"]

    list_display_links = ("id", "code",)
    list_per_page = 10
    ordering = ('id',)
    search_fields = ("code", "product_name",)
    search_help_text = "Pesquise pelo nome ou código do produto"


@admin.register(models.Nutrient)
class AdminNutrient(admin.ModelAdmin):
    list_display = ['id_product', 'energy', 'fat', 
                    'saturated_fat', 'carbohydrates', 
                    'sugars', 'lactose', 'fiber', 
                    'proteins', 'salt', 'alcohol', 
                    'vitamina_a', 'vitamina_b', 'vitamina_c', 
                    'vitamina_d', 'vitamina_e', 'calcium']

    list_display_links = ('id_product',)
    list_per_page = 10
    ordering = ('id_product',)
    
