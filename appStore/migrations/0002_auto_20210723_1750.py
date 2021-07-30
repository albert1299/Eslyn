# Generated by Django 3.2.5 on 2021-07-23 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStore.catalog', verbose_name='Catálogo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/productos/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nombre'),
        ),
    ]