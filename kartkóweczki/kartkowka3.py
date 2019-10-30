#ZADANIE 1
x=[0,10,8,3,5,4,7]
for i in x:
    if i%2==1:
        print(i)
    else:
        continue

#ZADANIE 2
g="*"

N=int(input("Wprowadź liczbę N:"))
for i in range(N):
    print(str(g)*i)
    z=str(g)*i

for i in range(N):
    print(z[:-i])
