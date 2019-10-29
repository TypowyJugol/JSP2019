import math

a=int(input("Wprowadź liczbę a:"))
b=int(input("Wprowadź liczbę b:"))
c=int(input("Wprowadź liczbę c:"))

if a==0:
    print("To nie jest równanie kwadratowe")
else:
    delta=b**2-4*a*c
    print(delta)
    if delta<0:
        print("Równanie nie ma rozwiązań")
    elif delta==0:
        print(-b/2*a)
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("Rozwiązanie 1:",x1)
        print("Rozwiązanie 2:",x2)