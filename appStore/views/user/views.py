from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


from appStore.models import Data_User
from appStore.forms import UserForm, DataUserForm

class UsuarioCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    #success_url = reverse_lazy('createDataUser')

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST) 
        if form.is_valid():
            user = form.save()
            print(user.pk)
            return redirect('createDataUser',user.pk)

        return render(request, 'user/create.html', {'form':form})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Usuario'
        return context

class DataUserCreateView(CreateView):
    model = Data_User
    form_class = DataUserForm
    template_name = 'user/create_dataUser.html'

    def post(self, request, *args, **kwargs):
        form = DataUserForm(request.POST) 
        if form.is_valid():
            dataUser = form.save(commit=False)
            dataUser.user_id = self.kwargs['pk']
            dataUser.save()
            return redirect('catalogs')

        return render(request, 'user/create_dataUser.html', {'form':form})       


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Usuario'
        return context
