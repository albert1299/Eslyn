from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import *
from appStore.models import Catalog
from appStore.forms import *
from django.urls import reverse_lazy
from appStore.models import *

class CatalogListView(ListView):
    model = Catalog
    template_name = 'catalog/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('catalog_create')
        return context

class CatalogCreateView(CreateView):
    model = Catalog
    form_class = CatalogForm
    template_name = 'catalog/create.html'
    success_url = reverse_lazy('catalogs')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Catálogo'
        context['create_url'] = reverse_lazy('catalog_create')
        return context