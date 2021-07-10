from app.wsgi import *
from appStore.models import *

data = ['Blusa', 'Pantalon', 'Calentador',
        'Abrigo', 'Bufanda', 'Camiseta',
        'Camisa', 'Falda', 'Pantaloneta',
        'Buzo', 'Vestido']

for i in data:
    prod = Product(name=i)
    prod.save()

