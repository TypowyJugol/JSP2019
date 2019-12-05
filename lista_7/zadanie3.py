import random
import time

lista = []

def sortowanie_babelkowe(arg):
    n = len(arg)
    i = 0
    while(n>1):
        while(i < n-1):
            if(arg[i] > arg[i+1]):
                temp = arg[i]
                temp2 = arg[i+1]
                arg[i] = temp2
                arg[i+1] = temp
            i = i+1
        n = n-1
        i = 0
    return arg


def generuj(x):
    for i in range(x):
        lista.append(random.randint(1,20))
    return lista

generuj(100)
start=time.time()
print("Dla 100 liczb:")
print(sortowanie_babelkowe(lista))
stop=time.time()
print("Czas: "+str(stop-start))
generuj(200)
start=time.time()
print("Dla 200 liczb:")
print(sortowanie_babelkowe(lista))
stop=time.time()
print("Czas: "+str(stop-start))
generuj(300)
start=time.time()
print("Dla 300 liczb:")
print(sortowanie_babelkowe(lista))
stop=time.time()
print("Czas: "+str(stop-start))