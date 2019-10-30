
m=int(input("Wprowadz liczbę wierszy:"))
n=int(input("Wprowadz liczbe kolumn:"))

tablica=[]
for i in range(m):
    tablica.append([])
    for j in range(n):
        tablica[i].append(i*j)

print(tablica)