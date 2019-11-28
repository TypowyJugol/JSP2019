KLUCZ = 13


def szyfruj(napis):
    zaszyfrowany = ""
    for i in range(len(napis)):
        if (((ord(napis[i])>=65) and (ord(napis[i])<=90)) or ((ord(napis[i])>=97) and (ord(napis[i])<=122))):
            if (ord(napis[i]) > (122 - KLUCZ)):
                zaszyfrowany += chr(ord(napis[i]) + KLUCZ - 26)
            else:
                zaszyfrowany += chr(ord(napis[i]) + KLUCZ)
        else:
            zaszyfrowany += napis[i]
    return zaszyfrowany

def deszyfruj(napis):
    zdeszyfrowany = ""
    for i in range(len(napis)):
        if (((ord(napis[i]) >= 65) and (ord(napis[i]) <= 90)) or ((ord(napis[i]) >= 97) and (ord(napis[i]) <= 122))):
            if ((ord(napis[i]) - KLUCZ) < 97):
                zdeszyfrowany += chr(ord(napis[i]) - KLUCZ + 26)
            else:
                zdeszyfrowany += chr(ord(napis[i]) - KLUCZ)
        else:
            zdeszyfrowany += napis[i]
    return zdeszyfrowany



