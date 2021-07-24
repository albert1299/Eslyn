from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.urls import reverse_lazy

from appStore.models import Product
from appStore.forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos del catálogo'
        context['create_url'] = reverse_lazy('product_create')
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear producto'
        context['create_url'] = reverse_lazy('product_create')
        return context

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar producto'
        context['update_url'] = reverse_lazy('product_update')
        return context

class ProductDeleteView(DeleteView):
    model = Product
    # form_class = ProductForm
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Producto'
        # context['entity'] = 'Producto'
        context['delete_url'] = 'product_delete'
        return context

class CatalogProductstListView(ListView):
    model = Product
    template_name = 'product/catalog_list.html'
    success_url = reverse_lazy('catalog_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos del catálogo'
        context['object_list'] = Product.objects.filter(catalog=self.kwargs['pk'])
        context['create_url'] = reverse_lazy('product_create')
        return context