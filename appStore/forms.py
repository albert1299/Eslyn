from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appStore.models import Data_User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password1', 'password2'
        labels = {'first_name':'Nombre', 'last_name':'Apellido','email': 'Correo','username': 'Nombre de usuario', 'password1': 'Contraseña'}
        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su Usuario',
                    'class': 'form-control',
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su primer nombre',
                    'class': 'form-control',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese su apellido',
                    'class': 'form-control',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrese su correo',
                    'class': 'form-control',
                }
            ),
            'password1': EmailInput(
                attrs={
                    'placeholder': 'Contraseña',
                    'class': 'form-control',
                }
            ),
        }

class DataUserForm(ModelForm):

    class Meta:
        model = Data_User
        fields = 'ci', 'phone', 'address'
        labels = {'ci':'Número de cédula', 'phone':'Número de teléfono','address': 'Dirección'}
        widgets = {
            'ci': TextInput(
                attrs={
                    'placeholder': 'Ingrese su cédula',
                    'class': 'form-control',
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': 'Ingrese su número de teléfono',
                    'class': 'form-control',
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                    'class': 'form-control',
                }
            ),
        }
        