import random
import numpy

N = int(input("Podaj dlugosc listy: "))
M = int(input("Podaj przedzial wylosowanych liczb: "))
x=random.sample(range(M), N)


def my_argsort(lista):
    print(sorted(range(len(lista)), key=lambda k: lista[k]))

my_argsort(x)
