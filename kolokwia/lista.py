import os
if os.path.exists("lista.txt")==False:
    dopisz = 0
    ile = 0
    t_ile = []
    imie = []
    nazwisko = []
    indeks = []
    ocena = []
    while dopisz==0:
        dopisz = int(input("Czy dopisać nowego studenta 0-tak 1-nie?:"))
        if dopisz == 0:
            plik = open("lista.txt","a")
            t_imie = input("Podaj imie:")
            imie.append(t_imie)
            t_nazwisko = input("Podaj nazwisko:")
            nazwisko.append(t_nazwisko)
            t_indeks = input("Podaj indeks:")
            indeks.append(t_indeks)
            t_ocena = input("Podaj ocene:")
            ocena.append(t_ocena)
            student =ile + " " + t_imie + " " + t_nazwisko + " " + str(t_indeks) + " " + str(t_ocena)

            plik.write(student)
            plik.write("\n")
            plik.close()
            ile += 1
else:
    plik = open("lista.txt","r")
    print(plik.read())
    for line in plik.readlines():
        temp = line.split()
        t_ile.append(temp[0])
        imie.append(temp[1])
        nazwisko.append(temp[2])
        indeks.append(temp[3])
        ocena.append(temp[4])
    plik.close()

    plik = open("lista.txt", "a")
    while True:
        dopisz = int(input("Dopisać nowego studenta(1) czy zmienic ocene(0):"))
        if dopisz==0:
            i = int(input("Podaj numer studenta na liście:"))
            ocena[i] = input()
        if dopisz==1:
            ile.append(len(t_ile))
            t_imie = input("Podaj imie:")
            imie.append(t_imie)
            t_nazwisko = input("Podaj nazwisko:")
            nazwisko.append(t_nazwisko)
            t_indeks = input("Podaj indeks:")
            indeks.append(t_indeks)
            t_ocena = input("Podaj ocene:")
            ocena.append(t_ocena)
            student = ile + " " + t_imie + " " + t_nazwisko + " " + str(t_indeks) + " " + str(t_ocena)

            plik.write(student)
            plik.write("\n")
            plik.close()
            ile += 1

