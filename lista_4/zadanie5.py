import math
lista=[1,2,3,4,5,6,7]
silnia=[]


for i in range(len(lista)):
    n=lista[i]
    silnia.append(math.factorial(n))

print(silnia)

