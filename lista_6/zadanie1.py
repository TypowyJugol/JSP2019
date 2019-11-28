import trojkat
a=int(input("Podaj bok a: "))
b=int(input("Podaj bok b: "))
c=int(input("Podaj bok c: "))
lista=[a,b,c]
lista=sorted(lista)
suma=lista[0]+lista[1]
if suma<=lista[2]:
    print("Trójkąt o podanych bokach nie istnieje")
else:
    print("Obwód trojkąta to: "+str(trojkat.obwod(a,b,c)))
    print("Pole trojkąta to: "+str(trojkat.pole(a,b,c)))
    print("Trójkąt jest : "+str(trojkat.trojkat_boki(a,b,c)))
    print("Trójkąt jest: "+str(trojkat.trojkat_katy(a,b,c)))
