# Generated by Django 3.2.5 on 2021-07-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_user',
            name='address',
            field=models.IntegerField(max_length=150, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='data_user',
            name='ci',
            field=models.CharField(max_length=10, unique=True, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='data_user',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Teléfono'),
        ),
    ]