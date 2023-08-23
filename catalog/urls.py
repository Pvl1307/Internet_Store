from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/info_about_product/', ProductDetailView.as_view(), name='info_about_product')
]
