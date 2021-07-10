from django.db import models

class Data_User(models.Model):
    ci = models.CharField(max_length=150, verbose_name='Cédula', null=False, blank=False)
    phone = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Teléfono', null=False, blank=False)
    address = models.IntegerField(verbose_name='Dirección', null=False, blank=False)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.ci

class Catalog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', null=False, blank=False)
    description = models.CharField(max_length=300, verbose_name='Descripción', null=True, blank=True)
    #image = models.FileField(max_length=150, verbose_name='Categoria')
    category = models.CharField(max_length=150, verbose_name='Categoria', null=False, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', null=False, blank=False)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio', null=False, blank=False)
    stock = models.IntegerField(verbose_name='Stock', null=False, blank=False)
    description = models.CharField(max_length=300, verbose_name='Descripción', null=True, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name




