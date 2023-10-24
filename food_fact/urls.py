from django.urls import path
from food_fact import views

app_name = 'food_fact'

urlpatterns = [
    #Listar os produtos
    path('products', views.list_products, name='list'),

    #Buscar um produto
    path('products/<int:code_product>/', views.get_product, name='product')
]