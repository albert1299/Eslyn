from django.urls import path
from appStore.views.product.views import *
from appStore.views.catalog.views import *
from appStore.views.user.views import *


urlpatterns = [
    path('', CatalogListView.as_view(), name='catalogs'),
    path('createUser/', UsuarioCreateView.as_view(), name= "createUser"),
    path('createDataUser/<int:pk>/', DataUserCreateView.as_view(), name= "createDataUser"),
    path('catalog/products/', ProductListView.as_view(), name='product_list')
]