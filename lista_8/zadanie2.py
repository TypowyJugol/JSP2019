import os
import time
import re


def deszyfruj(napis):
    zdeszyfrowany = ""
    for i in range(len(napis)):
        if ((ord(napis[i]) >= 97) and (ord(napis[i]) <= 122)):
            if ((ord(napis[i]) - KLUCZ) < 97):
                zdeszyfrowany += chr(ord(napis[i]) - KLUCZ + 26)
            else:
                zdeszyfrowany += chr(ord(napis[i]) - KLUCZ)
        elif ((ord(napis[i]) >= 65) and (ord(napis[i]) <= 90)):
            if ((ord(napis[i]) - KLUCZ) < 65):
                zdeszyfrowany += chr(ord(napis[i]) - KLUCZ + 26)
            else:
                zdeszyfrowany += chr(ord(napis[i]) - KLUCZ)
        else:
            zdeszyfrowany += napis[i]
    return zdeszyfrowany

x = 1
while x==1:
    try:
        dir_path2 = input("Wprowadź ścieżkę do katalogu: ")
        pliki = os.listdir(dir_path2)
        if (bool(pliki)==False):
            print("W podanym katalogu nie ma plików")
        else:
            break
    except:
        print("Podany katalog nie istnieje")


for i in range(len(pliki)):
    plik = str(pliki[i])
    try:
        temp = (re.search("plik_zaszyfrowany%._", plik)).group(0)
        KLUCZ = int(temp[18])
        os.chdir(dir_path2)
        f = open(plik, "r")
        napis = f.read()
        f.close()
        napis_deszyfrowany = deszyfruj(napis)

        rok = time.strftime("%Y", time.localtime())
        miesiac = time.strftime("%m", time.localtime())
        dzien = time.strftime("%d", time.localtime())

        dir_path3 = ("plik_deszyfrowany%" + str(KLUCZ) + "_" + "%" + str(rok) + "%" + str(miesiac) + "%" + str(dzien) + ".txt")
        f = open(dir_path3, "w")
        f.write(napis_deszyfrowany)
        f.close()
    except:
        pass