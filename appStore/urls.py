from django.urls import path
from appStore.views.product.views import *

urlpatterns = [
    path('product/list/', ProductListView.as_view(), name='product_list')
]