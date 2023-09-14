from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactView, ProductListView, ProductDetailView, ProductCreateView, \
    VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/info_about_product/', cache_page(60)(ProductDetailView.as_view()), name='info_about_product'),
    path('createproduct/', ProductCreateView.as_view(), name='create_product'),
    path('updateproduct/<int:pk>/', ProductCreateView.as_view(), name='update_product'),
    path('createversion/', VersionCreateView.as_view(), name='create_version')
]
