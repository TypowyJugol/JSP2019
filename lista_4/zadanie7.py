x=int(input("Podaj liczbę wierszy: "))

l=[1]
for i in range(x):
    print(l)
    y=[]
    y.append(l[0])
    for i in range(len(l)-1):
        y.append(l[i]+l[i+1])
    y.append(l[0])
    l=y
