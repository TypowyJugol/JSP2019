
try:
    f = open("PESEL.txt", "r")
    f2 = open("PESEL_ODKODOWANY.txt", "w+")
    pesel = f.readlines()
    tab = [1,3,7,9,1,3,7,9,1,3,1]
    suma = 0
    for i in pesel:
        for a, val in enumerate(i[:-1]):
            suma += (int(val) * tab[a])
        if (suma%10==0):
            if (int(i[9])%2==0):
                plec = ("Kobieta")
            else:
                plec = ("Mężczyzna")
            rok = (i[0:2])
            miesiac = int(i[2:4])
            dzien = (i[4:6])
            if miesiac>12:
                miesiac = miesiac - 20
                rok = "20" + rok
            else:
                rok = "19" + rok
            odkodowany = "nr PESEL: " + i[:-1] + " data urodzenia: " + "%" + dzien + "-%" + str(miesiac) + "-%" + rok + " Płeć: " + plec
            f2.write(odkodowany + "\n")
        else:
            odkodowany = "PESEL NIEPOPRAWNY"
            f2.write(odkodowany + "\n")
        suma = 0

    f.close()
    f2.close()
except:
    print("Plik nie istnieje!")