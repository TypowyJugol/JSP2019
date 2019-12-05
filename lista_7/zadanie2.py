import random
import time

lista = []


def sortowanie_przez_wstawianie(arg):
    for i in range(1, len(arg)):
        key = arg[i]
        j = i - 1
        while j >= 0 and arg[j] > key:
            arg[j + 1] = arg[j]
            j -= 1
        arg[j + 1] = key
    return arg


def generuj(x):
    for i in range(x):
        lista.append(random.randint(1, 20))
    return lista


generuj(100)
start=time.time()
print("Dla 100 liczb:")
print(sortowanie_przez_wstawianie(lista))
stop=time.time()
print("Czas: "+ str(stop-start))
generuj(200)
start=time.time()
print("Dla 200 liczb:")
print(sortowanie_przez_wstawianie(lista))
stop=time.time()
print("Czas: "+ str(stop-start))
generuj(300)
start=time.time()
print("Dla 300 liczb:")
print(sortowanie_przez_wstawianie(lista))
stop=time.time()
print("Czas: "+ str(stop-start))