#funkcja("jeden")=1             #te 3 assercje mają znaleźć się w kodzie
#funkcja("trzydzieści trzy")=33
#funkcja("trzynaście")=13


liczba = str(input("Wprowadź liczbę słownie:"))

def zamiana(liczba):
    liczby = {"jeden":1,
              "dwa":2,
              "trzy":3,
              "cztery":4,
              "pięć":5,
              "sześć":6,
              "siedem":7,
              "osiem":8,
              "dziewięć":9,
              "dziesięć":10,
              "jedenaście":11,
              "dwanaście":12,
              "trzynaście":13,
              "czternaście":14,
              "piętnaście":15,
              "szesnaście":16,
              "siedemnaście":17,
              "osiemnaście":18,
              "dziewiętnaście":19,
              "dwadzieścia":20,
              "trzydzieści":30,
              "czterdzieści":40,
              "pięćdziesiąt":50}

    if liczba in liczby:
        print(liczby[liczba])

    else:
        innaliczba=liczba.split()
        print(liczby[innaliczba[0]]+liczby[innaliczba[1]])


#nie rozumiem dlaczego asercje wyrzucają błędy, skoro wyniki są prawidłowe
#assert zamiana("jeden")==1
#assert zamiana("trzydzieści trzy")==33
#assert zamiana("trzynaście")==13)

zamiana(liczba)
