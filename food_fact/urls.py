from django.urls import path
from food_fact import views

app_name = 'food_fact'

urlpatterns = [
    path('', views.list_products, name='base'),
]