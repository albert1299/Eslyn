from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from appStore.models import Catalog

class CatalogListView(ListView):
    model = Catalog
    template_name = 'catalog/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context