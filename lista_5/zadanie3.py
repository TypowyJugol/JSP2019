#za sprawdzenie poprawnosci napisu dodatkowe punkty np. napis XXXXXX jest bez sensu
#program ma działać na liczbach do 3000 (n<=3000)

liczba=str(input("Podaj liczbę rzymską:"))

def zamiana(liczba):
    rzymska={"I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000}
    arabska=0
    for i in range(len(liczba)):
        if i>0 and rzymska[liczba[i]]>rzymska[liczba[i-1]]:
            arabska+=rzymska[liczba[i]]-2*rzymska[liczba[i-1]]
        else:
            arabska+=rzymska[liczba[i]]
    if(arabska<= 3000):
        print(arabska)
    else:
        print("Liczba nie mieści się w przedziale od 0 do 3000!")

zamiana(liczba)