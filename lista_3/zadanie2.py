liczba=int(input("Wprowadz liczbę:"))
if liczba%2==1:
    print("Liczba jest nieparzysta")
else:
    print("Liczba jest parzysta")

#wersja bez instrukcji if

liczba=int(input("Podaj liczbę:"))
x=["Liczba jest parzysta", "Liczba jest nieparzysta"]

print(x[liczba%2])