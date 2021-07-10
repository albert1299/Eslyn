# Generated by Django 3.2.5 on 2021-07-10 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='images/catalogos/')),
                ('category', models.CharField(max_length=150, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='images/productos/')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStore.catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Data_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=150, unique=True, verbose_name='Cédula')),
                ('phone', models.CharField(max_length=150, verbose_name='Teléfono')),
                ('address', models.IntegerField(verbose_name='Dirección')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
