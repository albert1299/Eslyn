from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from appStore.models import Catalog

def contact(request):
  return render(request,'contactos/list.html')

