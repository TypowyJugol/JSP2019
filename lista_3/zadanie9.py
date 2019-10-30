
m = int(input("Wprowadz wartosc m: "))
n = int(input("Wprowadz wartosc n: "))

tablica= []
for i in range(m):
    tablica.append([])
    for j in range(n):
        tablica[i].append(i*j)

print(tablica)