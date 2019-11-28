KLUCZ = 13


def szyfruj(napis):
    zaszyfrowany = ""
    for i in range(len(napis)):
        if ord(napis[i]) > 122 - KLUCZ:
            zaszyfrowany += chr(ord(napis[i]) + KLUCZ - 26)
        else:
            zaszyfrowany += chr(ord(napis[i]) + KLUCZ)
    return zaszyfrowany


def deszyfruj(napis):
    zdeszyfrowany = ""
    KLUCZM = KLUCZ % 26
    for i in range(len(napis)):
        if (ord(napis[i]) - KLUCZM < 97):
            zdeszyfrowany += chr(ord(napis[i]) - KLUCZM + 26)
        else:
            zdeszyfrowany += chr(ord(napis[i]) - KLUCZM)
    return zdeszyfrowany