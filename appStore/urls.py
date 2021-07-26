from django.urls import path

from appStore.views.catalog import views
from appStore.views.product.views import *
from appStore.views.catalog.views import *
from appStore.views.user.views import *
from appStore.views.conctactos.views import *

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalogs'),
   # path('catalog/', CatalogListView.as_view(), name='catalog_list'),
    path('catalog/create/', CatalogCreateView.as_view(), name='catalog_create'),
    path('catalog/products/', ProductListView.as_view(), name='product_list'),
    path('catalog/products_create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/products_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/products/<int:pk>/', product, name='product_view'),
    path('catalog/products_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/<int:pk>/products/', CatalogProductstListView.as_view(), name='catalog_products'),
    path('createUser/', UsuarioCreateView.as_view(), name= "createUser"),
    path('createDataUser/<int:pk>/', DataUserCreateView.as_view(), name= "createDataUser"),
    path('contact/', contact, name='contact'),
]
