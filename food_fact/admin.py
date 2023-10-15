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
