import math

def obwod(a,b,c):
    return a+b+c

def pole(a,b,c):
    p=1/2*(a+b+c)
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def trojkat_boki(a,b,c):
    if(a==b) and (a==c) and (b==c):
        return "równoboczny"
    elif (a==b) or (a==c) or (b==c):
        return "równoramienny"
    else:
        return "różnoboczny"

def trojkat_katy(a,b,c):
    if((a**2)+(b**2)==c**2):
        return "prostokątny"
    elif(a**2+b**2>c**2):
        return "ostrokątny"
    else:
        return "rozwartokątny"