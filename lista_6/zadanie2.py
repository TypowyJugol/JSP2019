import SzyfrCezara

napis=str(input("Podaj napis do zaszyfrowania: "))
x=int(input("Jeśli chcesz zaszyfrować wybierz 1, jeśli nie wybierz 0: "))
if x==1:
    print(SzyfrCezara.szyfruj(napis))
else:
    print(SzyfrCezara.deszyfruj(napis))