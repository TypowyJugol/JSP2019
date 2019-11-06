import colorsys

r = int(input("Wprowadz R: "))
g = int(input("Wprowadz G: "))
b = int(input("Wprowadz B: "))

lista = colorsys.rgb_to_hsv(r/255,g/255,b/255)
print(lista[0]*360,lista[1]*100,lista[2]*100)
