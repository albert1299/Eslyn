from django.forms import *
from appStore.models import Product

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
            'price': TextInput(
                attrs={
                    'placeholder': 'Ingrese el precio',
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
            'category': TextInput(
                attrs={
                    'placeholder': 'Ingrese la categoria',
                }
            ),
        }