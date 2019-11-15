#funkcja(1511)="tysiąc pięćset jedenaście"          obowiązkowe assercje
#funkcja(698)="sześćset dziewięćdziesiąt osiem"

liczba=int(input("Wprowadź liczbę:"))

def zamiana(liczba):

    jedności={1:"jeden",
              2:"dwa",
              3:"trzy",
              4:"cztery",
              5:"pięć",
              6:"sześć",
              7:"siedem",
              8:"osiem",
              9:"dziewięć"}

    dziesiątki={1:"dziesięć",
                2:"dwadzieśćia",
                3:"trzydzieści",
                4:"czterdzieści",
                5:"pięćdziesiąt",
                6:"szseśćdziesiąt",
                7:"siedemdziesiąt",
                8:"osiemdziesiąt",
                9:"dziewięćdziesiąt"}

    setki={1:"sto",
           2:"dwieście",
           3:"trzysta",
           4:"czterysta",
           5:"pięćset",
           6:"sześćset",
           7:"siedemset",
           8:"osiemset",
           9:"dziewięćset",}

    tysiące={1:"tysiąc"}

    znane ={1:"jeden",
            2:"dwa",
            3:"trzy",
            4:"cztery",
            5:"pięć",
            6:"sześć",
            7:"siedem",
            8:"osiem",
            9:"dziewięć",
            10:"dziesięć",
            11:"jedenaście",
            12:"dwanaście",
            13:"trzynaście",
            14:"czternaście",
            15:"piętnaście",
            16:"szesnaście",
            17:"siedemnaście",
            18:"osiemnaście",
            19:"dziewiętnaście",
            20:"dwadzieścia",
            30:"trzydzieści",
            40:"czterdzieści",
            50:"pięćdziesiąt",
            60:"szseśćdziesiąt",
            70:"siedemdziesiąt",
            80:"osiemdziesiąt",
            90:"dziewięćdziesiąt",
            100:"sto",
            200:"dwieście",
            300:"trzysta",
            400:"czterysta",
            500:"pięćset",
            600:"sześćset",
            700:"siedemset",
            800:"osiemset",
            900:"dziewięćset",
            1000:"tysiąc"}

    if liczba in znane:
        print(znane[liczba])
    else:
        liczba=str(liczba)
        innaliczba=[]
        for l in liczba:
            innaliczba.append(l)

        lista=[]

        for i in range(len(innaliczba)):
            x=innaliczba[i]
            x=int(x)
            lista.append(x)

        if len(lista)==4:
            s=""
            for i in range(len(lista)):
                x=str(lista[i])
                s+=x
            y=s[-2:]
            y=int(y)
            if y in znane:
                print(tysiące[lista[0]] + " " + setki[lista[1]] + " " + znane[y])
            else:
                print(tysiące[lista[0]]+" "+setki[lista[1]]+" "+dziesiątki[lista[2]]+" "+jedności[lista[3]])
        elif len(lista)==3:
            s = ""
            for i in range(len(lista)):
                x = str(lista[i])
                s += x
            y = s[-2:]
            y = int(y)
            if y in znane:
                print(setki[lista[0]] + " " + znane[y])
            else:
                print(setki[lista[0]] + " " + dziesiątki[lista[1]] + " " + jedności[lista[2]])
        elif len(lista)==2:
            print(dziesiątki[lista[0]]+" "+jedności[lista[1]])
        else:
            print(jedności[lista[0]])

zamiana(liczba)

#to samo co w zadaniu 1
#assert zamiana(1511)=="tysiąc pięćset jedenaście"
#assert zamiana(698)=="sześćset dziewięćdziesiąt osiem"
