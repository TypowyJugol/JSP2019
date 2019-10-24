x=["Kasia","Basia","Marek","Darek"]
x.append("Józek")
x.extend(["Ania","Basia"])
x.sort()
print("Czwarty:",x[3],"Dwóch pierwszych:",x[0:2],"Dwóch ostatnich",x[-2:])
x=list(set(x))
x.remove("Basia")
print(len(x))
x=tuple(x)
print(x)

