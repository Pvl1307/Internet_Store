from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, products, info_about_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/info_about_product/', info_about_product, name='info_about_product')
]