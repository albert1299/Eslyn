from django.db import models

class Data_User(models.Model):
    ci = models.CharField(max_length=10, verbose_name='Cédula', unique=True)
    phone = models.CharField(max_length=10, verbose_name='Teléfono')
    address = models.CharField(max_length=150, verbose_name='Dirección')
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.ci

class Catalog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=300, verbose_name='Descripción', null=True, blank=True)
    image = models.ImageField(upload_to='images/catalogos/')
    category = models.CharField(max_length=150, verbose_name='Categoria')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')
    description = models.CharField(max_length=300, verbose_name='Descripción', null=True, blank=True)
    image = models.ImageField(upload_to='images/productos/')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




