KLUCZ = 13


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



