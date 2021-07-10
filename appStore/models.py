from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    size = models.CharField(max_length=10, verbose_name='Talla')
    color = models.CharField(max_length=25, verbose_name='Color')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    description = models.CharField(max_length=300, verbose_name='Descripcion')
    category = models.CharField(max_length=150, verbose_name='Categoria')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name


