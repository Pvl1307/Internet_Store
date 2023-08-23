from django.urls import path

from weblog.apps import WeblogConfig
from weblog.views import WeBlogCreateView, WeBlogListView, WeBlogDetailView, WeBlogUpdateView, WeBlogDeleteView

app_name = WeblogConfig.name

urlpatterns = [
    path('create/', WeBlogCreateView.as_view(), name='create'),
    path('', WeBlogListView.as_view(), name='list'),
    path('view/<int:pk>/', WeBlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', WeBlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', WeBlogDeleteView.as_view(), name='delete')
]
