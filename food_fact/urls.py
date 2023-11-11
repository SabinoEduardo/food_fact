from django.urls import path
from food_fact import views

app_name = 'food_fact'

urlpatterns = [
    #boas vindas
    path('', views.msg, name='home'),

    #Listar os produtos
    path('products/', views.list_products, name='list_products'),

    #Filtar um produto pelo nome (name) ou marca (brand)
    path('products/search/', views.search, name='serach'),

    #Buscar um produto pelo código
    path('products/<int:code_product>/', views.get_product, name='one_product'),
]