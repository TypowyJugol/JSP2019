key={"a":"y",
     "e":"i",
     "i":"o",
     "o":"a",
     "y":"e"}

zdanie=input("Podaj zdanie: ")



def szyfr(zdanie, key):
    for i in zdanie:
        if i in key.keys():
            zdanie=zdanie.replace(i,key[i])
        else:
            continue
    print(zdanie)

def deszyfr(zdanie, key):
    reverse_key=dict(map(reversed,key.items()))
    for i in zdanie:
        if i in reverse_key.items():
            zdanie=zdanie.replace(i,reverse_key[i])
        else:
            continue
    print(zdanie)

szyfr(zdanie,key)
deszyfr(zdanie,key)