#zadanie 2
from random import randint
lista = []
for i in range(0, 10):
    lista.append(randint(0, 100))
print(lista)
lista2 = [(i) for i in lista if i%2==0]
print(lista2)