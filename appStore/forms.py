from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appStore.models import *

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            #form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre',
                }
            ),
            'price': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el precio',
                    'min': 1
                }
            ),
            'stock': TextInput(
                attrs={
                    'placeholder': 'Ingrese el stock',
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Ingrese la descripción',
                    'rows': 2,
                    'cols': 2
                }
            ),
            'image': FileInput(
                attrs={
                    'label': 'Imagenss',
                }
            ),
        }

class CatalogForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            # form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    class Meta:
         model = Catalog
         fields = '__all__'
         widgets = {
            'name': TextInput(
                attrs={
                   'placeholder': 'Ingrese el nombre',
                }
            ),
            'description': Textarea(
                 attrs={
                     'placeholder': 'Ingrese la descripción',
                     'rows': 2,
                     'cols': 2
                 }
            ),
            'image': FileInput(
                  attrs={
                      'label': 'Imagenss',
                  }
            ),
         }
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
        