from django.urls import path
from appStore.views.product.views import *
from appStore.views.catalog.views import *

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalogs'),
    path('catalog/products/', ProductListView.as_view(), name='product_list'),
    path('catalog/products_create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/products_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
]
