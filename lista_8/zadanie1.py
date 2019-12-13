import os
import time

def szyfruj(napis):
    zaszyfrowany = ""
    for i in range(len(napis)):
        if ((ord(napis[i])>=97) and (ord(napis[i])<=122)):
            if ((ord(napis[i]) + KLUCZ) > 122):
                zaszyfrowany += chr(ord(napis[i]) + KLUCZ - 26)
            else:
                zaszyfrowany += chr(ord(napis[i]) + KLUCZ)
        elif ((ord(napis[i])>=65) and (ord(napis[i])<=90)):
            if ((ord(napis[i]) + KLUCZ) > 90):
                zaszyfrowany += chr(ord(napis[i]) + KLUCZ - 26)
            else:
                zaszyfrowany += chr(ord(napis[i]) + KLUCZ)
        else:
            zaszyfrowany += napis[i]
    return zaszyfrowany

while True:
    try:
        dir_path2 = input("Wprowadź ścieżkę do pliku: ")
        f = open(dir_path2, "r")
        napis = f.read()
        f.close()
        break
    except:
        print("Podany plik nie istnieje!")

KLUCZ = int(input("Wprowadź klucz(przesunięcie w szyfrze) w zakresie od 1 do 10: "))
napis_zaszyfrowany = szyfruj(napis)

rok = time.strftime("%Y", time.localtime())
miesiac = time.strftime("%m", time.localtime())
dzien = time.strftime("%d", time.localtime())

dir_path3 = ("plik_zaszyfrowany%" + str(KLUCZ) + "_" + "%" + str(rok) + "%" + str(miesiac) + "%" + str(dzien) + ".txt")

katalog = input("Wprowadź ścieżkę do katalogu w którym mam zapisać plik: ")
try:
    os.makedirs(katalog)
    os.chdir(katalog)
except:
    os.chdir(katalog)

f = open(dir_path3, "w")
f.write(napis_zaszyfrowany)
f.close()


