from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from appStore.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos del catálogo'
        context['object_list'] = Product.objects.filter(catalog=2)
        return context